#!/usr/bin/env bash
# Rebuild THESIS.pdf from THESIS.md + refs/references.md
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"
python3 scripts/md_to_pdf.py
echo "Wrote $ROOT/THESIS.pdf"
