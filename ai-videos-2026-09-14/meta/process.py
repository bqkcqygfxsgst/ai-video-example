#!/usr/bin/env python3
"""Download, duration-check, frame-extract, OCR-filter X videos."""
from __future__ import annotations

import json
import os
import re
import subprocess
import sys
import time
import urllib.request
from pathlib import Path

ROOT = Path("/workspace/ai-videos-2026-09-14")
VIDEOS = ROOT / "videos"
FRAMES = ROOT / "frames"
META = ROOT / "meta"
RAW = ROOT / "_raw"
for p in (VIDEOS, FRAMES, META, RAW):
    p.mkdir(parents=True, exist_ok=True)

UA = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36"
)
MIN_S, MAX_S = 8.0, 35.0

ocr_engine = None


def get_ocr():
    global ocr_engine
    if ocr_engine is None:
        from rapidocr_onnxruntime import RapidOCR

        ocr_engine = RapidOCR()
    return ocr_engine


def ffprobe_duration(path: Path) -> float | None:
    cmd = [
        "ffmpeg",
        "-hide_banner",
        "-i",
        str(path),
        "-f",
        "null",
        "-",
    ]
    r = subprocess.run(cmd, capture_output=True, text=True)
    text = r.stderr or ""
    m = re.search(r"Duration: (\d+):(\d+):(\d+(?:\.\d+)?)", text)
    if not m:
        return None
    h, mn, s = int(m.group(1)), int(m.group(2)), float(m.group(3))
    return h * 3600 + mn * 60 + s


def ffprobe_wh(path: Path) -> tuple[int, int]:
    cmd = [
        "ffmpeg",
        "-hide_banner",
        "-i",
        str(path),
        "-f",
        "null",
        "-",
    ]
    r = subprocess.run(cmd, capture_output=True, text=True)
    m = re.search(r"Stream #0:0.*?, (\d+)x(\d+)", r.stderr or "")
    if not m:
        return (0, 0)
    return int(m.group(1)), int(m.group(2))


def download_curl(url: str, dest: Path) -> bool:
    dest.parent.mkdir(parents=True, exist_ok=True)
    tmp = dest.with_suffix(dest.suffix + ".part")
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Referer": "https://x.com/"})
    try:
        with urllib.request.urlopen(req, timeout=90) as resp, open(tmp, "wb") as f:
            while True:
                chunk = resp.read(1024 * 256)
                if not chunk:
                    break
                f.write(chunk)
        tmp.replace(dest)
        return dest.stat().st_size > 50_000
    except Exception as e:
        print(f"  curl fail: {e}", flush=True)
        if tmp.exists():
            tmp.unlink()
        return False


def download_ytdlp(tweet_url: str, dest: Path) -> bool:
    tmpdir = RAW / dest.stem
    tmpdir.mkdir(exist_ok=True)
    cmd = [
        "yt-dlp",
        "--no-warnings",
        "-f",
        "bv*[height<=1080]+ba/b[height<=1080]/b",
        "--merge-output-format",
        "mp4",
        "-o",
        str(tmpdir / "clip.%(ext)s"),
        tweet_url,
    ]
    r = subprocess.run(cmd, capture_output=True, text=True, timeout=180)
    files = list(tmpdir.glob("clip.*"))
    if not files:
        print("  ytdlp fail:", (r.stderr or r.stdout)[-400:], flush=True)
        return False
    files[0].replace(dest)
    return dest.exists() and dest.stat().st_size > 50_000


def transcode_1080(src: Path, dest: Path) -> bool:
    w, h = ffprobe_wh(src)
    if w == 0:
        src.replace(dest)
        return True
    scale = []
    if max(w, h) > 1080:
        # keep aspect, longest side 1080
        scale = ["-vf", "scale='if(gt(iw,ih),1080,-2)':'if(gt(ih,iw),1080,-2)'"]
    cmd = [
        "ffmpeg",
        "-y",
        "-hide_banner",
        "-loglevel",
        "error",
        "-i",
        str(src),
        *scale,
        "-c:v",
        "libx264",
        "-preset",
        "veryfast",
        "-crf",
        "20",
        "-c:a",
        "aac",
        "-b:a",
        "128k",
        "-movflags",
        "+faststart",
        str(dest),
    ]
    r = subprocess.run(cmd, capture_output=True, text=True, timeout=480)
    if r.returncode != 0 or not dest.exists():
        print("  transcode fail", r.stderr[-300:], flush=True)
        return False
    return True


