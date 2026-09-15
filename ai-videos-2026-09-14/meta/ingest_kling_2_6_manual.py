#!/usr/bin/env python3
"""Ingest user-picked Kling 2.6 posts (manual=True)."""
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path("/workspace/ai-videos-2026-09-14")
META = ROOT / "meta"
sys.path.insert(0, str(META))

import process as P  # noqa: E402

MODEL = "Kling 2.6"

CANDS = [
    {
        "id": "2009588496869040536",
        "handle": "CharaspowerAI",
        "likes": 1030,
        "views": 89018,
        "followers": 54233,
        "date": "2026-01-09",
        "dur_ms": 10041,
        "video_url": "https://video.twimg.com/ext_tw_video/2009588462786088960/pu/vid/avc1/1280x720/Z5i7_SMOo4dstN2x.mp4?tag=12",
        "caption": "I'm using JSON prompts more and more with Kling 2.6",
        "sell": "JSON提示控制",
        "evidence": "JSON prompts more and more with Kling 2.6",
    },
    {
        "id": "2028041714158735434",
        "handle": "WuxiaRocks",
        "likes": 78,
        "views": 7446,
        "followers": 7809,
        "date": "2026-03-01",
        "dur_ms": 10041,
        "video_url": "https://video.twimg.com/amplify_video/2028041562878623744/vid/avc1/1920x1080/cTX_FGI8gwVg4CJ6.mp4",
        "caption": "How cinematic is Kling 2.6? Very cinematic. Kling 2.6 @ImagineArt_X",
        "sell": "电影感镜头",
        "evidence": "How cinematic is Kling 2.6? Kling 2.6 @ImagineArt_X",
    },
    {
        "id": "1997233757020119476",
        "handle": "WuxiaRocks",
        "likes": 390,
        "views": 18642,
        "followers": 7809,
        "date": "2025-12-06",
        "dur_ms": 10041,
        "video_url": "https://video.twimg.com/amplify_video/1997233365490302977/vid/avc1/1920x1080/sTj-tFj52K2KATzq.mp4",
        "caption": "Kling 2.6 is here to take fight scenes to the next level.",
        "sell": "格斗对打",
        "evidence": "Kling 2.6 is here to take fight scenes Kling 2.6 = Fire",
    },
    {
        "id": "2004833980361965679",
        "handle": "rovvmut_",
        "likes": 11910,
        "views": 1296027,
        "followers": 31542,
        "date": "2025-12-27",
        "dur_ms": 13600,
        "video_url": "https://video.twimg.com/amplify_video/2004833747255066624/vid/avc1/1072x1936/F9WuoHyd2HPret0M.mp4",
        "caption": "Donald Trump has got some moves Kling 2.6 Motion Control",
        "sell": "特朗普舞蹈",
        "evidence": "Kling 2.6 Motion Control",
    },
    {
        "id": "2008073112966058258",
        "handle": "SHD766",
        "likes": 641,
        "views": 28161,
        "followers": 3018,
        "date": "2026-01-05",
        "dur_ms": 14600,
        "video_url": "https://video.twimg.com/amplify_video/2008073048210227200/vid/avc1/720x1280/QC-XXwNhOGWO-3Mp.mp4",
        "caption": "kling 2.6 motion control is insane",
        "sell": "动作控制",
        "evidence": "kling 2.6 motion control is insane",
    },
    {
        "id": "2007726590994911252",
        "handle": "rovvmut_",
        "likes": 589,
        "views": 64085,
        "followers": 31542,
        "date": "2026-01-04",
        "dur_ms": 14666,
        "video_url": "https://video.twimg.com/amplify_video/2007726419888295936/vid/avc1/1072x1936/ijth9lkYax98yTbO.mp4",
        "caption": "Joining the trend. Kling 2.6 Motion Control",
        "sell": "和尚跳舞",
        "evidence": "Kling 2.6 Motion Control",
    },
    {
        "id": "2014914360028922175",
        "handle": "h_ashizawaJP",
        "likes": 343,
        "views": 16030,
        "followers": 28494,
        "date": "2026-01-24",
        "dur_ms": 35300,
        "video_url": "https://video.twimg.com/amplify_video/2014914227274973189/vid/avc1/1080x1920/JSB7wWzVYDKoR0Ed.mp4",
        "caption": "Kling 2.6で生成したホラー。編集なしで効果音もKling 2.6",
        "sell": "原生音效恐怖",
        "evidence": "Kling 2.6で生成したホラー 効果音もKling 2.6 @Kling_ai",
    },
    {
        "id": "2013545633219780831",
        "handle": "WuxiaRocks",
        "likes": 1695,
        "views": 255029,
        "followers": 7809,
        "date": "2026-01-20",
        "dur_ms": 10041,
        "video_url": "https://video.twimg.com/amplify_video/2013545362896683009/vid/avc1/1920x1080/ytKkBzj7m9SXTO6O.mp4",
        "caption": "Want action? Want explosions? Want Ninjas? Kling 2.6 says all of it.",
        "sell": "忍者爆炸",
        "evidence": "Kling 2.6 says all of it",
    },
    {
        "id": "2099391427331424418",
        "handle": "kayforkind",
        "likes": 1,
        "views": 38,
        "followers": 136,
        "date": "2026-09-14",
        "dur_ms": 10100,
        "video_url": "https://video.twimg.com/amplify_video/2099386695175266304/vid/avc1/1920x1080/YTbeb46EX0OuhC6B.mp4",
        "caption": "#3/10 Kling 2.6 FPV freefall through an impossible fortress",
        "sell": "要塞自由落体",
        "evidence": "Kling 2.6 FPV freefall through an impossible fortress",
    },
    {
        "id": "2001707617765540042",
        "handle": "Solopopsss",
        "likes": 4816,
        "views": 661464,
        "followers": 35128,
        "date": "2025-12-18",
        "dur_ms": 7200,
        "video_url": "https://video.twimg.com/amplify_video/2001707130634579968/vid/avc1/1776x1168/POYkoyDGdOhKGIuA.mp4",
        "caption": "Tested out the new Kling 2.6 Motion control as a viability for AI influencers",
        "sell": "动作控制网红",
        "evidence": "Kling 2.6 Motion control as a viability for AI influencers",
    },
    {
        "id": "1996944817205793262",
        "handle": "CHAO2U_AI",
        "likes": 285,
        "views": 4641,
        "followers": 7587,
        "date": "2025-12-05",
        "dur_ms": 10041,
        "video_url": "https://video.twimg.com/amplify_video/1996938719061016576/vid/avc1/1244x1664/ndWDS6-ekUmZc-b-.mp4",
        "caption": "Generated by @higgsfield_ai - Kling 2.6 bashful K-Pop Cute Dance",
        "sell": "害羞舞蹈",
        "evidence": "Generated by @higgsfield_ai - Kling 2.6 #higgsfield_Kling26",
    },
    {
        "id": "1997283058136048045",
        "handle": "CHAO2U_AI",
        "likes": 253,
        "views": 5581,
        "followers": 7587,
        "date": "2025-12-06",
        "dur_ms": 10041,
        "video_url": "https://video.twimg.com/amplify_video/1997279637676982272/vid/avc1/1244x1664/5D1pxTmpPm6KMKzQ.mp4",
        "caption": "Generated by @higgsfield_ai - Kling 2.6 Prompt: bashful, sing",
        "sell": "唱歌复活战",
        "evidence": "Generated by @higgsfield_ai - Kling 2.6 #higgsfield_Kling26",
    },
    {
        "id": "1997023870050574842",
        "handle": "TheAva_AI",
        "likes": 9,
        "views": 90869,
        "followers": 11373,
        "date": "2025-12-05",
        "dur_ms": 9440,
        "video_url": "https://video.twimg.com/amplify_video/1997023816027947008/vid/avc1/1000x800/OiBxedo-FOyHHdO2.mp4",
        "caption": "UNLIMITED Kling 2.6 with Native Audio is LIVE. Higgsfield Kling 2.6",
        "sell": "原生音频宣传",
        "evidence": "UNLIMITED Kling 2.6 with Native Audio Higgsfield Kling 2.6",
    },
    {
        "id": "1996245765207867563",
        "handle": "openart_ai",
        "likes": 405,
        "views": 27452,
        "followers": 78290,
        "date": "2025-12-03",
        "dur_ms": 58955,
        "video_url": "https://video.twimg.com/amplify_video/1996245223958016000/vid/avc1/2560x1440/SqkzhZiHqF4UJdOv.mp4",
        "caption": "Introducing Kling 2.6 on OpenArt! with native audio @Kling_ai",
        "sell": "官方上线片",
        "evidence": "Introducing Kling 2.6 on OpenArt native audio @Kling_ai",
    },
    {
        "id": "2008333801303453893",
        "handle": "higgsfield_ai",
        "likes": 2828,
        "views": 1151653,
        "followers": 230516,
        "date": "2026-01-06",
        "dur_ms": 12158,
        "video_url": "https://video.twimg.com/amplify_video/2008333732353372165/vid/avc1/1280x720/0hKDIMlDPXvFpjxK.mp4?tag=14",
        "caption": "7 days UNLIMITED Kling 2.6, Seedance 1.5 Pro, Hailuo 2.3 Fast.",
        "sell": "促销宣传",
        "evidence": "UNLIMITED Kling 2.6, Seedance 1.5 Pro, Hailuo 2.3 Fast",
    },
    {
        "id": "2003111539247648819",
        "handle": "MonetizationDon",
        "likes": 117,
        "views": 1043,
        "followers": 10343,
        "date": "2025-12-22",
        "dur_ms": 10041,
        "video_url": "https://video.twimg.com/amplify_video/2003110895606501376/vid/avc1/1920x1080/dZVBIPilxl6PpMXK.mp4",
        "caption": "jaw-dropping fight scenes all powered by Kling 2.6 on @higgsfield_ai",
        "sell": "功夫对打",
        "evidence": "powered by Kling 2.6 on @higgsfield_ai",
    },
    {
        "id": "1996991183252607425",
        "handle": "hedra_labs",
        "likes": 2314,
        "views": 1649015,
        "followers": 54144,
        "date": "2025-12-05",
        "dur_ms": 41750,
        "video_url": "https://video.twimg.com/amplify_video/1996991093402226691/vid/avc1/1290x720/rl4OLNfRcKm4sMp7.mp4?tag=14",
        "caption": "SOUND ON! Kling 2.6 with Native Audio just landed in Hedra.",
        "sell": "原生音频上线",
        "evidence": "Kling 2.6 with Native Audio just landed in Hedra",
    },
    {
        "id": "1997247060970721384",
        "handle": "codewithimanshu",
        "likes": 74,
        "views": 274700,
        "followers": 68703,
        "date": "2025-12-06",
        "dur_ms": 10040,
        "video_url": "https://video.twimg.com/amplify_video/1997247001893928960/vid/avc1/960x720/U9MEIxE1C9yex3ZQ.mp4?tag=14",
        "caption": "Cyber Week just brought Kling 2.6 to Higgsfield What's new in Kling 2.6 Pro",
        "sell": "电影创作者",
        "evidence": "brought Kling 2.6 to Higgsfield Kling 2.6 Pro",
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
