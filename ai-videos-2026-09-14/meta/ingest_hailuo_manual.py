#!/usr/bin/env python3
"""Ingest user-picked Hailuo AI posts into the catalog (manual=True)."""
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
        "id": "2098261672066785574",
        "handle": "ai_Tyler_no_bu",
        "likes": 5,
        "views": 275,
        "followers": 1458,
        "date": "2026-09-11",
        "dur_ms": 15083,
        "video_url": "https://video.twimg.com/amplify_video/2098261531343667200/vid/avc1/1280x720/myEBr-G3MuR0Wmh0.mp4?tag=14",
        "caption": "MiniMax Designで制作 @Hailuo_AI 中国時代劇のオープニングムービー風",
        "sell": "中国时代剧片头风",
        "evidence": "MiniMax Designで制作 @Hailuo_AI #MiniMaxDesign #HailuoAI",
    },
    {
        "id": "2097967040460145051",
        "handle": "TaoRInne",
        "likes": 63,
        "views": 2639,
        "followers": 2357,
        "date": "2026-09-10",
        "dur_ms": 30166,
        "video_url": "https://video.twimg.com/amplify_video/2097966959791108097/vid/avc1/2560x1440/BmuZ0oo5g6p6C3FY.mp4",
        "caption": "映像作品『廻哀村（えあいむら）』予告映像 Movie：@hailuoai",
        "sell": "廻哀村预告片",
        "evidence": "Movie：@hailuoai",
    },
    {
        "id": "2097362270820987276",
        "handle": "PrometheanAIX",
        "likes": 51,
        "views": 5177,
        "followers": 6003,
        "date": "2026-09-08",
        "dur_ms": 8000,
        "video_url": "https://video.twimg.com/amplify_video/2097361563862933507/vid/avc1/768x1024/ApoDy22aROVTXN55.mp4",
        "caption": "PROMPT SHARE #HailuoCPP #HailuoAI @Hailuo_AI Paid partnership with Hailuo.",
        "sell": "白裙都市街拍行走",
        "evidence": "#HailuoCPP #HailuoAI @Hailuo_AI Paid partnership with Hailuo.",
    },
    {
        "id": "1943654004208062684",
        "handle": "beholdersai",
        "likes": 514,
        "views": 10688,
        "followers": 8890,
        "date": "2025-07-11",
        "dur_ms": 11708,
        "video_url": "https://video.twimg.com/amplify_video/1943639821550845952/vid/avc1/720x720/pkc9eHSSsTMkCPKX.mp4?tag=14",
        "caption": "Great morning! A soft, sleepy gleam #hailuoai",
        "sell": "晨光里的萌兽醒来",
        "evidence": "#hailuoai",
    },
    {
        "id": "2095376965293269453",
        "handle": "Romi2656",
        "likes": 78,
        "views": 14303,
        "followers": 10070,
        "date": "2026-09-03",
        "dur_ms": 15083,
        "video_url": "https://video.twimg.com/amplify_video/2095376653807710208/vid/avc1/1440x2560/53uEJw-J8Y8V5mtv.mp4",
        "caption": "From dull to fresh, smooth, and frizz-free. Created with @Hailuo_AI #MiniMaxH3 #HailuoAI",
        "sell": "护发柔顺前后对比",
        "evidence": "Created with @Hailuo_AI #MiniMaxH3 #HailuoAI",
    },
    {
        "id": "2098261736268984484",
        "handle": "ai_Tyler_no_bu",
        "likes": 3,
        "views": 226,
        "followers": 1458,
        "date": "2026-09-11",
        "dur_ms": 15104,
        "video_url": "https://video.twimg.com/amplify_video/2098261706623553536/vid/avc1/720x1260/RMEhjqpkmG-UVlz2.mp4?tag=14",
        "caption": "MiniMax Designで制作 @Hailuo_AI #MiniMaxDesign #HailuoAI",
        "sell": "MiniMax Design 竖屏短片",
        "evidence": "MiniMax Designで制作 @Hailuo_AI #HailuoAI",
    },
    {
        "id": "2095572832394621431",
        "handle": "PrometheanAIX",
        "likes": 39,
        "views": 3097,
        "followers": 6003,
        "date": "2026-09-03",
        "dur_ms": 10125,
        "video_url": "https://video.twimg.com/amplify_video/2095572339245162497/vid/avc1/768x1024/8yTUhAZFYla9tfYQ.mp4",
        "caption": "PROMPTSHARE #HailuoCPP #HailuoAI @Hailuo_AI Paid partnership with Hailuo.",
        "sell": "屋顶低机位男装大片",
        "evidence": "#HailuoCPP #HailuoAI @Hailuo_AI Paid partnership with Hailuo.",
    },
    {
        "id": "1959040387781197833",
        "handle": "HakumaiDev",
        "likes": 1218,
        "views": 17603,
        "followers": 22167,
        "date": "2025-08-22",
        "dur_ms": 10125,
        "video_url": "https://video.twimg.com/amplify_video/1958952569902178304/vid/avc1/768x768/WgyuHpywBMJOwVoP.mp4",
        "caption": "〜 赤虎の咆哮 〜 Crimson Tiger Roar #HailuoAI",
        "sell": "赤虎咆哮",
        "evidence": "#HailuoAI",
    },
    {
        "id": "2096146384260870331",
        "handle": "JayKay65220066",
        "likes": 109,
        "views": 6676,
        "followers": 14148,
        "date": "2026-09-05",
        "dur_ms": 15083,
        "video_url": "https://video.twimg.com/amplify_video/2096117671649775616/vid/avc1/1344x768/zwbzs96DFePkfn-b.mp4",
        "caption": "Whimsical Carnival Magic! Made with MiniMax H3 video model from @Hailuo_AI!",
        "sell": "奇幻嘉年华",
        "evidence": "Made with MiniMax H3 video model from @Hailuo_AI!",
    },
    {
        "id": "2095481944523853857",
        "handle": "JayKay65220066",
        "likes": 113,
        "views": 4695,
        "followers": 14148,
        "date": "2026-09-03",
        "dur_ms": 15083,
        "video_url": "https://video.twimg.com/amplify_video/2095401247637716992/vid/avc1/1344x768/luqQXtaCs6URaZ_z.mp4",
        "caption": "Watch Shop Whimsy! Made with MiniMax H3 video model from @Hailuo_AI!",
        "sell": "钟表店奇想",
        "evidence": "Made with MiniMax H3 video model from @Hailuo_AI!",
    },
    {
        "id": "2095119574031122897",
        "handle": "JayKay65220066",
        "likes": 83,
        "views": 4100,
        "followers": 14148,
        "date": "2026-09-02",
        "dur_ms": 15083,
        "video_url": "https://video.twimg.com/amplify_video/2095036537972953088/vid/avc1/1344x768/eymrQ39QoOzoziqV.mp4",
        "caption": "Rocky Vocal Performance! Made with MiniMax H3 video model from @Hailuo_AI!",
        "sell": "石头人演唱",
        "evidence": "Made with MiniMax H3 video model from @Hailuo_AI!",
    },
    {
        "id": "1867240573821968727",
        "handle": "ciguleva",
        "likes": 1953,
        "views": 130775,
        "followers": 238488,
        "date": "2024-12-12",
        "dur_ms": 5640,
        "video_url": "https://video.twimg.com/ext_tw_video/1867240438274625536/pu/vid/avc1/720x1072/5Dof-no1hCtjC0zs.mp4?tag=12",
        "caption": "I'll start. Hailuoai. No prompts, 1 iteration.",
        "sell": "外星人看平板 Hailuo I2V",
        "evidence": "I'll start. Hailuoai. No prompts, 1 iteration.",
    },
]


def next_n() -> int:
    n = 201
    if (P.VIDEOS).exists():
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
    c = {
        **c,
        "model": "Hailuo AI",
        "manual": True,
        "handle": handle,
    }
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
    if dur > 35.0:
        print("  REJECT over 35s", flush=True)
        raw.unlink(missing_ok=True)
        return "reject"

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
        "model": "Hailuo AI",
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

    # merge into candidates.json for bookkeeping
    cand_path = META / "candidates.json"
    existing = json.loads(cand_path.read_text()) if cand_path.exists() else []
    have = {str(x.get("id")) for x in existing}
    added = 0
    for c in CANDS:
        if str(c["id"]) not in have:
            existing.append(
                {
                    **c,
                    "model": "Hailuo AI",
                    "manual": True,
                }
            )
            added += 1
    if added:
        cand_path.write_text(json.dumps(existing, ensure_ascii=False, indent=2), encoding="utf-8")
        print("candidates +", added, "now", len(existing), flush=True)


if __name__ == "__main__":
    main()
