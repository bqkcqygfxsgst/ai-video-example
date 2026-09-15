#!/usr/bin/env python3
"""Ingest user-picked Kling 3.0 Omni posts (manual=True)."""
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path("/workspace/ai-videos-2026-09-14")
META = ROOT / "meta"
sys.path.insert(0, str(META))

import process as P  # noqa: E402

MODEL = "Kling 3.0 Omni"

CANDS = [
    {
        "id": "2098121124743967015",
        "handle": "magnific",
        "likes": 70,
        "views": 6545,
        "followers": 89971,
        "date": "2026-09-10",
        "dur_ms": 14948,
        "video_url": "https://video.twimg.com/amplify_video/2098121077998424064/vid/avc1/1920x1080/AZMtlW9fr9Ao4nV7.mp4?tag=16",
        "caption": "3 ways to create cinematic videos with Kling Kling 3.0 Omni visual direction",
        "sell": "三种成片对比",
        "evidence": "Kling 3.0 Omni, visual direction and cinematic continuity",
    },
    {
        "id": "2099628544653504669",
        "handle": "0xKarmi",
        "likes": 12,
        "views": 659,
        "followers": 689,
        "date": "2026-09-14",
        "dur_ms": 29566,
        "video_url": "https://video.twimg.com/amplify_video/2099628416685264897/vid/avc1/716x1274/HYO1D69I-J7A9sF8.mp4",
        "caption": "i opened Kling 3.0 Omni, typed a massive needle-shaped rock spire",
        "sell": "城市石针",
        "evidence": "i opened Kling 3.0 Omni, typed a massive needle-shaped rock spire",
    },
    {
        "id": "2097334981588926486",
        "handle": "browncatro1",
        "likes": 14,
        "views": 555,
        "followers": 6712,
        "date": "2026-09-08",
        "dur_ms": 15041,
        "video_url": "https://video.twimg.com/amplify_video/2097334883941318657/vid/avc1/1080x1920/bNTyGQ_PFCIn_SPp.mp4",
        "caption": "KlingのOmni reference動画にすることができました #klingai @Kling_ai",
        "sell": "波普舞蹈",
        "evidence": "KlingのOmni reference動画 #klingai @Kling_ai",
    },
    {
        "id": "2099465490704085047",
        "handle": "YaReYaRu30Life",
        "likes": 5,
        "views": 573,
        "followers": 5350,
        "date": "2026-09-14",
        "dur_ms": 15041,
        "video_url": "https://video.twimg.com/amplify_video/2099465460546994176/vid/avc1/1280x720/gZ7UhnTbLXWqtnYx.mp4",
        "caption": "Kling3.0 Omniに使用したらなんか事故った @Kling_ai #KlingECP",
        "sell": "游戏事故",
        "evidence": "Kling3.0 Omniに使用したら @Kling_ai #KlingECP",
    },
    {
        "id": "2098694327979692246",
        "handle": "uso800railway",
        "likes": 0,
        "views": 47,
        "followers": 129,
        "date": "2026-09-12",
        "dur_ms": 10041,
        "video_url": "https://video.twimg.com/amplify_video/2098692859251822592/vid/avc1/1280x720/kB0zTdTIxerxbgLL.mp4?tag=14",
        "caption": "Kling 3.0 Omni レクイエクタングラーは最初に影響出る傾向",
        "sell": "铁路场景",
        "evidence": "Kling 3.0 Omni 柱や梁が湾曲する傾向",
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
