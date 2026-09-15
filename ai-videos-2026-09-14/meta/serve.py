#!/usr/bin/env python3
"""Catalog gallery server: static files + screening APIs on 0.0.0.0:8080."""
from __future__ import annotations

import json
import shutil
import sys
import threading
from datetime import datetime, timezone
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import parse_qs, urlparse

ROOT = Path("/workspace/ai-videos-2026-09-14")
META = ROOT / "meta"
VIDEOS = ROOT / "videos"
FRAMES = ROOT / "frames"
REMOVED = ROOT / "_removed"
REMOVED_VIDEOS = REMOVED / "videos"
REMOVED_FRAMES = REMOVED / "frames"

sys.path.insert(0, str(META))
import generate_index  # noqa: E402

LOCK = threading.Lock()
HOST = "0.0.0.0"
PORT = 8080


def _mkdirs() -> None:
    for p in (REMOVED_VIDEOS, REMOVED_FRAMES, META):
        p.mkdir(parents=True, exist_ok=True)


def _atomic_write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(text, encoding="utf-8")
    tmp.replace(path)


def _read_jsonl(path: Path) -> list[dict]:
    if not path.exists():
        return []
    rows = []
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        try:
            rows.append(json.loads(line))
        except json.JSONDecodeError:
            continue
    return rows


def _write_jsonl(path: Path, rows: list[dict]) -> None:
    text = "".join(json.dumps(r, ensure_ascii=False) + "\n" for r in rows)
    _atomic_write(path, text)


def _load_skip() -> list[str]:
    p = META / "skip_ids.json"
    if not p.exists():
        return []
    try:
        data = json.loads(p.read_text(encoding="utf-8") or "[]")
    except json.JSONDecodeError:
        return []
    if not isinstance(data, list):
        return []
    return [str(x) for x in data]


def _save_skip(ids: list[str]) -> None:
    _atomic_write(META / "skip_ids.json", json.dumps(ids, ensure_ascii=False, indent=2) + "\n")


def _sid(v) -> str:
    return str(v or "").strip()


def _unique_dest(folder: Path, name: str) -> Path:
    dest = folder / name
    if not dest.exists():
        return dest
    stem = Path(name).stem
    suf = Path(name).suffix
    i = 1
    while True:
        cand = folder / f"{stem}__{i}{suf}"
        if not cand.exists():
            return cand
        i += 1


def _unique_dir(folder: Path, name: str) -> Path:
    dest = folder / name
    if not dest.exists():
        return dest
    i = 1
    while True:
        cand = folder / f"{name}__{i}"
        if not cand.exists():
            return cand
        i += 1


def _slim_removed(row: dict) -> dict:
    handle = (row.get("handle") or "").lstrip("@")
    return {
        "id": _sid(row.get("id")),
        "sell": row.get("sell") or row.get("caption") or "",
        "handle": handle,
        "model": row.get("model") or "",
        "file": row.get("filename") or row.get("file") or "",
        "date": row.get("date") or "",
        "purity": row.get("purity") or "",
        "removed_at": row.get("removed_at") or "",
    }


def snapshot() -> dict:
    rows = generate_index.load_accepted()
    items = generate_index.catalog_items(rows)
    removed = [_slim_removed(r) for r in _read_jsonl(META / "removed.jsonl")]
    # newest first, unique by id
    seen = set()
    uniq = []
    for r in reversed(removed):
        i = r["id"]
        if not i or i in seen:
            continue
        seen.add(i)
        uniq.append(r)
    return {"items": items, "removed": uniq, "count": len(items), "removed_n": len(uniq)}


def regen() -> None:
    try:
        generate_index.main()
    except Exception as exc:
        print("regen failed:", exc, file=sys.stderr)


def remove_item(tid: str) -> tuple[int, dict]:
    tid = _sid(tid)
    if not tid:
        return 400, {"ok": False, "error": "missing id"}
    _mkdirs()
    accepted = _read_jsonl(META / "accepted.jsonl")
    found = None
    kept = []
    for row in accepted:
        if _sid(row.get("id")) == tid:
            if found is None:
                found = row
            # drop duplicates of the same id too
            continue
        kept.append(row)
    if found is None:
        return 404, {"ok": False, "error": "not in catalog"}

    filename = found.get("filename") or ""
    stem = Path(filename).stem if filename else tid
    video_src = VIDEOS / filename if filename else None
    frames_src = FRAMES / stem if stem else None

    skip = _load_skip()
    if tid not in skip:
        skip.append(tid)
        _save_skip(skip)

    _write_jsonl(META / "accepted.jsonl", kept)

    record = dict(found)
    record["removed_at"] = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    record["removed_video"] = ""
    record["removed_frames"] = ""

    video_dst = ""
    frames_dst = ""
    if video_src is not None and video_src.exists() and video_src.is_file():
        dest = _unique_dest(REMOVED_VIDEOS, filename)
        dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.move(str(video_src), str(dest))
        video_dst = str(dest.relative_to(ROOT))
    if frames_src is not None and frames_src.exists() and frames_src.is_dir():
        dest = _unique_dir(REMOVED_FRAMES, stem)
        dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.move(str(frames_src), str(dest))
        frames_dst = str(dest.relative_to(ROOT))
    record["removed_video"] = video_dst
    record["removed_frames"] = frames_dst

    existing = [r for r in _read_jsonl(META / "removed.jsonl") if _sid(r.get("id")) != tid]
    existing.append(record)
    _write_jsonl(META / "removed.jsonl", existing)

    regen()
    snap = snapshot()
    return 200, {
        "ok": True,
        "id": tid,
        "item": generate_index.catalog_items([found])[0] if found.get("filename") else _slim_removed(found),
        "count": snap["count"],
        "removed_n": snap["removed_n"],
    }


