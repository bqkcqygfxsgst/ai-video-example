#!/usr/bin/env python3
"""Ingest user-picked Seedance 2.5 posts (manual=True)."""
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path("/workspace/ai-videos-2026-09-14")
META = ROOT / "meta"
sys.path.insert(0, str(META))

import process as P  # noqa: E402

MODEL = "Seedance 2.5"

CANDS = [
    {
        "id": "2093897747263062523",
        "handle": "keshiAIart",
        "likes": 1970,
        "views": 124429,
        "followers": 69635,
        "date": "2026-08-30",
        "dur_ms": 47833,
        "video_url": "https://video.twimg.com/amplify_video/2093876204512366592/vid/avc1/2560x1440/ZhtqTSUVZ8UScVvV.mp4",
        "caption": "バトル seedance2.5",
        "sell": "武打对决",
        "evidence": "バトル seedance2.5",
    },
    {
        "id": "2097213270071586924",
        "handle": "Imagvio_AI",
        "likes": 22,
        "views": 14210,
        "followers": 88,
        "date": "2026-09-08",
        "dur_ms": 40279,
        "video_url": "https://video.twimg.com/amplify_video/2097213150995324929/vid/avc1/1920x1080/jvLSVOEL9L6eVgN4.mp4",
        "caption": "A cinematic ninja battle brought to life with Imagvio AI #seedance25",
        "sell": "忍者对决",
        "evidence": "cinematic ninja battle #ImagvioAI #seedance25",
    },
    {
        "id": "2092085807951831072",
        "handle": "keshiAIart",
        "likes": 1527,
        "views": 67561,
        "followers": 69635,
        "date": "2026-08-25",
        "dur_ms": 61416,
        "video_url": "https://video.twimg.com/amplify_video/2091902277758148608/vid/avc1/2560x1440/wrX3yMWUEq-PiNdp.mp4",
        "caption": "滑板 Seedance2.5",
        "sell": "滑板一镜",
        "evidence": "Seedance2.5",
    },
    {
        "id": "2095094811493851220",
        "handle": "SadiaMalik182",
        "likes": 274,
        "views": 2375,
        "followers": 10796,
        "date": "2026-09-02",
        "dur_ms": 29930,
        "video_url": "https://video.twimg.com/amplify_video/2095094241601183744/vid/avc1/1080x1920/z10hALLHvC8lt176.mp4",
        "caption": "Created with Seedance 2.5 on @wavespeed_ai",
        "sell": "云上莲花仙境",
        "evidence": "Created with Seedance 2.5 on @wavespeed_ai #Seedance2.5",
    },
    {
        "id": "2087388113496846692",
        "handle": "k_kaori_dododo",
        "likes": 16138,
        "views": 11379058,
        "followers": 3024,
        "date": "2026-08-12",
        "dur_ms": 60116,
        "video_url": "https://video.twimg.com/amplify_video/2087387997331447808/vid/avc1/1920x1080/S_kFbq2v1LSy3QP8.mp4",
        "caption": "うん、やべWWWWW 日本語喋らせたらやべW seedance2.5楽しい",
        "sell": "日语对白写实",
        "evidence": "seedance2.5楽しい",
    },
    {
        "id": "2099306588305867054",
        "handle": "AI_VideoLab",
        "likes": 6,
        "views": 1523,
        "followers": 525,
        "date": "2026-09-14",
        "dur_ms": 30144,
        "video_url": "https://video.twimg.com/amplify_video/2099306554600427520/vid/avc1/1920x1080/FA09VLSZe0ii0nIQ.mp4",
        "caption": "Seedance 2.5 is getting seriously good at animated storytelling.",
        "sell": "鹦鹉与海盗厨师",
        "evidence": "Seedance 2.5 is getting seriously good at animated storytelling. #Seedance25",
    },
    {
        "id": "2098414558113350133",
        "handle": "PUNPUNinuhime",
        "likes": 89,
        "views": 6951,
        "followers": 8869,
        "date": "2026-09-11",
        "dur_ms": 70401,
        "video_url": "https://video.twimg.com/amplify_video/2098414425988636672/vid/avc1/1872x1080/-h_WrGA7vZI8MLS-.mp4",
        "caption": "Created with seedance2.5（#CapCut）",
        "sell": "空中森林冒险",
        "evidence": "Created with seedance2.5（#CapCut） @capcutapp_jp",
    },
    {
        "id": "2098729585793720501",
        "handle": "NVTDanh",
        "likes": 65,
        "views": 2923,
        "followers": 5529,
        "date": "2026-09-12",
        "dur_ms": 30000,
        "video_url": "https://video.twimg.com/amplify_video/2098710689393287168/vid/avc1/3840x2160/Q_J-waipFY3k4mgg.mp4",
        "caption": "Created with Seedance2.5 on @higgsfield_ai #higgsfield",
        "sell": "GTA一镜闯关",
        "evidence": "Created with Seedance2.5 on @higgsfield_ai #higgsfield",
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
