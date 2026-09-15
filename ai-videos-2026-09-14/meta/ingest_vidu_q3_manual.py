#!/usr/bin/env python3
"""Ingest user-picked Vidu Q3 posts (manual=True)."""
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path("/workspace/ai-videos-2026-09-14")
META = ROOT / "meta"
sys.path.insert(0, str(META))

import process as P  # noqa: E402

MODEL = "Vidu Q3"

CANDS = [
    {
        "id": "2056862394450915569",
        "handle": "chiha_20220301",
        "likes": 358,
        "views": 7293,
        "followers": 1502,
        "date": "2026-05-19",
        "dur_ms": 35433,
        "video_url": "https://video.twimg.com/amplify_video/2056862316961169409/vid/avc1/1080x1620/bn3l_8Wp3mKC8-it.mp4",
        "caption": "風景動画は元のイラストさえ出来ればViduQ3でサクッと安く作れます",
        "sell": "风景视频",
        "evidence": "ViduQ3でサクッと安く作れます #ViduCPP",
    },
    {
        "id": "2089836511508533274",
        "handle": "chiha_20220301",
        "likes": 95,
        "views": 1832,
        "followers": 1502,
        "date": "2026-08-18",
        "dur_ms": 35478,
        "video_url": "https://video.twimg.com/amplify_video/2089836347133673472/vid/avc1/1080x1620/Y4BmWLE1haBaX6ji.mp4",
        "caption": "今日の動画はViduQ3のフラッシュで生成【空の上のクリスタル城】",
        "sell": "空上水晶城",
        "evidence": "ViduQ3のフラッシュで生成 #ViduAI #ViduCPP",
    },
    {
        "id": "2017193582386663919",
        "handle": "genel_ai",
        "likes": 1108,
        "views": 177038,
        "followers": 28750,
        "date": "2026-01-30",
        "dur_ms": 14533,
        "video_url": "https://video.twimg.com/amplify_video/2017189742027403265/vid/avc1/1920x1080/xscgp3SrP68Liq48.mp4",
        "caption": "ViduQ3 で作るVlog風 編集なし、1枚の画像で",
        "sell": "Vlog风",
        "evidence": "ViduQ3 ( @ViduAI_official ) で作るVlog風",
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
