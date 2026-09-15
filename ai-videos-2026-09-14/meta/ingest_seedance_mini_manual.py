#!/usr/bin/env python3
"""Ingest user-picked Seedance 2.0 Mini posts (manual=True)."""
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path("/workspace/ai-videos-2026-09-14")
META = ROOT / "meta"
sys.path.insert(0, str(META))

import process as P  # noqa: E402

MODEL = "Seedance 2.0 Mini"

CANDS = [
    {
        "id": "2077642205171511383",
        "handle": "lansenai",
        "likes": 31,
        "views": 3384,
        "followers": 10180,
        "date": "2026-07-16",
        "dur_ms": 31347,
        "video_url": "https://video.twimg.com/amplify_video/2077641567159083008/vid/avc1/2508x1440/W4kDJ49LekBY4uNM.mp4",
        "caption": "Seedance2.0 mini制作。五张脸，五种命运人物特写，武侠江湖。",
        "sell": "五张武侠脸特写",
        "evidence": "Seedance2.0 mini制作。五张脸，五种命运人物特写，武侠江湖。",
    },
    {
        "id": "2069541625626526104",
        "handle": "Kashiko_AIart",
        "likes": 222,
        "views": 5124,
        "followers": 13903,
        "date": "2026-06-23",
        "dur_ms": 29094,
        "video_url": "https://video.twimg.com/ext_tw_video/2069541579597963264/pu/vid/avc1/1256x720/CQjBRAUZv8wnLTUU.mp4",
        "caption": "カミナリちゃま @wavespeed_ai に Seedance2.0 mini があったので試してみた",
        "sell": "雷公奔跑",
        "evidence": "Seedance2.0 mini があったので試してみた 720p 15秒",
    },
    {
        "id": "2067176803698147518",
        "handle": "studio_oneroom",
        "likes": 59,
        "views": 9115,
        "followers": 4976,
        "date": "2026-06-17",
        "dur_ms": 14740,
        "video_url": "https://video.twimg.com/amplify_video/2067174875010379776/vid/avc1/1920x1080/wneHRx-p-jNrnudW.mp4",
        "caption": "コスパ最強のSeedance2.0 Mini この動画はCapCutのSeedance2.0 Miniで生成しています。",
        "sell": "Mini滑板疾走",
        "evidence": "CapCutのSeedance2.0 Miniで生成",
    },
    {
        "id": "2070348238205718591",
        "handle": "lansenai",
        "likes": 16,
        "views": 1334,
        "followers": 10180,
        "date": "2026-06-26",
        "dur_ms": 15033,
        "video_url": "https://video.twimg.com/amplify_video/2070347869320798208/vid/avc1/1280x720/mx8F9UzxbiV4fAeJ.mp4",
        "caption": "依旧seedance2.0 mini继续一个怪诞风格，中式场景",
        "sell": "中式怪诞恐怖场景",
        "evidence": "依旧seedance2.0 mini继续一个怪诞风格，中式场景",
    },
    {
        "id": "2067442678145683623",
        "handle": "genel_ai",
        "likes": 53,
        "views": 8134,
        "followers": 28750,
        "date": "2026-06-18",
        "dur_ms": 9833,
        "video_url": "https://video.twimg.com/amplify_video/2067159363702370305/vid/avc1/1920x1080/zOadL9BFJAC-rq99.mp4",
        "caption": "ChatGPT Images 2.0でコラージュ画像生成 Seedance2.0 Miniで動画化",
        "sell": "拼贴图转动画",
        "evidence": "Seedance2.0 Miniで動画化",
    },
    {
        "id": "2097264543038894563",
        "handle": "atlas_remake",
        "likes": 0,
        "views": 100,
        "followers": 33,
        "date": "2026-09-08",
        "dur_ms": 15041,
        "video_url": "https://video.twimg.com/amplify_video/2097263502893420544/vid/avc1/1920x1080/VLBBNhWu_yuKLhxt.mp4",
        "caption": "AAA-style character selection screen created with Seedance 2.0 Mini.",
        "sell": "游戏角色选择界面",
        "evidence": "created with Seedance 2.0 Mini",
    },
    {
        "id": "2073430386278052095",
        "handle": "superfang119",
        "likes": 4,
        "views": 2888,
        "followers": 369,
        "date": "2026-07-04",
        "dur_ms": 15103,
        "video_url": "https://video.twimg.com/amplify_video/2073430152181362688/vid/avc1/1280x720/7XXC7PG2He2SiMMc.mp4",
        "caption": "直接用seedance2.0 mini 出，感觉没有grok的那种风骚的味道",
        "sell": "草帽看网球",
        "evidence": "直接用seedance2.0 mini 出",
    },
    {
        "id": "2071966729618726915",
        "handle": "Vtuber7144",
        "likes": 37,
        "views": 718,
        "followers": 3413,
        "date": "2026-06-30",
        "dur_ms": 25356,
        "video_url": "https://video.twimg.com/amplify_video/2071966506229866496/vid/avc1/1440x1440/4VwcL6iPHv8hEpOo.mp4",
        "caption": "capcutのSeedance2.0とSeedance2.0 miniで動画を作りました。",
        "sell": "游戏动作参考",
        "evidence": "capcutのSeedance2.0とSeedance2.0 miniで動画を作りました @capcutapp_jp",
    },
    {
        "id": "2071616176539795724",
        "handle": "applete77191758",
        "likes": 21,
        "views": 817,
        "followers": 2291,
        "date": "2026-06-29",
        "dur_ms": 15104,
        "video_url": "https://video.twimg.com/amplify_video/2071615426988294144/vid/avc1/864x496/SZNk_7y-uQ6wOUqx.mp4",
        "caption": "リハビリ？も兼ねてSeedance2.0 miniで作成 なんだ？キャラが変わってしまった",
        "sell": "Mini角色漂移短片",
        "evidence": "Seedance2.0 miniで作成",
    },
    {
        "id": "2066666666956571135",
        "handle": "shirawiggles",
        "likes": 13,
        "views": 570,
        "followers": 3292,
        "date": "2026-06-15",
        "dur_ms": 15061,
        "video_url": "https://video.twimg.com/ext_tw_video/2066666574241468416/pu/vid/avc1/788x1400/1W0LfBHWzWiUHxya.mp4",
        "caption": "Video Model: Seedance2.0 mini @dreamina_ai #dreaminacpp",
        "sell": "DreamWorks风角色",
        "evidence": "Video Model: Seedance2.0 mini @dreamina_ai #dreaminacpp",
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
