#!/usr/bin/env bash
# Simple wrapper to run the Python package from this directory
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"
python3 -m ytloader "$@"
