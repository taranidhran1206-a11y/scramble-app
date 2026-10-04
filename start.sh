#!/bin/bash
PORT=8080
echo "=================================================="
echo " 🧩 Word Scramble React Web App"
echo " Serving at: http://localhost:$PORT"
echo " Press Ctrl+C to stop the server"
echo "=================================================="

# Automatically open in your device's browser
if command -v termux-open-url >/dev/null 2>&1; then
  (sleep 1 && termux-open-url "http://localhost:$PORT") &
elif command -v termux-open >/dev/null 2>&1; then
  (sleep 1 && termux-open "http://localhost:$PORT") &
elif command -v xdg-open >/dev/null 2>&1; then
  (sleep 1 && xdg-open "http://localhost:$PORT") &
fi

python3 -m http.server "$PORT"