def extract_frames(video: Path, stem: str, duration: float) -> list[Path]:
    out_dir = FRAMES / stem
    out_dir.mkdir(parents=True, exist_ok=True)
    positions = [0.15, 0.40, 0.65, 0.90]
    paths = []
    for i, p in enumerate(positions):
        t = max(0.05, min(duration * p, duration - 0.05))
        fp = out_dir / f"{i}.jpg"
        cmd = [
            "ffmpeg",
            "-y",
            "-hide_banner",
            "-loglevel",
            "error",
            "-ss",
            f"{t:.3f}",
            "-i",
            str(video),
            "-frames:v",
            "1",
            "-q:v",
            "3",
            str(fp),
        ]
        subprocess.run(cmd, capture_output=True, timeout=30)
        if fp.exists():
            paths.append(fp)
    return paths


def ocr_frame(path: Path) -> dict:
    from PIL import Image

    img = Image.open(path)
    W, H = img.size
    area = W * H
    ocr = get_ocr()
    result, _ = ocr(str(path))
    boxes = result or []
    obvious = []
    edge_hits = []
    total_obv = 0.0
    texts = []
    watermark_kw = (
        "pollo", "flova", "capcut", "higgsfield", "seedance", "hailuo",
        "minimax", "kling", "vidu", "runway", "watermark", "subscribe",
        "grok", "imagine", "happyhorse", "happy horse",
    )

    def keep_text(t: str) -> bool:
        t = (t or "").strip()
        if not t:
            return False
        # drop 1–2 glyph texture false positives (★, C, 8, 口)
        compact = re.sub(r"[\s★☆■□●○◆◇※•·\-_|~`'\"“”‘’!！?？.。,，、:：;；]+", "", t)
        if len(compact) < 3:
            return False
        if re.fullmatch(r"[\d\W_]+", compact):
            return False
        return True

    for item in boxes:
        box, text, score = item[0], item[1], float(item[2])
        if not keep_text(text) and not any(k in (text or "").lower() for k in watermark_kw):
            continue
        xs = [p[0] for p in box]
        ys = [p[1] for p in box]
        bw, bh = max(xs) - min(xs), max(ys) - min(ys)
        frac = (bw * bh) / area if area else 0
        cx, cy = (min(xs) + max(xs)) / 2, (min(ys) + max(ys)) / 2
        near_edge = cx < 0.10 * W or cx > 0.90 * W or cy < 0.10 * H or cy > 0.90 * H
        rec = {"text": text, "score": score, "frac": frac, "edge": near_edge}
        texts.append(rec)
        if frac >= 0.006 and score >= 0.45:
            obvious.append(rec)
            total_obv += frac
            if near_edge:
                edge_hits.append(rec)
    marked = total_obv >= 0.015
    huge = total_obv >= 0.04
    joined = " ".join(t["text"] for t in texts).lower()
    brand_wm = any(
        k in joined
        for k in (
            "pollo.ai",
            "flova.ai",
            "capcut",
            "higgsfield",
            "grok imagine",
            "grok.com",
        )
    )
    return {
        "w": W,
        "h": H,
        "n_boxes": len(boxes),
        "total_obv": total_obv,
        "marked": marked or brand_wm,
        "huge": huge,
        "edge_hits": len(edge_hits),
        "texts": [t["text"] for t in texts if t["score"] >= 0.4][:12],
        "brand_wm": brand_wm,
    }


def judge_ocr(frame_reports: list[dict]) -> tuple[str, dict]:
    marked = sum(1 for f in frame_reports if f.get("marked"))
    huge = any(f.get("huge") for f in frame_reports)
    edge = sum(f.get("edge_hits", 0) for f in frame_reports)
    if huge or marked >= 2:
        return "不纯净", {"marked": marked, "huge": huge, "edge": edge}
    if marked == 1 or edge >= 2:
        return "边缘疑似水印", {"marked": marked, "huge": huge, "edge": edge}
    return "纯净", {"marked": marked, "huge": huge, "edge": edge}


def slug_model(m: str) -> str:
    s = m.replace(" ", "-")
    s = re.sub(r"[^A-Za-z0-9.\-]+", "", s)
    return s


