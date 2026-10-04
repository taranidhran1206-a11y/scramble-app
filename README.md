# 🧩 Word Scramble Master (React Web App)

An interactive, responsive Word Scramble game website built with React 18 and styled with Tailwind CSS.

## Features
- **Modern React Architecture**: Pure React component with stateful tile picking, word bank, and guess validation.
- **Interactive Tiles**: Click on letter tiles or type directly with your device's keyboard.
- **Web Audio FX**: Synthesized chime, buzz, shuffle, and click sound effects via the Web Audio API (no external audio assets required).
- **Celebration Effects**: Confetti cannon animation on successful solve.
- **Multiple Categories**: Tech & Code, Animals, Space & Science, Everyday.
- **Multi-stage Hints**: Clue description followed by starting letter reveal.
- **Timer & Streaks**: Optional 30s countdown timer with speed bonus scoring, and win streak tracking.
- **High Score**: Preserved in browser `localStorage`.

## Quick Start
To launch the server and open the game in your browser:
```bash
cd ~/scramble-game-web
./start.sh
```
Or manually run:
```bash
python3 -m http.server 8080 --directory ~/scramble-game-web
```
Then visit: `http://localhost:8080`
