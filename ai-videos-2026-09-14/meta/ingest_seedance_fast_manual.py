#!/usr/bin/env python3
"""Ingest user-picked Seedance 2.0 Fast posts (manual=True)."""
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path("/workspace/ai-videos-2026-09-14")
META = ROOT / "meta"
sys.path.insert(0, str(META))

import process as P  # noqa: E402

MODEL = "Seedance 2.0 Fast"

CANDS = [
    {
        "id": "2062656780484907190",
        "handle": "Kashiko_AIart",
        "likes": 146,
        "views": 3722,
        "followers": 13903,
        "date": "2026-06-04",
        "dur_ms": 25117,
        "video_url": "https://video.twimg.com/amplify_video/2062656271531298816/vid/avc1/1254x720/8HgVlpzKASMfsXQ0.mp4",
        "caption": "Seedance2.0 Turboが安くて速くてめっちゃ良い！Seedance2.0 TurboのFast（高速）モード 720p",
        "sell": "Turbo Fast 推背奔跑",
        "evidence": "Seedance2.0 TurboのFast（高速）モード 720p WaveSpeedAI",
    },
    {
        "id": "2071875780091756966",
        "handle": "kellyyjjones",
        "likes": 99,
        "views": 50760,
        "followers": 3260,
        "date": "2026-06-30",
        "dur_ms": 8095,
        "video_url": "https://video.twimg.com/amplify_video/2071875580690096128/vid/avc1/1280x720/aZOe9JEBQg0ZaSqm.mp4",
        "caption": "Made with Seedance2.0 Fast by @Lart_AI Shadow Monarch warrior",
        "sell": "暗影君主拔刀",
        "evidence": "Made with Seedance2.0 Fast by @Lart_AI",
    },
    {
        "id": "2072547334903452111",
        "handle": "kellyyjjones",
        "likes": 109,
        "views": 27060,
        "followers": 3260,
        "date": "2026-07-02",
        "dur_ms": 8095,
        "video_url": "https://video.twimg.com/amplify_video/2072547233900396544/vid/avc1/1280x720/mYvHlcl8v81rgSEp.mp4",
        "caption": "Made with Seedance2.0 Fast by @Lart_AI cozy farmhouse farmer routine",
        "sell": "农夫一日新海诚风",
        "evidence": "Made with Seedance2.0 Fast by @Lart_AI",
    },
    {
        "id": "2077764228786901360",
        "handle": "kellyyjjones",
        "likes": 139,
        "views": 21453,
        "followers": 3260,
        "date": "2026-07-16",
        "dur_ms": 10080,
        "video_url": "https://video.twimg.com/amplify_video/2077764064047144960/vid/avc1/1280x720/w8e80AlB07UtNNks.mp4",
        "caption": "Where peace meets the horizon. Made with Seedance2.0 Fast by @Lart_AI",
        "sell": "山谷阳台看蝴蝶",
        "evidence": "Made with Seedance2.0 Fast by @Lart_AI",
    },
    {
        "id": "2097358700428059003",
        "handle": "aimikoda",
        "likes": 193,
        "views": 10878,
        "followers": 29072,
        "date": "2026-09-08",
        "dur_ms": 23196,
        "video_url": "https://video.twimg.com/amplify_video/2097358492759633920/vid/avc1/2560x1440/8TZkPoCGshVATErl.mp4",
        "caption": "Seedance 2.5 + Midjourney v8.2 sped up to 1.30x",
        "sell": "白发对战紫甲",
        "evidence": "Seedance 2.5 + Midjourney v8.2",
    },
    {
        "id": "2097985576137875651",
        "handle": "Xaroon_x",
        "likes": 195,
        "views": 8377,
        "followers": 10258,
        "date": "2026-09-10",
        "dur_ms": 24760,
        "video_url": "https://video.twimg.com/amplify_video/2097985276794830848/vid/avc1/1080x1920/v6C1YkKNyKSnr4iF.mp4",
        "caption": "Hollywood-style alien invasion cinematic with Seedance 2.5 on @wavespeed_ai",
        "sell": "外星入侵变身",
        "evidence": "Seedance 2.5 on @wavespeed_ai",
    },
    {
        "id": "2072976926000418992",
        "handle": "kellyyjjones",
        "likes": 171,
        "views": 23506,
        "followers": 3260,
        "date": "2026-07-03",
        "dur_ms": 8160,
        "video_url": "https://video.twimg.com/amplify_video/2072976841019891712/vid/avc1/1280x720/DzPLtuuIubTkSjMN.mp4",
        "caption": "Made with Seedance2.0 Fast by @Lart_AI miniature village",
        "sell": "微缩村庄航拍",
        "evidence": "Made with Seedance2.0 Fast by @Lart_AI",
    },
    {
        "id": "2041050487626285111",
        "handle": "Adam38363368936",
        "likes": 12,
        "views": 7524,
        "followers": 17066,
        "date": "2026-04-06",
        "dur_ms": 15066,
        "video_url": "https://video.twimg.com/amplify_video/2041049185085169664/vid/avc1/1280x720/YItoUeElPGjZQrbP.mp4",
        "caption": "深渊主宰·万物凋零。用Seedance2.0 fast试验生成宏大的电影片段",
        "sell": "深渊主宰万物凋零",
        "evidence": "用Seedance2.0 fast试验生成宏大的电影片段",
    },
    {
        "id": "2067709390585790859",
        "handle": "banana_ai_club1",
        "likes": 48,
        "views": 4851,
        "followers": 41532,
        "date": "2026-06-18",
        "dur_ms": 8057,
        "video_url": "https://video.twimg.com/amplify_video/2067709114411847680/vid/avc1/1112x834/on7o2gCy_D-eg22T.mp4",
        "caption": "higgsfield Enhanced Seedance2.0 Fast 8秒720P",
        "sell": "Higgsfield Fast 八秒",
        "evidence": "higgsfield Enhanced Seedance2.0 Fast 8秒720P",
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
