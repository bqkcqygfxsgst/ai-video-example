#!/usr/bin/env python3
"""Ingest user-picked Vidu Q2 Turbo posts (manual=True)."""
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path("/workspace/ai-videos-2026-09-14")
META = ROOT / "meta"
sys.path.insert(0, str(META))

import process as P  # noqa: E402

MODEL = "Vidu Q2 Turbo"

CANDS = [
    {
        "id": "1972777135585845652",
        "handle": "talinkacreator",
        "likes": 15,
        "views": 469,
        "followers": 146,
        "date": "2025-09-29",
        "dur_ms": 28000,
        "video_url": "https://video.twimg.com/amplify_video/1972777041322754048/vid/avc1/1920x1080/K6GLigag40qge1tD.mp4",
        "caption": "Testing Vidu Q2 Turbo in PolloAI — faster, smoother, and with stunning cinematic motion.",
        "sell": "超现实霓虹城市",
        "evidence": "Testing Vidu Q2 Turbo in PolloAI #ViduQ2Turbo",
    },
    {
        "id": "1974599085790466188",
        "handle": "talinkacreator",
        "likes": 21,
        "views": 193,
        "followers": 146,
        "date": "2025-10-04",
        "dur_ms": 20367,
        "video_url": "https://video.twimg.com/amplify_video/1974598986787954689/vid/avc1/1080x1914/7YwATCK3-vwUqW9j.mp4",
        "caption": "Created in PolloAI with Vidu Q2 Turbo: thousands of glowing butterflies",
        "sell": "秋日蝴蝶群",
        "evidence": "Created in PolloAI with Vidu Q2 Turbo #ViduQ2Turbo",
    },
    {
        "id": "1973474393109176770",
        "handle": "talinkacreator",
        "likes": 15,
        "views": 289,
        "followers": 146,
        "date": "2025-10-01",
        "dur_ms": 41266,
        "video_url": "https://video.twimg.com/amplify_video/1973474222623043585/vid/avc1/1080x1920/R63VkJUqhYbLQ2Ek.mp4",
        "caption": "Image-to-Video with Vidu Q2 Turbo, Kling 2.5 Turbo and 1.2.5",
        "sell": "图生视频实验",
        "evidence": "Image-to-Video with Vidu Q2 Turbo #ViduQ2Turbo",
    },
]


def next_n() -> int:
    n = 201
    if P.VIDEOS.exists():
        for p in P.VIDEOS.glob("*.mp4"):
            try:
                n = max(n, int(p.name.split("_")[0]))
            except ValueError:
                pass
    acc = META / "accepted.jsonl"
    if acc.exists():
        for line in acc.read_text().splitlines():
            if not line.strip():
                continue
            o = json.loads(line)
            if o.get("n"):
                n = max(n, int(o["n"]))
    return n + 1


def ingest_one(c: dict, idx: int) -> str:
    handle = c["handle"].lstrip("@")
    c = {**c, "model": MODEL, "manual": True, "handle": handle}
    model_slug = P.slug_model(c["model"])
    sid = str(c["id"]).split("-")[0][-6:]
    stem = f"{idx:03d}_{model_slug}_@{handle}_{sid}"
    tweet = f"https://x.com/{handle}/status/{c['id']}"
    print(f"\n[{idx:03d}] @{handle} {c['id']}", flush=True)

    raw = P.RAW / f"{stem}_src.mp4"
    final = P.VIDEOS / f"{stem}.mp4"
    ok = False
    if c.get("video_url"):
        ok = P.download_curl(c["video_url"], raw)
    if not ok:
        ok = P.download_ytdlp(tweet, raw)
    if not ok or not raw.exists():
        print("  FAIL download", flush=True)
        return "fail"

    dur = P.ffprobe_duration(raw)
    if dur is None:
        print("  FAIL duration", flush=True)
        return "fail"
    print(f"  duration={dur:.2f}s size={raw.stat().st_size/1e6:.1f}MB", flush=True)

    if not P.transcode_1080(raw, final):
        print("  FAIL transcode", flush=True)
        return "fail"
    raw.unlink(missing_ok=True)

    frames = P.extract_frames(final, stem, dur)
    reports = []
    try:
        for fp in frames:
            reports.append(P.ocr_frame(fp))
        purity, ocr_meta = P.judge_ocr(reports)
    except Exception as e:
        print("  OCR error", e, flush=True)
        purity, ocr_meta = "OCR失败-人工待核", {"error": str(e)}
    print(f"  purity={purity} ocr={ocr_meta}", flush=True)

    rec = {
        **c,
        "n": idx,
        "filename": final.name,
        "tweet": tweet,
        "measured_s": round(dur, 2),
        "purity": purity,
        "ocr": ocr_meta,
        "frame_texts": [r.get("texts") for r in reports],
        "bytes": final.stat().st_size,
        "manual": True,
        "model": MODEL,
    }
    with (META / "accepted.jsonl").open("a", encoding="utf-8") as f:
        f.write(json.dumps(rec, ensure_ascii=False) + "\n")
    print("  OK", final.name, flush=True)
    return "ok"


def main() -> None:
    done = set()
    acc_path = META / "accepted.jsonl"
    if acc_path.exists():
        for line in acc_path.read_text().splitlines():
            if line.strip():
                done.add(str(json.loads(line)["id"]))
    n = next_n()
    stats = {"ok": 0, "skip": 0, "fail": 0, "reject": 0}
    for c in CANDS:
        tid = str(c["id"])
        if tid in done:
            print(f"skip already accepted {tid}", flush=True)
            stats["skip"] += 1
            continue
        status = ingest_one(c, n)
        if status == "ok":
            stats["ok"] += 1
            n += 1
        else:
            stats[status] = stats.get(status, 0) + 1
    print("\nDONE", stats, flush=True)

    cand_path = META / "candidates.json"
    existing = json.loads(cand_path.read_text()) if cand_path.exists() else []
    have = {str(x.get("id")) for x in existing}
    added = 0
    for c in CANDS:
        if str(c["id"]) not in have:
            existing.append({**c, "model": MODEL, "manual": True})
            added += 1
    if added:
        cand_path.write_text(json.dumps(existing, ensure_ascii=False, indent=2), encoding="utf-8")
        print("candidates +", added, "now", len(existing), flush=True)


if __name__ == "__main__":
    main()