def process_one(c: dict, idx: int, results: list, rejects: list, fails: list) -> None:
    handle = c["handle"].lstrip("@")
    model_slug = slug_model(c["model"])
    sid = str(c["id"]).split("-")[0][-6:]
    stem = f"{idx:03d}_{model_slug}_@{handle}_{sid}"
    tweet = f"https://x.com/{handle}/status/{c['id']}"
    print(f"\n[{idx:03d}] @{handle} {c['model']} {c['id']}", flush=True)

    raw = RAW / f"{stem}_src.mp4"
    final = VIDEOS / f"{stem}.mp4"
    ok = False
    if c.get("video_url"):
        ok = download_curl(c["video_url"], raw)
    if not ok:
        ok = download_ytdlp(tweet, raw)
    if not ok:
        fails.append({**c, "reason": "下载失败"})
        print("  FAIL download", flush=True)
        return

    if not raw.exists():
        fails.append({**c, "reason": "下载文件丢失"})
        print("  FAIL missing raw", flush=True)
        return
    dur = ffprobe_duration(raw)
    if dur is None:
        fails.append({**c, "reason": "无法读取时长"})
        print("  FAIL duration", flush=True)
        return
    print(f"  duration={dur:.2f}s size={raw.stat().st_size/1e6:.1f}MB", flush=True)
    if dur < MIN_S or dur > MAX_S:
        rejects.append({**c, "reason": f"实测时长 {dur:.1f}s 不在 8–35s", "measured_s": dur})
        print("  REJECT duration", flush=True)
        raw.unlink(missing_ok=True)
        return

    if not transcode_1080(raw, final):
        fails.append({**c, "reason": "转码失败"})
        return
    raw.unlink(missing_ok=True)

    frames = extract_frames(final, stem, dur)
    reports = []
    try:
        for fp in frames:
            reports.append(ocr_frame(fp))
        purity, ocr_meta = judge_ocr(reports)
    except Exception as e:
        print("  OCR error", e, flush=True)
        purity, ocr_meta = "OCR失败-人工待核", {"error": str(e)}

    print(f"  purity={purity} ocr={ocr_meta}", flush=True)
    if purity == "不纯净":
        rejects.append(
            {
                **c,
                "reason": "OCR判定画面不纯净（字幕/水印/大面积文字）",
                "measured_s": dur,
                "ocr": ocr_meta,
                "frame_texts": [r.get("texts") for r in reports],
            }
        )
        final.unlink(missing_ok=True)
        return

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
    }
    results.append(rec)
    with (META / "accepted.jsonl").open("a") as f:
        f.write(json.dumps(rec, ensure_ascii=False) + "\n")


def main():
    cands = json.loads((META / "candidates.json").read_text())
    # skip already accepted ids
    done = set()
    acc_path = META / "accepted.jsonl"
    if acc_path.exists():
        for line in acc_path.read_text().splitlines():
            if line.strip():
                done.add(json.loads(line)["id"])
    skip_path = META / "skip_ids.json"
    if skip_path.exists():
        done.update(json.loads(skip_path.read_text()))
    rej_path = META / "rejects.json"
    if rej_path.exists():
        try:
            for r in json.loads(rej_path.read_text() or "[]"):
                if isinstance(r, dict) and r.get("id"):
                    done.add(r["id"])
        except Exception:
            pass
    fail_path = META / "fails.json"
    if fail_path.exists():
        try:
            for r in json.loads(fail_path.read_text() or "[]"):
                if isinstance(r, dict) and r.get("id"):
                    done.add(r["id"])
        except Exception:
            pass
    results, rejects, fails = [], [], []
    # preserve historical rejects/fails across runs (this file is overwritten each loop)
    prev_rej, prev_fail = [], []
    if rej_path.exists():
        try:
            prev_rej = json.loads(rej_path.read_text() or "[]") or []
        except Exception:
            prev_rej = []
    if fail_path.exists():
        try:
            prev_fail = json.loads(fail_path.read_text() or "[]") or []
        except Exception:
            prev_fail = []
    n = sum(1 for _ in acc_path.read_text().splitlines() if _.strip()) if acc_path.exists() else 0
    for c in cands:
        if c["id"] in done:
            continue
        n += 1
        try:
            process_one(c, n, results, rejects, fails)
        except Exception as e:
            print("  EXC", e, flush=True)
            fails.append({**c, "reason": f"exception {e}"})
        (META / "rejects.json").write_text(
            json.dumps(prev_rej + rejects, ensure_ascii=False, indent=2)
        )
        (META / "fails.json").write_text(
            json.dumps(prev_fail + fails, ensure_ascii=False, indent=2)
        )
    print(
        f"\nDONE new_ok={len(results)} reject={len(rejects)} fail={len(fails)} total_done_ids={n}",
        flush=True,
    )


if __name__ == "__main__":
    main()
