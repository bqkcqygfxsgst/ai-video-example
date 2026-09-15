#!/usr/bin/env python3
"""Auto-ingest a filtered high-quality batch (duration + OCR enforced)."""
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path("/workspace/ai-videos-2026-09-14")
META = ROOT / "meta"
sys.path.insert(0, str(META))

import process as P  # noqa: E402

CANDS = [
    {
        "id": "2099588162209108245",
        "handle": "KeorUnreal",
        "model": "Kling 3.0",
        "likes": 1518,
        "views": 23167,
        "followers": 42712,
        "date": "2026-09-14",
        "dur_ms": 12041,
        "video_url": "https://video.twimg.com/amplify_video/2099588066419621888/vid/avc1/1076x1928/aTEY5ByQ778-CeMc.mp4",
        "caption": "It's better not to make her angry. Kling 3.0 via Higgsfield AI",
        "sell": "蜘蛛女夜巡",
        "evidence": "Kling 3.0 via Higgsfield AI",
    },
    {
        "id": "2093467081891319936",
        "handle": "ojiji2025",
        "model": "Kling 3.0",
        "likes": 965,
        "views": 27654,
        "followers": 5338,
        "date": "2026-08-28",
        "dur_ms": 15041,
        "video_url": "https://video.twimg.com/amplify_video/2093466951683305472/vid/avc1/1440x1440/AmyJvbad2schs8FT.mp4",
        "caption": "Flying in formation Made with Midjourney and Kling 3.0",
        "sell": "机甲编队飞行",
        "evidence": "Made with Midjourney and Kling 3.0",
    },
    {
        "id": "2092015419167310260",
        "handle": "ojiji2025",
        "model": "Kling 3.0",
        "likes": 643,
        "views": 12669,
        "followers": 5338,
        "date": "2026-08-24",
        "dur_ms": 15041,
        "video_url": "https://video.twimg.com/amplify_video/2092015357041225728/vid/avc1/1440x1440/6fuQauZpTXr95lpa.mp4",
        "caption": "Somebody's enjoying the future Made with Midjourney and Kling 3.0",
        "sell": "未来城市兜风",
        "evidence": "Made with Midjourney and Kling 3.0",
    },
    {
        "id": "2091486492598427777",
        "handle": "ojiji2025",
        "model": "Kling 3.0",
        "likes": 665,
        "views": 12754,
        "followers": 5338,
        "date": "2026-08-23",
        "dur_ms": 15041,
        "video_url": "https://video.twimg.com/amplify_video/2091486420607328256/vid/avc1/1440x1440/7jQW4nLJa7zfPZUQ.mp4",
        "caption": "Footage of a mecha rampage Made with Midjourney and Kling 3.0",
        "sell": "机甲城市暴走",
        "evidence": "Made with Midjourney and Kling 3.0",
    },
    {
        "id": "2089322005913100339",
        "handle": "ojiji2025",
        "model": "Kling 3.0",
        "likes": 625,
        "views": 20459,
        "followers": 5338,
        "date": "2026-08-17",
        "dur_ms": 15041,
        "video_url": "https://video.twimg.com/amplify_video/2089321814824787968/vid/avc1/1440x1440/GB_t4IJLS8IJtI9F.mp4",
        "caption": "Testing out the new mecha Made with Midjourney and Kling 3.0",
        "sell": "新机甲试驾",
        "evidence": "Made with Midjourney and Kling 3.0",
    },
    {
        "id": "2076637773214486759",
        "handle": "Kling_ai",
        "model": "Kling 3.0",
        "likes": 729,
        "views": 549880,
        "followers": 134835,
        "date": "2026-07-13",
        "dur_ms": 15133,
        "video_url": "https://video.twimg.com/amplify_video/2076601278353035264/vid/avc1/1920x1080/k5dLeXr6OjqqHHwg.mp4",
        "caption": "Cat by day. Boxer by night.",
        "sell": "猫拳击手",
        "evidence": "official @Kling_ai",
    },
    {
        "id": "2080080455756591396",
        "handle": "Kling_ai",
        "model": "Kling 3.0",
        "likes": 217,
        "views": 163935,
        "followers": 134835,
        "date": "2026-07-23",
        "dur_ms": 12817,
        "video_url": "https://video.twimg.com/amplify_video/2079920884350095360/vid/avc1/1080x1920/Xn0lUPXnxZkK_caP.mp4",
        "caption": "POV: The Massive Disaster Was Filmed Here",
        "sell": "灾难现场POV",
        "evidence": "official @Kling_ai",
    },
    {
        "id": "2082775431653240923",
        "handle": "0xbisc",
        "model": "Seedance 2.0",
        "likes": 1309,
        "views": 70530,
        "followers": 15823,
        "date": "2026-07-30",
        "dur_ms": 13766,
        "video_url": "https://video.twimg.com/amplify_video/2082775222047084544/vid/avc1/1080x1080/nEK-qG8dQT8ja-5N.mp4",
        "caption": "never step on a fish made with Seedance 2 #DreaminaCPP",
        "sell": "别踩那条鱼",
        "evidence": "made with Seedance 2 #DreaminaCPP @dreamina_ai",
    },
    {
        "id": "2081336600588611738",
        "handle": "0xbisc",
        "model": "Seedance 2.0",
        "likes": 1510,
        "views": 63250,
        "followers": 15823,
        "date": "2026-07-26",
        "dur_ms": 15033,
        "video_url": "https://video.twimg.com/amplify_video/2081336238704074752/vid/avc1/1080x1080/8yT7sCO9uIZ8KSYH.mp4",
        "caption": "kinda bored, just messing around with a pen made with Seedance 2",
        "sell": "玩笔特写",
        "evidence": "made with Seedance 2 on @openart_ai",
    },
    {
        "id": "2096236118442398127",
        "handle": "SadiaMalik182",
        "model": "Seedance 2.5",
        "likes": 1099,
        "views": 79412,
        "followers": 10796,
        "date": "2026-09-05",
        "dur_ms": 29472,
        "video_url": "https://video.twimg.com/amplify_video/2096235764891963392/vid/avc1/720x1280/qO2EYNxrzBP1Ez9V.mp4",
        "caption": "A little seaside escape created with Seedance 2 5 on @nemovideoai",
        "sell": "海边咖啡馆vlog",
        "evidence": "created with Seedance 2 5 on @nemovideoai #Seedance25",
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


def main() -> None:
    done = set()
    acc_path = META / "accepted.jsonl"
    if acc_path.exists():
        for line in acc_path.read_text().splitlines():
            if line.strip():
                done.add(str(json.loads(line)["id"]))
    skip_path = META / "skip_ids.json"
    if skip_path.exists():
        done.update(str(x) for x in json.loads(skip_path.read_text()))

    n = next_n()
    results, rejects, fails = [], [], []
    stats = {"ok": 0, "skip": 0}
    for c in CANDS:
        tid = str(c["id"])
        if tid in done:
            print(f"skip already {tid}", flush=True)
            stats["skip"] += 1
            continue
        before = len(results)
        P.process_one(c, n, results, rejects, fails)
        if len(results) > before:
            stats["ok"] += 1
            n += 1
    print("\nDONE", stats, "rejects", len(rejects), "fails", len(fails), flush=True)
    for r in rejects:
        print("  REJECT", r.get("id"), r.get("reason"), flush=True)
    for r in fails:
        print("  FAIL", r.get("id"), r.get("reason"), flush=True)

    rej_path = META / "rejects.json"
    prev = []
    if rej_path.exists():
        try:
            prev = json.loads(rej_path.read_text() or "[]") or []
        except Exception:
            prev = []
    if rejects:
        prev.extend(rejects)
        rej_path.write_text(json.dumps(prev, ensure_ascii=False, indent=2), encoding="utf-8")

    cand_path = META / "candidates.json"
    existing = json.loads(cand_path.read_text()) if cand_path.exists() else []
    have = {str(x.get("id")) for x in existing}
    added = 0
    for c in CANDS:
        if str(c["id"]) not in have:
            existing.append(c)
            added += 1
    if added:
        cand_path.write_text(json.dumps(existing, ensure_ascii=False, indent=2), encoding="utf-8")
        print("candidates +", added, "now", len(existing), flush=True)


if __name__ == "__main__":
    main()
