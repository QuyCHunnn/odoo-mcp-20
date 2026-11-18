#!/usr/bin/env bash
set -euo pipefail
TASK_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
cd "$TASK_DIR"
if [[ ! -x "$TASK_DIR/.venv/bin/python" ]]; then
    echo "Missing .venv; follow README.md setup." >&2
    exit 1
fi
exec "$TASK_DIR/.venv/bin/python" -m odoo_mcp "$@"
