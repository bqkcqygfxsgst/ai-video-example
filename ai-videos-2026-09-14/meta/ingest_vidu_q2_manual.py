#!/usr/bin/env python3
"""Ingest user-picked Vidu Q2 posts (manual=True)."""
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path("/workspace/ai-videos-2026-09-14")
META = ROOT / "meta"
sys.path.insert(0, str(META))

import process as P  # noqa: E402

MODEL = "Vidu Q2"

CANDS = [
    {
        "id": "1972619362738852281",
        "handle": "genel_ai",
        "likes": 989,
        "views": 58670,
        "followers": 28750,
        "date": "2025-09-29",
        "dur_ms": 11066,
        "video_url": "https://video.twimg.com/amplify_video/1972614091660578816/vid/avc1/1920x1080/VKNtWDvZmy5I-20n.mp4",
        "caption": "Vidu Q2 Cinematic 印象派風の柔らかいタッチ",
        "sell": "印象派风动画",
        "evidence": "Vidu Q2 Cinematic この動きはViduでしか出ませんでした",
    },
    {
        "id": "1980642488785465349",
        "handle": "toyxyz3",
        "likes": 211,
        "views": 12560,
        "followers": 31914,
        "date": "2025-10-21",
        "dur_ms": 5041,
        "video_url": "https://video.twimg.com/amplify_video/1980642316659380224/vid/avc1/1920x1080/a8MJOjdN6dEtLBCS.mp4",
        "caption": "Vidu Q2 ref to video test #ViduQ2",
        "sell": "参考转动图",
        "evidence": "Vidu Q2 ref to video test #ViduQ2",
    },
    {
        "id": "1980946719102955592",
        "handle": "hq4ai",
        "likes": 200,
        "views": 28892,
        "followers": 37062,
        "date": "2025-10-22",
        "dur_ms": 88050,
        "video_url": "https://video.twimg.com/amplify_video/1980933460718968832/vid/avc1/720x972/_YuYETzSAjDdu5Yc.mp4",
        "caption": "Vidu AI Q2 Reference-to-Video Joker rap",
        "sell": "小丑说唱",
        "evidence": 'Vidu AI "Q2 Reference-to-Video" is the best among similar Models',
    },
    {
        "id": "1971567991495242070",
        "handle": "KanaWorks_AI",
        "likes": 136,
        "views": 4247,
        "followers": 8810,
        "date": "2025-09-26",
        "dur_ms": 19086,
        "video_url": "https://video.twimg.com/amplify_video/1971567027237388288/vid/avc1/1890x1080/AFvTztLELr-ePYsi.mp4",
        "caption": "The Little Knight made with vidu Q2 @ViduAI_official",
        "sell": "小骑士",
        "evidence": "made with vidu Q2 @ViduAI_official #viduq2",
    },
    {
        "id": "1980615840677654800",
        "handle": "umesh_ai",
        "likes": 218,
        "views": 12399,
        "followers": 47116,
        "date": "2025-10-21",
        "dur_ms": 8083,
        "video_url": "https://video.twimg.com/amplify_video/1980613450381381632/vid/avc1/1928x1080/F8ShpqggdFDProde.mp4",
        "caption": "Vidu's latest video model, Vidu Q2, is here! Motion range test",
        "sell": "运动幅度测试",
        "evidence": "Vidu's latest video model, Vidu Q2, is here! Motion range test",
    },
    {
        "id": "1982301523037344090",
        "handle": "towya_aillust",
        "likes": 7,
        "views": 482,
        "followers": 15557,
        "date": "2025-10-26",
        "dur_ms": 8083,
        "video_url": "https://video.twimg.com/amplify_video/1982299586552074240/vid/avc1/1890x1080/gXRVvH79wwUbK9nc.mp4",
        "caption": "Vidu Q2 Image-to-Video 魔法陣の出し方がカッコイイ",
        "sell": "空中战I2V",
        "evidence": "Vidu Q2 Image-to-Video #viducpp",
    },
    {
        "id": "1981212269238505826",
        "handle": "WuxiaRocks",
        "likes": 16,
        "views": 1134,
        "followers": 7809,
        "date": "2025-10-23",
        "dur_ms": 8041,
        "video_url": "https://video.twimg.com/amplify_video/1981208691723415552/vid/avc1/1920x1080/MG8th_wyu-2mO_ym.mp4",
        "caption": "I recreated some familiar Sora 2 memes using the new Vidu Q2 Reference-to-video",
        "sell": "复刻Sora梗",
        "evidence": "using the new Vidu Q2 Reference-to-video feature #ViduQ2",
    },
    {
        "id": "1980526689752072453",
        "handle": "neco1751662",
        "likes": 52,
        "views": 12191,
        "followers": 3247,
        "date": "2025-10-21",
        "dur_ms": 153958,
        "video_url": "https://video.twimg.com/amplify_video/1980523110336978944/vid/avc1/1280x720/2Jk1TlOk3F9C3LzU.mp4",
        "caption": "Pink The Cat Remake 全てVidu Q2 Reference to Video",
        "sell": "粉猫短片",
        "evidence": "全てVidu Q2 Reference to Videoを使用して制作しました",
    },
    {
        "id": "1990024955099291926",
        "handle": "Ayu_AI_0912",
        "likes": 42,
        "views": 8079,
        "followers": 3909,
        "date": "2025-11-16",
        "dur_ms": 35280,
        "video_url": "https://video.twimg.com/amplify_video/1990021507448557568/vid/avc1/1920x1080/0G8Mu-fShxmKl1xw.mp4",
        "caption": "Vidu Q2 超動いて楽しい！！動画：Vidu Q2 リファレンス機能",
        "sell": "妖精动作",
        "evidence": "動画：Vidu Q2 リファレンス機能 #ViduCPP #動かせるQ2",
    },
    {
        "id": "2004103038424973741",
        "handle": "wildmindai",
        "likes": 131,
        "views": 8651,
        "followers": 11427,
        "date": "2025-12-25",
        "dur_ms": 51349,
        "video_url": "https://video.twimg.com/amplify_video/2004102696610263040/vid/avc1/1920x1088/IzMyih30esABhtjB.mp4",
        "caption": "DreaMontage outperforms Vidu Q2, Pixverse V5 & Kling 2.5",
        "sell": "长镜头对比片",
        "evidence": "outperforms Vidu Q2, Pixverse V5 & Kling 2.5 (user placed under Vidu Q2)",
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