def restore_item(tid: str) -> tuple[int, dict]:
    tid = _sid(tid)
    if not tid:
        return 400, {"ok": False, "error": "missing id"}
    _mkdirs()
    removed = _read_jsonl(META / "removed.jsonl")
    found = None
    kept_removed = []
    for row in removed:
        if _sid(row.get("id")) == tid:
            found = row  # last write wins
        else:
            kept_removed.append(row)
    if found is None:
        return 404, {"ok": False, "error": "not in removed"}

    filename = found.get("filename") or ""
    stem = Path(filename).stem if filename else tid

    video_rel = found.get("removed_video") or ""
    frames_rel = found.get("removed_frames") or ""
    video_src = (ROOT / video_rel) if video_rel else (REMOVED_VIDEOS / filename if filename else None)
    frames_src = (ROOT / frames_rel) if frames_rel else (REMOVED_FRAMES / stem if stem else None)

    if filename:
        video_dst = VIDEOS / filename
        if video_src is not None and video_src.exists() and video_src.is_file():
            video_dst.parent.mkdir(parents=True, exist_ok=True)
            if not video_dst.exists():
                shutil.move(str(video_src), str(video_dst))
        frames_dst = FRAMES / stem
        if frames_src is not None and frames_src.exists() and frames_src.is_dir():
            frames_dst.parent.mkdir(parents=True, exist_ok=True)
            if not frames_dst.exists():
                shutil.move(str(frames_src), str(frames_dst))

    accepted = _read_jsonl(META / "accepted.jsonl")
    if not any(_sid(r.get("id")) == tid for r in accepted):
        clean = {k: v for k, v in found.items() if k not in ("removed_at", "removed_video", "removed_frames")}
        accepted.append(clean)
        _write_jsonl(META / "accepted.jsonl", accepted)

    skip = [s for s in _load_skip() if s != tid]
    _save_skip(skip)
    _write_jsonl(META / "removed.jsonl", kept_removed)

    regen()
    snap = snapshot()
    return 200, {"ok": True, "id": tid, "count": snap["count"], "removed_n": snap["removed_n"]}


class Handler(SimpleHTTPRequestHandler):
    protocol_version = "HTTP/1.1"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(ROOT), **kwargs)

    def log_message(self, fmt: str, *args) -> None:
        sys.stderr.write("%s - %s\n" % (self.address_string(), fmt % args))

    def _json(self, status: int, obj: dict) -> None:
        raw = json.dumps(obj, ensure_ascii=False).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Cache-Control", "no-store")
        self.send_header("Content-Length", str(len(raw)))
        self.end_headers()
        self.wfile.write(raw)

    def _read_json(self) -> dict | None:
        try:
            n = int(self.headers.get("Content-Length") or 0)
        except ValueError:
            n = 0
        if n > 65536:
            self._json(413, {"ok": False, "error": "too large"})
            return None
        raw = self.rfile.read(n) if n else b"{}"
        try:
            data = json.loads(raw.decode("utf-8") or "{}")
        except (UnicodeDecodeError, json.JSONDecodeError):
            self._json(400, {"ok": False, "error": "invalid json"})
            return None
        if not isinstance(data, dict):
            self._json(400, {"ok": False, "error": "invalid json"})
            return None
        return data

    def end_headers(self) -> None:
        parsed = urlparse(self.path)
        path = parsed.path
        qs = parse_qs(parsed.query)
        if path in ("/", "/index.html"):
            self.send_header("Cache-Control", "no-store")
        if path.startswith("/videos/") and "dl" in qs:
            name = Path(path).name
            self.send_header("Content-Disposition", f'attachment; filename="{name}"')
            self.send_header("Cache-Control", "no-store")
        super().end_headers()

    def do_GET(self) -> None:  # noqa: N802
        path = urlparse(self.path).path
        if path.startswith("/_removed"):
            self.send_error(404, "Not Found")
            return
        if path == "/api/catalog":
            with LOCK:
                snap = snapshot()
            self._json(200, {"ok": True, **snap})
            return
        if path == "/api/stats":
            with LOCK:
                snap = snapshot()
            self._json(
                200,
                {
                    "ok": True,
                    "count": snap["count"],
                    "removed_n": snap["removed_n"],
                    "models": len({it.get("model") for it in snap["items"] if it.get("model")}),
                },
            )
            return
        if path.startswith("/api/"):
            self._json(404, {"ok": False, "error": "not found"})
            return
        super().do_GET()

    def do_POST(self) -> None:  # noqa: N802
        path = urlparse(self.path).path
        if path not in ("/api/remove", "/api/restore"):
            self._json(404, {"ok": False, "error": "not found"})
            return
        body = self._read_json()
        if body is None:
            return
        tid = _sid(body.get("id"))
        with LOCK:
            if path == "/api/remove":
                status, payload = remove_item(tid)
            else:
                status, payload = restore_item(tid)
        self._json(status, payload)

    def do_OPTIONS(self) -> None:  # noqa: N802
        self.send_response(204)
        self.send_header("Allow", "GET, POST, OPTIONS, HEAD")
        self.end_headers()


def main() -> None:
    _mkdirs()
    ThreadingHTTPServer.allow_reuse_address = True
    httpd = ThreadingHTTPServer((HOST, PORT), Handler)
    print(f"catalog gallery on {HOST}:{PORT}", flush=True)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        httpd.server_close()


if __name__ == "__main__":
    main()
