#!/usr/bin/env python3
"""Ingest user-picked Kling 3.0 posts (manual=True)."""
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path("/workspace/ai-videos-2026-09-14")
META = ROOT / "meta"
sys.path.insert(0, str(META))

import process as P  # noqa: E402

MODEL = "Kling 3.0"

CANDS = [
    {
        "id": "2097543568886026569",
        "handle": "liluocheng13",
        "likes": 56,
        "views": 1445,
        "followers": 3191,
        "date": "2026-09-09",
        "dur_ms": 15042,
        "video_url": "https://video.twimg.com/amplify_video/2097543336773193728/vid/avc1/720x1280/_2Zu08MgrN_ttnyd.mp4",
        "caption": "Image: ChatGPT Video: Kling 3.0",
        "sell": "唐卡转视频",
        "evidence": "Video: Kling 3.0",
    },
    {
        "id": "2097655880053658032",
        "handle": "liluocheng13",
        "likes": 59,
        "views": 1156,
        "followers": 3191,
        "date": "2026-09-09",
        "dur_ms": 15042,
        "video_url": "https://video.twimg.com/amplify_video/2097655794426884096/vid/avc1/716x1280/vHRElBmqR5Ctl9Cb.mp4",
        "caption": "Midjourney + Kling 3.0",
        "sell": "仰望构图",
        "evidence": "Midjourney + Kling 3.0",
    },
    {
        "id": "2019072637192843463",
        "handle": "PJaccetturo",
        "likes": 17771,
        "views": 4399264,
        "followers": 157848,
        "date": "2026-02-04",
        "dur_ms": 89958,
        "video_url": "https://video.twimg.com/amplify_video/2019065570076090368/vid/avc1/1714x720/50Khs8uuzOIOWI4O.mp4",
        "caption": "AI is now 100% photorealistic with the launch of Kling 3.0 The Way of Kings",
        "sell": "王者之路开场",
        "evidence": "launch of Kling 3.0 Multi-Shot technique",
    },
    {
        "id": "2095122944137773503",
        "handle": "ojiji2025",
        "likes": 349,
        "views": 5636,
        "followers": 5336,
        "date": "2026-09-02",
        "dur_ms": 15041,
        "video_url": "https://video.twimg.com/amplify_video/2095122880120197120/vid/avc1/1440x1440/g7TEqjvVWDpbqhim.mp4",
        "caption": "Winter Is Coming Midjourney Kling 3.0 from @Kling_ai",
        "sell": "寒冬来临",
        "evidence": "Kling 3.0 from @Kling_ai",
    },
    {
        "id": "2093104528438784135",
        "handle": "ojiji2025",
        "likes": 675,
        "views": 12542,
        "followers": 5336,
        "date": "2026-08-27",
        "dur_ms": 15041,
        "video_url": "https://video.twimg.com/amplify_video/2093104402118893568/vid/avc1/1440x1440/affV-JVlcX5QQY1I.mp4",
        "caption": "a spaceship leaves an outpost Made with Midjourney and Kling 3.0",
        "sell": "飞船离港",
        "evidence": "Made with Midjourney and Kling 3.0",
    },
    {
        "id": "2094763152701591715",
        "handle": "ojiji2025",
        "likes": 513,
        "views": 8175,
        "followers": 5336,
        "date": "2026-09-01",
        "dur_ms": 15041,
        "video_url": "https://video.twimg.com/amplify_video/2094763063287431168/vid/avc1/1440x1440/iE5QxQUpBEvhug40.mp4",
        "caption": "Flying through the maze Made with Midjourney and Kling 3.0",
        "sell": "迷宫穿行",
        "evidence": "Made with Midjourney and Kling 3.0",
    },
    {
        "id": "2019304424297177558",
        "handle": "higgsfield_ai",
        "likes": 557,
        "views": 34533,
        "followers": 230516,
        "date": "2026-02-05",
        "dur_ms": 6506,
        "video_url": "https://video.twimg.com/amplify_video/2019304367200092161/vid/avc1/1286x720/ec7RoBf4wbDADeau.mp4?tag=14",
        "caption": "KLING 3.0 gives you PRO-GRADE camera movement Powered by Kling 3.0",
        "sell": "锁定跟踪",
        "evidence": "KLING 3.0 PRO-GRADE camera movement Powered by Kling 3.0",
    },
    {
        "id": "2099138203026599964",
        "handle": "im_shahid7",
        "likes": 64,
        "views": 2795,
        "followers": 5315,
        "date": "2026-09-13",
        "dur_ms": 15041,
        "video_url": "https://video.twimg.com/amplify_video/2099138035061555201/vid/avc1/3806x2160/juolIt7jFbeLkcew.mp4",
        "caption": "The walk towards serenity Made with Kling 3.0 on @Kling_ai",
        "sell": "林中漫步",
        "evidence": "Made with Kling 3.0 on @Kling_ai",
    },
    {
        "id": "2088600912231268580",
        "handle": "ojiji2025",
        "likes": 224,
        "views": 3922,
        "followers": 5336,
        "date": "2026-08-15",
        "dur_ms": 15041,
        "video_url": "https://video.twimg.com/amplify_video/2088600734816448512/vid/avc1/1440x1440/xcQuFAp7yFT9HHuU.mp4",
        "caption": "Slow and steady wins the race Made with Midjourney and Kling 3.0",
        "sell": "乌龟竞走",
        "evidence": "Made with Midjourney and Kling 3.0",
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
