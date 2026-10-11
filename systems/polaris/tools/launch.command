#!/bin/zsh
cd "$(dirname "$0")/.." || exit 1
python3 -m http.server 8768 --bind 127.0.0.1
