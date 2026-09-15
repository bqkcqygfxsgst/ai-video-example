#!/usr/bin/env python3
"""Ingest user-picked MiniMax H3 posts (manual=True)."""
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path("/workspace/ai-videos-2026-09-14")
META = ROOT / "meta"
sys.path.insert(0, str(META))

import process as P  # noqa: E402

MODEL = "MiniMax H3"

CANDS = [
    {
        "id": "2090230978547703913",
        "handle": "Jessewelle",
        "likes": 5308,
        "views": 1138262,
        "followers": 897338,
        "date": "2026-08-20",
        "dur_ms": 15083,
        "video_url": "https://video.twimg.com/amplify_video/2090230875883786240/vid/avc1/1280x720/dbeUj4MuMgAB3YA-.mp4",
        "caption": "Minimax h3 is just way too good. Rendered this locally on my machine.",
        "sell": "本地渲染短片",
        "evidence": "Minimax h3 is just way too good. Rendered this locally",
    },
    {
        "id": "2087828526577705303",
        "handle": "aimikoda",
        "likes": 1219,
        "views": 187575,
        "followers": 29072,
        "date": "2026-08-13",
        "dur_ms": 15083,
        "video_url": "https://video.twimg.com/amplify_video/2087827783841890304/vid/avc1/2560x1440/0Of387mCCcFo36oh.mp4",
        "caption": "MiniMax H3 Character Introduction Template",
        "sell": "角色介绍模板",
        "evidence": "MiniMax H3 Character Introduction Template",
    },
    {
        "id": "2095807711371841623",
        "handle": "MauriceBourdon",
        "likes": 3058,
        "views": 219099,
        "followers": 1185,
        "date": "2026-09-04",
        "dur_ms": 126400,
        "video_url": "https://video.twimg.com/amplify_video/2095807269283704833/vid/avc1/1270x720/dS11mi14TITUMzVm.mp4",
        "caption": "Minimax H3 running locally. 100% Text-to-Video. 100% ComfyUI.",
        "sell": "本地循环长片",
        "evidence": "Minimax H3 running locally. 100% Text-to-Video.",
    },
    {
        "id": "2094427110764917030",
        "handle": "aimikoda",
        "likes": 211,
        "views": 21518,
        "followers": 29072,
        "date": "2026-08-31",
        "dur_ms": 15083,
        "video_url": "https://video.twimg.com/amplify_video/2094426256418697216/vid/avc1/1344x768/vaAvPDnwwKqPn8it.mp4",
        "caption": "MiniMax H3 - Tilt-Shift Burger Commerical - t2v",
        "sell": "微缩汉堡工地",
        "evidence": "MiniMax H3 - Tilt-Shift Burger Commerical - t2v",
    },
    {
        "id": "2097536639429964189",
        "handle": "hey_am_cherry",
        "likes": 98,
        "views": 8722,
        "followers": 4700,
        "date": "2026-09-09",
        "dur_ms": 15115,
        "video_url": "https://video.twimg.com/amplify_video/2097536583750848512/vid/avc1/1440x1920/JAUweRXMruYuneGh.mp4",
        "caption": "Made this little scene in MiniMax H3 @Hailuo_AI",
        "sell": "胶片感拾物",
        "evidence": "Made this little scene in MiniMax H3 @Hailuo_AI",
    },
    {
        "id": "2082747126497300930",
        "handle": "itxabdullaa",
        "likes": 129,
        "views": 5918,
        "followers": 7273,
        "date": "2026-07-30",
        "dur_ms": 15083,
        "video_url": "https://video.twimg.com/amplify_video/2082747028283719680/vid/avc1/2560x1440/K10AxLHebBI2ZcxJ.mp4",
        "caption": "Made with MiniMax H3 on @Hailuo_AI #MiniMaxH3 Seoul Summer 1998",
        "sell": "1998首尔雨中公交",
        "evidence": "Made with MiniMax H3 on @Hailuo_AI #MiniMaxH3",
    },
    {
        "id": "2099132723143245957",
        "handle": "ai_lifehack55",
        "likes": 128,
        "views": 4063,
        "followers": 2749,
        "date": "2026-09-13",
        "dur_ms": 46958,
        "video_url": "https://video.twimg.com/amplify_video/2099132307747880960/vid/avc1/1440x1440/Rmj2PWV8qfGqdS_0.mp4",
        "caption": "MiniMax H3 ＆ MidjouneyV8.2 SJinn MiniMax H3（動画生成）",
        "sell": "公牛与我舞蹈",
        "evidence": "SJinn MiniMax H3（動画生成） MiniMax H3 ＆ MidjouneyV8.2",
    },
    {
        "id": "2098984611980493291",
        "handle": "CaliraVal",
        "likes": 154,
        "views": 10410,
        "followers": 9947,
        "date": "2026-09-13",
        "dur_ms": 15084,
        "video_url": "https://video.twimg.com/amplify_video/2098979051570688000/vid/avc1/1920x1440/TlE_gztU3cSnAL-C.mp4",
        "caption": "Created with MiniMax H3.",
        "sell": "夏日金鱼街景",
        "evidence": "Created with MiniMax H3.",
    },
    {
        "id": "2097997942783410513",
        "handle": "ai_uncovered",
        "likes": 33,
        "views": 14761,
        "followers": 25541,
        "date": "2026-09-10",
        "dur_ms": 11656,
        "video_url": "https://video.twimg.com/amplify_video/2097996575901704192/vid/avc1/1440x2560/qLFqY9LyvKhcjwmP.mp4",
        "caption": "So I tested MiniMax H3 on @itsPolloAI A dog drops an ice cream",
        "sell": "狗掉冰淇淋",
        "evidence": "tested MiniMax H3 on @itsPolloAI",
    },
    {
        "id": "2098452592074322074",
        "handle": "ashen_one",
        "likes": 188,
        "views": 23884,
        "followers": 55296,
        "date": "2026-09-11",
        "dur_ms": 15104,
        "video_url": "https://video.twimg.com/amplify_video/2098452200758398979/vid/avc1/1344x768/eMYFaKacJ1VU75RE.mp4",
        "caption": "MINIMAX H3 VIDEO GENERATION IS ABSURDLY POWERFUL. Attack on Titan",
        "sell": "进击的巨人风",
        "evidence": "MINIMAX H3 VIDEO GENERATION I generated this 15-second animation of Attack on Titan",
    },
    {
        "id": "2098678102222323820",
        "handle": "SD_Tutorial",
        "likes": 311,
        "views": 15537,
        "followers": 11085,
        "date": "2026-09-12",
        "dur_ms": 16916,
        "video_url": "https://video.twimg.com/amplify_video/2098678007393333248/vid/avc1/800x506/BAjVxuBDwjgOedt-.mp4?tag=14",
        "caption": "Minimax H3 VFX Camera control Visual camera planner for MiniMax H3 inside ComfyUI.",
        "sell": "镜头轨迹演示",
        "evidence": "Visual camera planner for MiniMax H3 inside ComfyUI",
    },
    {
        "id": "2097502327519232447",
        "handle": "plasm0",
        "likes": 33,
        "views": 2437,
        "followers": 6986,
        "date": "2026-09-09",
        "dur_ms": 10104,
        "video_url": "https://video.twimg.com/amplify_video/2097502001772851200/vid/avc1/2112x1216/Cr1TaKOc2kLQOVKk.mp4",
        "caption": "testing local Minimax H3 Singularity Model",
        "sell": "本地奇点测试",
        "evidence": "testing local Minimax H3 Singularity Model",
    },
    {
        "id": "2094282576542470337",
        "handle": "ponyodong",
        "likes": 235,
        "views": 23416,
        "followers": 14894,
        "date": "2026-08-31",
        "dur_ms": 15084,
        "video_url": "https://video.twimg.com/amplify_video/2094281712717144065/vid/avc1/2560x1440/JnrhFnhLPbLreKeS.mp4",
        "caption": "把你喜欢的人物资产图和场景图放到 MiniMax H3 里即可",
        "sell": "复古拼贴MV",
        "evidence": "丢进 MiniMax H3 动漫角色风格的15 秒复古潮流拼贴 MV",
    },
    {
        "id": "2099244467630878842",
        "handle": "amadeus_NFT",
        "likes": 12,
        "views": 507,
        "followers": 89,
        "date": "2026-09-13",
        "dur_ms": 15083,
        "video_url": "https://video.twimg.com/amplify_video/2099243333206020096/vid/avc1/1080x1936/gnrtT0v2QixLcxcD.mp4",
        "caption": "I generated this high-speed fly-through using MiniMax H3",
        "sell": "建筑自组装",
        "evidence": "generated this high-speed fly-through using MiniMax H3",
    },
    {
        "id": "2097626398320119822",
        "handle": "AlexM12jx",
        "likes": 87,
        "views": 31120,
        "followers": 60964,
        "date": "2026-09-09",
        "dur_ms": 15083,
        "video_url": "https://video.twimg.com/amplify_video/2097626358436536320/vid/avc1/768x1344/hDjCBD6ijG1xlD4i.mp4",
        "caption": "Made this one using MiniMax H3 Max on @itsPolloAI",
        "sell": "竖屏样片",
        "evidence": "using MiniMax H3 Max on @itsPolloAI",
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
