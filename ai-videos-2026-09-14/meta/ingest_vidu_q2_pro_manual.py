#!/usr/bin/env python3
"""Ingest user-picked Vidu Q2 Pro posts (manual=True)."""
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path("/workspace/ai-videos-2026-09-14")
META = ROOT / "meta"
sys.path.insert(0, str(META))

import process as P  # noqa: E402

MODEL = "Vidu Q2 Pro"

CANDS = [
    {
        "id": "1988257018809929903",
        "handle": "wavespeed_ai",
        "likes": 37,
        "views": 3178,
        "followers": 8564,
        "date": "2025-11-11",
        "dur_ms": 5083,
        "video_url": "https://video.twimg.com/amplify_video/1988256817281896449/vid/avc1/1282x718/5wzIsjqtA6TnWonO.mp4",
        "caption": "Vidu Q2 Turbo & Pro bring your characters to life",
        "sell": "角色开启动画",
        "evidence": "Vidu Q2 Turbo & Pro bring your characters to life #ViduQ2",
    },
    {
        "id": "2016085477355409445",
        "handle": "seiiiiiiiiiiru",
        "likes": 205,
        "views": 16706,
        "followers": 23237,
        "date": "2026-01-27",
        "dur_ms": 8000,
        "video_url": "https://video.twimg.com/amplify_video/2016083342962360321/vid/avc1/1080x1244/z6ZwbjJha_kId4fn.mp4",
        "caption": "【Vidu AI】Q2Proリリース リファレンスの始祖Vidu",
        "sell": "参考生成演示",
        "evidence": "Q2Proリリース 動画や画像を参照してプロンプト指示で動画を生成",
    },
    {
        "id": "2016841728008003755",
        "handle": "nbykos",
        "likes": 181,
        "views": 16844,
        "followers": 25614,
        "date": "2026-01-29",
        "dur_ms": 10100,
        "video_url": "https://video.twimg.com/amplify_video/2016840549727424513/vid/avc1/1920x1080/SnDG-GqVYzAsmGeJ.mp4",
        "caption": "Vidu Q2 Proは参照生成特有の細部の描画の崩れが無い",
        "sell": "3D风格参照",
        "evidence": "Vidu Q2 Proは参照生成特有の細部の描画の崩れが無い",
    },
    {
        "id": "2016149008092430413",
        "handle": "ai_artworkgen",
        "likes": 27,
        "views": 2424,
        "followers": 23783,
        "date": "2026-01-27",
        "dur_ms": 5066,
        "video_url": "https://video.twimg.com/amplify_video/2016148956624117760/vid/avc1/1280x720/8aLW6kqio3p08mdf.mp4?tag=14",
        "caption": "Vidu Q2 R2V Pro is HERE. What if you could edit video like text?",
        "sell": "视频编辑控制",
        "evidence": "Vidu Q2 R2V Pro is HERE Ref2Vid Pro",
    },
    {
        "id": "2016164936045760610",
        "handle": "KEETY2591756",
        "likes": 56,
        "views": 3860,
        "followers": 2146,
        "date": "2026-01-27",
        "dur_ms": 18833,
        "video_url": "https://video.twimg.com/amplify_video/2016164659108495360/vid/avc1/1920x1080/KTosDQj1Q5wNcGlh.mp4",
        "caption": "Vidu Q2-Proリリース 動画リファレンス",
        "sell": "视频参考",
        "evidence": "Vidu Q2-Proリリース @ViduAI_official #ViduCPP",
    },
    {
        "id": "2016125009920450758",
        "handle": "ExquisitMe",
        "likes": 1,
        "views": 54,
        "followers": 0,
        "date": "2026-01-27",
        "dur_ms": 22101,
        "video_url": "https://video.twimg.com/amplify_video/2016123787826073600/vid/avc1/1280x720/1TzeLfUBIrykKo8E.mp4?tag=14",
        "caption": "Vidu Q2 Pro kicks some.. Clone or Sync movement, replace character",
        "sell": "动作克隆换人",
        "evidence": "Vidu Q2 Pro Clone or Sync movement #ViduQ2R2VPro",
    },
    {
        "id": "1994345237213274247",
        "handle": "ROSHENDILAN",
        "likes": 4,
        "views": 122,
        "followers": 524,
        "date": "2025-11-28",
        "dur_ms": 30000,
        "video_url": "https://video.twimg.com/amplify_video/1994345165629083649/vid/avc1/1080x1920/4FwCgU-TOI1_R7jJ.mp4",
        "caption": "Created with Midjourney V7 Vidu Q2 Pro ElevenLabs",
        "sell": "雪中孩童小狗",
        "evidence": "Created with Midjourney V7 Vidu Q2 Pro",
    },
    {
        "id": "2042559646154789201",
        "handle": "SasaruGAI",
        "likes": 2,
        "views": 101,
        "followers": 371,
        "date": "2026-04-10",
        "dur_ms": 8000,
        "video_url": "https://video.twimg.com/amplify_video/2042559591880495105/vid/avc1/1280x720/fA2F7uLPJyMlT21f.mp4",
        "caption": "Vidu Q2 pro 私の鉄板ネタを実写系でしてみました",
        "sell": "实写铁板梗",
        "evidence": "Vidu Q2 pro 私の鉄板ネタを実写系で",
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
