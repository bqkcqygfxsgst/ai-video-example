#!/usr/bin/env python3
"""Ingest user-picked Kling 2.1 posts (manual=True)."""
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path("/workspace/ai-videos-2026-09-14")
META = ROOT / "meta"
sys.path.insert(0, str(META))

import process as P  # noqa: E402

MODEL = "Kling 2.1"

CANDS = [
    {
        "id": "1932833690003914817",
        "handle": "MayorKingAI",
        "likes": 876,
        "views": 76025,
        "followers": 36152,
        "date": "2025-06-11",
        "dur_ms": 10041,
        "video_url": "https://video.twimg.com/amplify_video/1932831823974842368/vid/avc1/1920x1080/V3pQOHMt0C5SkpwT.mp4",
        "caption": "Rear tracking shot, text-to-video, and AI-generated sound with Kling 2.1. Master",
        "sell": "后跟黑猫街市",
        "evidence": "Kling 2.1. Master Made in @Kling_ai",
    },
    {
        "id": "1926037824953897337",
        "handle": "StevieMac03",
        "likes": 214,
        "views": 11706,
        "followers": 15836,
        "date": "2025-05-23",
        "dur_ms": 21250,
        "video_url": "https://video.twimg.com/amplify_video/1926037471881535488/vid/avc1/1928x1080/6vs71_auw9Enw2sj.mp4",
        "caption": "Kling 2.1 is coming, now with 1080p outputs. Created in @kling 2.1 Master.",
        "sell": "抢先测试",
        "evidence": "Created in @kling 2.1 Master",
    },
    {
        "id": "1927126460352893348",
        "handle": "MayorKingAI",
        "likes": 477,
        "views": 53311,
        "followers": 36152,
        "date": "2025-05-26",
        "dur_ms": 44118,
        "video_url": "https://video.twimg.com/amplify_video/1927126369021878272/vid/avc1/720x1286/igQubqmN4rK901iv.mp4?tag=14",
        "caption": "Kling 2.1. Image to Video Prompt Collection Video: Kling 2.1",
        "sell": "提示词合集",
        "evidence": "Kling 2.1. Image to Video Prompt Collection Video: Kling 2.1",
    },
    {
        "id": "1927953037185765400",
        "handle": "hq4ai",
        "likes": 270,
        "views": 55181,
        "followers": 37062,
        "date": "2025-05-29",
        "dur_ms": 86029,
        "video_url": "https://video.twimg.com/amplify_video/1927952948132466688/vid/avc1/1280x720/UauPCnqZ7fEaXdIt.mp4",
        "caption": "Kling 2.1 is here! this is our promotional video for it.",
        "sell": "宣传片",
        "evidence": "Kling 2.1 is here! promotional video currently the pinnacle of I2V",
    },
    {
        "id": "1958897667096158339",
        "handle": "AleRVG",
        "likes": 1006,
        "views": 51338,
        "followers": 17694,
        "date": "2025-08-22",
        "dur_ms": 8733,
        "video_url": "https://video.twimg.com/amplify_video/1958896055270957058/vid/avc1/1080x1080/f9D6bVFgMs9tO-Dg.mp4",
        "caption": "KLING 2.1 launches Start & End Frames metamorphosis",
        "sell": "首尾帧变形",
        "evidence": "KLING 2.1 launches Start & End Frames",
    },
    {
        "id": "1926659598896750682",
        "handle": "towya_aillust",
        "likes": 174,
        "views": 15615,
        "followers": 15557,
        "date": "2025-05-25",
        "dur_ms": 25216,
        "video_url": "https://video.twimg.com/amplify_video/1926659374837080064/vid/avc1/1280x720/i0dpPWHoEbIgP3EE.mp4",
        "caption": "KLING 2.1 Early Access Standardで作っています",
        "sell": "Standard试作",
        "evidence": "KLING 2.1 Early Access @Kling_ai Standard",
    },
    {
        "id": "1968283810073899289",
        "handle": "jerrod_lew",
        "likes": 218,
        "views": 13201,
        "followers": 19391,
        "date": "2025-09-17",
        "dur_ms": 15116,
        "video_url": "https://video.twimg.com/amplify_video/1967208215139020800/vid/avc1/1920x1080/TPa4KJAMSPbuhekr.mp4",
        "caption": "Seedance 4K with Kling 2.1 and 60FPS video upscaler. Kling 2.1 start/end frames",
        "sell": "角色一致剪辑",
        "evidence": "Kling 2.1 start/end frames were used to stitch the clips together",
    },
    {
        "id": "1928902234718249389",
        "handle": "HBCoop_",
        "likes": 284,
        "views": 11973,
        "followers": 54747,
        "date": "2025-05-31",
        "dur_ms": 10041,
        "video_url": "https://video.twimg.com/ext_tw_video/1928902204095672321/pu/vid/avc1/720x1286/51wQvm4N-o0lusJo.mp4?tag=12",
        "caption": "Midjourney -> Kling 2.1 pro",
        "sell": "花瓣人像",
        "evidence": "Midjourney -> Kling 2.1 pro",
    },
    {
        "id": "1926625183550284126",
        "handle": "WuxiaRocks",
        "likes": 65,
        "views": 3857,
        "followers": 7809,
        "date": "2025-05-25",
        "dur_ms": 5041,
        "video_url": "https://video.twimg.com/amplify_video/1926624424586891264/vid/avc1/1948x1060/rmdXrN_I-S2dLlOm.mp4",
        "caption": "Testing out Kling 2.1 Pro with I2V Imagen 4 + Kling 2.1 Pro",
        "sell": "I2V细节",
        "evidence": "Testing out Kling 2.1 Pro with I2V Imagen 4 + Kling 2.1 Pro",
    },
    {
        "id": "1926092625905320264",
        "handle": "mxvdxn",
        "likes": 528,
        "views": 38880,
        "followers": 23970,
        "date": "2025-05-24",
        "dur_ms": 22778,
        "video_url": "https://video.twimg.com/amplify_video/1926087581780893696/vid/avc1/1928x1080/64TtYAgn8QBUbvXB.mp4",
        "caption": "Got early access to test @Kling_ai 2.1 KLING 2.1 Professional Mode",
        "sell": "Professional试作",
        "evidence": "early access to test @Kling_ai 2.1 Professional Mode",
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
