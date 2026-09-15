#!/usr/bin/env python3
"""Ingest user-picked Kling O1 posts (manual=True)."""
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path("/workspace/ai-videos-2026-09-14")
META = ROOT / "meta"
sys.path.insert(0, str(META))

import process as P  # noqa: E402

MODEL = "Kling O1"

CANDS = [
    {
        "id": "2009022900628787688",
        "handle": "shikoba_86",
        "likes": 182,
        "views": 10560,
        "followers": 6942,
        "date": "2026-01-07",
        "dur_ms": 5041,
        "video_url": "https://video.twimg.com/amplify_video/2009022465465344000/vid/avc1/1920x1080/B2tdkuDGsH3zf2dn.mp4",
        "caption": "Kling O1 / 2.6 Tip - Cinematic Horror with Audio (Jump Scare Scenes)",
        "sell": "惊悚跳吓",
        "evidence": "Kling O1 / 2.6 Tip Cinematic Horror with Audio",
    },
    {
        "id": "2003736707661987927",
        "handle": "0xInk_",
        "likes": 276,
        "views": 13928,
        "followers": 204215,
        "date": "2025-12-24",
        "dur_ms": 10016,
        "video_url": "https://video.twimg.com/amplify_video/2003735674802081792/vid/avc1/3840x2160/pa1Re2ANeDTpKT_E.mp4",
        "caption": "can't stop playing with Kling O1 the camera movements are insanely good",
        "sell": "运镜狂玩",
        "evidence": "can't stop playing with Kling O1 the camera movements are insanely good",
    },
    {
        "id": "1995568523222085776",
        "handle": "MayorKingAI",
        "likes": 364,
        "views": 36706,
        "followers": 36152,
        "date": "2025-12-01",
        "dur_ms": 3100,
        "video_url": "https://video.twimg.com/amplify_video/1995568463574908928/vid/avc1/1280x720/-z0eSF-NLS3npTgi.mp4?tag=14",
        "caption": "Kling just dropped o1. Invideo just turned it into a full VFX house.",
        "sell": "o1发布",
        "evidence": "Kling just dropped o1 Invideo VFX house",
    },
    {
        "id": "1996919687603691699",
        "handle": "manishkumar_dev",
        "likes": 85,
        "views": 25455,
        "followers": 53549,
        "date": "2025-12-05",
        "dur_ms": 5041,
        "video_url": "https://video.twimg.com/amplify_video/1996919631588872193/vid/avc1/1280x720/12YAzDB6ApMWuKEy.mp4?tag=14",
        "caption": "I just tried the new AI video model Kling O1",
        "sell": "多模态试用",
        "evidence": "tried the new AI video model Kling O1",
    },
    {
        "id": "1995935038953959829",
        "handle": "invideoOfficial",
        "likes": 280,
        "views": 848194,
        "followers": 36183,
        "date": "2025-12-02",
        "dur_ms": 31708,
        "video_url": "https://video.twimg.com/amplify_video/1995934937699254272/vid/avc1/1920x1080/__rFDneN8P6cpA8d.mp4",
        "caption": "Kling o1 is FREE and UNLIMITED on invideo till Dec 8. VFX House",
        "sell": "VFX House",
        "evidence": "Kling o1 is FREE and UNLIMITED on invideo VFX House",
    },
    {
        "id": "1996467070737990125",
        "handle": "TechByMarkandey",
        "likes": 66,
        "views": 32890,
        "followers": 64972,
        "date": "2025-12-04",
        "dur_ms": 5041,
        "video_url": "https://video.twimg.com/amplify_video/1996467017885663232/vid/avc1/1280x720/cfLd3t7XY25gVo5h.mp4?tag=14",
        "caption": "I just tested the new AI tool Kling O1 for video creation. Freepik",
        "sell": "发型改造",
        "evidence": "tested the new AI tool Kling O1 Freepik has now integrated Kling O1",
    },
    {
        "id": "1995568661919400215",
        "handle": "invideoOfficial",
        "likes": 130,
        "views": 261839,
        "followers": 36183,
        "date": "2025-12-01",
        "dur_ms": 3133,
        "video_url": "https://video.twimg.com/amplify_video/1995568602230259712/vid/avc1/1280x720/3fkf7NAvxGIMoMeD.mp4?tag=14",
        "caption": "VFX House a full VFX studio built on Kling o1 inside invideo.",
        "sell": "虚拟场景",
        "evidence": "VFX House built on Kling o1 inside invideo",
    },
    {
        "id": "2018273084076122135",
        "handle": "churvikv",
        "likes": 108,
        "views": 4509,
        "followers": 7140,
        "date": "2026-02-02",
        "dur_ms": 8289,
        "video_url": "https://video.twimg.com/amplify_video/2018272550384435201/vid/avc1/720x1280/BOY0etlrknu0qerm.mp4",
        "caption": "Today I tested the model: Kling O1 image in video and video in video",
        "sell": "图生视频",
        "evidence": "tested the model: Kling O1 image in video and video in video",
    },
    {
        "id": "1997672465267577183",
        "handle": "ai_for_success",
        "likes": 392,
        "views": 45012,
        "followers": 81413,
        "date": "2025-12-07",
        "dur_ms": 5154,
        "video_url": "https://video.twimg.com/ext_tw_video/1997672430127775744/pu/vid/avc1/1920x1080/7aC92omA8YFsQ7cO.mp4",
        "caption": "MESSI Nano Banana Pro plus Kling O1 Start Frame and End Frame",
        "sell": "梅西3D屏",
        "evidence": "Nano Banana Pro plus Kling O1 Start Frame and End Frame",
    },
    {
        "id": "1996235306652287297",
        "handle": "invideoOfficial",
        "likes": 193,
        "views": 277578,
        "followers": 36183,
        "date": "2025-12-03",
        "dur_ms": 37333,
        "video_url": "https://video.twimg.com/amplify_video/1996235097926967296/vid/avc1/1930x1080/69km384Hcr5nCts6.mp4",
        "caption": "all new Kling models including Kling 2.6 and Kling o1 unlimited on invideo",
        "sell": "原生音频",
        "evidence": "Kling 2.6 and Kling o1 (image + video) UNLIMITED on invideo",
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
