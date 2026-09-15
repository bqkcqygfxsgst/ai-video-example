#!/usr/bin/env python3
"""Ingest user-picked Seedance 2.0 posts (manual=True)."""
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path("/workspace/ai-videos-2026-09-14")
META = ROOT / "meta"
sys.path.insert(0, str(META))

import process as P  # noqa: E402

MODEL = "Seedance 2.0"

CANDS = [
    {
        "id": "2023676595790376968",
        "handle": "sohbunshu",
        "likes": 4603,
        "views": 641110,
        "followers": 208651,
        "date": "2026-02-17",
        "dur_ms": 28277,
        "video_url": "https://video.twimg.com/amplify_video/2023642676764307463/vid/avc1/1906x1080/-TDf19rjv3nRXxlp.mp4",
        "caption": "Seedance2.0を使って半日で作った作品 使用費は１０００元",
        "sell": "半日做完的短片",
        "evidence": "Seedance2.0を使って半日で作った作品",
    },
    {
        "id": "2092933336679502290",
        "handle": "NVTDanh",
        "likes": 489,
        "views": 21226,
        "followers": 5529,
        "date": "2026-08-27",
        "dur_ms": 15069,
        "video_url": "https://video.twimg.com/amplify_video/2092931703329468416/vid/avc1/1280x720/OtPKOOxNpYC-XvJZ.mp4",
        "caption": "Day 70/100 Icarus first flight. Created with seedance2.0 on @dreamina_ai",
        "sell": "伊卡洛斯学飞绘本风",
        "evidence": "Created with seedance2.0 on @dreamina_ai #Dreaminacpp",
    },
    {
        "id": "2037364485229339040",
        "handle": "biz_fx50",
        "likes": 24603,
        "views": 2913156,
        "followers": 45185,
        "date": "2026-03-27",
        "dur_ms": 88421,
        "video_url": "https://video.twimg.com/amplify_video/2037064698869538818/vid/avc1/1074x596/Dg__l134WEUCW9Ev.mp4",
        "caption": "Sora終了で動画AIはSeedance2.0一択になった。これは魔法を捨て筋肉でヴォルデモートを挑むハリーポッターです。",
        "sell": "肌肉哈利对战伏地魔",
        "evidence": "Sora終了で動画AIはSeedance2.0一択になった",
    },
    {
        "id": "2098000061615722522",
        "handle": "ai_lifehack55",
        "likes": 99,
        "views": 1882,
        "followers": 2749,
        "date": "2026-09-10",
        "dur_ms": 45125,
        "video_url": "https://video.twimg.com/amplify_video/2097999483149946880/vid/avc1/1080x1080/OLc9L5DaqJhGc5wA.mp4",
        "caption": "Seedance2.0 本編のない予告編動画 The Last Bridge｜最後の架け橋 SJinn Seedance2.0",
        "sell": "最后的架桥预告片",
        "evidence": "Seedance2.0 本編のない予告編 SJinn Seedance2.0（動画生成）",
    },
    {
        "id": "2047335333042569411",
        "handle": "hibi_ai__",
        "likes": 5555,
        "views": 970742,
        "followers": 2558,
        "date": "2026-04-23",
        "dur_ms": 44300,
        "video_url": "https://video.twimg.com/amplify_video/2047323920869756928/vid/avc1/1920x1080/z5rVFukFvgX0vzy3.mp4",
        "caption": "最強のAIの組み合わせで1時間でMVできた GPT-Image2 × Seedance2 動画：Seedance2.0",
        "sell": "一小时做完的情侣MV",
        "evidence": "動画：Seedance2.0 音楽：Suno5.5 編集：CapCut",
    },
    {
        "id": "2098172059021127945",
        "handle": "chiha_20220301",
        "likes": 43,
        "views": 1007,
        "followers": 1502,
        "date": "2026-09-10",
        "dur_ms": 15068,
        "video_url": "https://video.twimg.com/amplify_video/2098171974711447552/vid/avc1/1920x1080/T2Zkgkkv_MBLIAd6.mp4",
        "caption": "今日の動画はCapCutのSeedance2.0で生成しています！【お城を見上げる帰り道】",
        "sell": "仰望城堡的归途",
        "evidence": "CapCutのSeedance2.0で生成 @capcutapp_jp #capcutcpp",
    },
    {
        "id": "2099257990692155398",
        "handle": "chiha_20220301",
        "likes": 61,
        "views": 1451,
        "followers": 1502,
        "date": "2026-09-13",
        "dur_ms": 15068,
        "video_url": "https://video.twimg.com/amplify_video/2099248532175851520/vid/avc1/1920x1080/3RwlUtD0WgtLJhDQ.mp4",
        "caption": "今日の動画はCapCutのSeedance2.0で生成しています！【魔法学校っぽい渡り廊下を歩く】",
        "sell": "魔法学校走廊行走",
        "evidence": "CapCutのSeedance2.0で生成 @capcutapp_jp #capcutcpp",
    },
    {
        "id": "2098076620422865144",
        "handle": "applete77191758",
        "likes": 24,
        "views": 1335,
        "followers": 2291,
        "date": "2026-09-10",
        "dur_ms": 10041,
        "video_url": "https://video.twimg.com/amplify_video/2098075547943497728/vid/avc1/854x480/Fnhw6IZKxUrVgRMw.mp4",
        "caption": "Seedance2.0で無理だったので2.5で生成しました。 #capcut生成ai",
        "sell": "猫科跑酷动作",
        "evidence": "Seedance2.0で無理だったので2.5で生成しました #capcut生成ai",
    },
    {
        "id": "2099335496396853326",
        "handle": "bDAxjGohPDX7XiV",
        "likes": 0,
        "views": 27,
        "followers": 33,
        "date": "2026-09-14",
        "dur_ms": 5088,
        "video_url": "https://video.twimg.com/amplify_video/2099334650670002176/vid/avc1/1280x720/Xs6YUnaCI24MrEyQ.mp4?tag=14",
        "caption": "Seedance2.0もまだまだ良いね。滑らかだ。 #seedance",
        "sell": "流畅运镜短片",
        "evidence": "Seedance2.0もまだまだ良いね #seedance",
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
