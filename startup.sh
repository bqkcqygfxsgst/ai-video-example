#!/bin/sh
# Serve the local AI-video catalog (static + screening APIs) on 0.0.0.0:8080
set -eu
ROOT="/workspace/ai-videos-2026-09-14"
cd "$ROOT"

if curl -sf -o /dev/null --max-time 2 http://127.0.0.1:8080/api/stats; then
  exit 0
fi

python3 - <<'PY'
import os, signal, time
kill_ids = []
for pid in os.listdir("/proc"):
    if not pid.isdigit():
        continue
    try:
        cmd = open(f"/proc/{pid}/cmdline", "rb").read().replace(b"\x00", b" ").decode()
    except Exception:
        continue
    if "http.server 8080" in cmd or "meta/serve.py" in cmd:
        kill_ids.append(int(pid))
me = os.getpid()
ppid = os.getppid()
for pid in kill_ids:
    if pid in (me, ppid):
        continue
    try:
        os.kill(pid, signal.SIGTERM)
    except (ProcessLookupError, PermissionError):
        pass
if kill_ids:
    time.sleep(0.45)
    for pid in kill_ids:
        if pid in (me, ppid):
            continue
        try:
            os.kill(pid, signal.SIGKILL)
        except (ProcessLookupError, PermissionError):
            pass
print("stopped", kill_ids, flush=True)
PY

if [ -f "$ROOT/meta/generate_index.py" ]; then
  python3 "$ROOT/meta/generate_index.py" >/tmp/gen-index.log 2>&1 || true
fi

python3 "$ROOT/meta/serve.py" >/tmp/catalog-http.log 2>&1 &
sleep 0.6
curl -sf -o /dev/null --max-time 3 http://127.0.0.1:8080/api/stats || true
exit 0
