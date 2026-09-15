#!/usr/bin/env python3
"""Ingest user-picked Kling 2.5 posts (manual=True)."""
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path("/workspace/ai-videos-2026-09-14")
META = ROOT / "meta"
sys.path.insert(0, str(META))

import process as P  # noqa: E402

MODEL = "Kling 2.5"

CANDS = [
    {
        "id": "2009936185389682857",
        "handle": "yori03617",
        "likes": 1825,
        "views": 69610,
        "followers": 18026,
        "date": "2026-01-10",
        "dur_ms": 10041,
        "video_url": "https://video.twimg.com/amplify_video/2009934186715721729/vid/avc1/1080x1080/RBiyoQCBl_IQgcQe.mp4",
        "caption": "#klingai Kling 2.5 Turbo 走らせてみました",
        "sell": "奔跑不摔倒",
        "evidence": "Kling 2.5 Turbo 走らせてみました",
    },
    {
        "id": "1985000508323774945",
        "handle": "maxescu",
        "likes": 467,
        "views": 51204,
        "followers": 38930,
        "date": "2025-11-02",
        "dur_ms": 10054,
        "video_url": "https://video.twimg.com/amplify_video/1984999062743961600/vid/avc1/1920x1080/l0I-1rn1-iwY1dvW.mp4",
        "caption": "This one is Kling 2.5, 1080p.",
        "sell": "攀岩POV",
        "evidence": "This one is Kling 2.5, 1080p.",
    },
    {
        "id": "1971583560252612817",
        "handle": "Framer_X",
        "likes": 827,
        "views": 69216,
        "followers": 49512,
        "date": "2025-09-26",
        "dur_ms": 9375,
        "video_url": "https://video.twimg.com/amplify_video/1971575319606792193/vid/avc1/1660x1250/VV56v1RJbXWZUmFC.mp4",
        "caption": "We've tested 500+ images for fast-paced animation with Kling 2.5",
        "sell": "快节奏合集",
        "evidence": "fast-paced animation with Kling 2.5 10 wild examples",
    },
    {
        "id": "1988354844290154502",
        "handle": "LudovicCreator",
        "likes": 761,
        "views": 54224,
        "followers": 38168,
        "date": "2025-11-11",
        "dur_ms": 10054,
        "video_url": "https://video.twimg.com/ext_tw_video/1988354803823431680/pu/vid/avc1/1280x720/BcAj7q6lZMHff1ex.mp4?tag=12",
        "caption": "KLING 2.5 desert wasteland scavenger Made in @Kling_ai",
        "sell": "废土拾荒",
        "evidence": "KLING 2.5 Made in @Kling_ai",
    },
    {
        "id": "1973326916510949632",
        "handle": "WuxiaRocks",
        "likes": 194,
        "views": 24908,
        "followers": 7809,
        "date": "2025-10-01",
        "dur_ms": 5085,
        "video_url": "https://video.twimg.com/amplify_video/1973326761913122816/vid/avc1/1920x1080/LSbqIQY9qgDIQbpQ.mp4",
        "caption": "Next physics test. Launching something. Kling 2.5 @ImagineArt_X",
        "sell": "抛射物理",
        "evidence": "Kling 2.5 @ImagineArt_X physics test",
    },
    {
        "id": "1988867769085931810",
        "handle": "umesh_ai",
        "likes": 262,
        "views": 17731,
        "followers": 47116,
        "date": "2025-11-13",
        "dur_ms": 5131,
        "video_url": "https://video.twimg.com/ext_tw_video/1988867691877388288/pu/vid/avc1/720x1080/4GWt8zGSCPlfvX--.mp4?tag=12",
        "caption": "Made with Kling 2.5 start and end frames. It is so much better than 2.1.",
        "sell": "猫咪入座",
        "evidence": "Made with Kling 2.5 start and end frames",
    },
    {
        "id": "1971104020245905754",
        "handle": "TechByMarkandey",
        "likes": 138,
        "views": 40557,
        "followers": 64972,
        "date": "2025-09-25",
        "dur_ms": 9166,
        "video_url": "https://video.twimg.com/amplify_video/1971103960707780608/vid/avc1/1260x720/jjxJ5iQ8Vj8uCRDN.mp4?tag=14",
        "caption": "Kling 2.5 delivers cinema-grade motion and emotion. Now live on Freepik",
        "sell": "影院级宣传",
        "evidence": "Kling 2.5 delivers cinema-grade motion Now live on Freepik",
    },
    {
        "id": "1970862178489278470",
        "handle": "javilopen",
        "likes": 434,
        "views": 45480,
        "followers": 128630,
        "date": "2025-09-24",
        "dur_ms": 5041,
        "video_url": "https://video.twimg.com/amplify_video/1970859563541827587/vid/avc1/1920x1080/eIPBgBJBOBr19pGl.mp4",
        "caption": "Testing Kling 2.5 Turbo inside Freepik Great for cinematic scenes",
        "sell": "飞船动作",
        "evidence": "Testing Kling 2.5 Turbo inside Freepik",
    },
    {
        "id": "1970480600676184249",
        "handle": "magnific",
        "likes": 487,
        "views": 182250,
        "followers": 89971,
        "date": "2025-09-23",
        "dur_ms": 16666,
        "video_url": "https://video.twimg.com/amplify_video/1970480542010474496/vid/avc1/1280x720/x6e_9f1BMAFVouU6.mp4?tag=14",
        "caption": "Introducing Kling 2.5 From cinematic realism to dramatic dynamism.",
        "sell": "官方发布片",
        "evidence": "Introducing Kling 2.5 Available now for all users",
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
