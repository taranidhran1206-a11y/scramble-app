<img width="500" height="500" alt="image-removebg-preview (5)" src="https://github.com/user-attachments/assets/65995ea3-5592-4cbd-9878-ca32bf202f7f" />
 Word Scramble Game (Web & CLI)

An interactive Word Scramble game featuring both a **Modern React Web App** and a **Python Terminal CLI Game**.

---

## 🌐 1. React Web App

Interactive browser game with a vibrant turquoise-and-sky-blue design.

### Features
- **Modern React 18 UI**: Responsive design with Tailwind CSS.
- **Automatic Clue Display**: Helpful clue banner automatically presented for every word.
- **Extra Hint System**: Optional first-letter reveal button.
- **Synthesized Audio**: Web Audio API sound effects (correct chime, error buzzer, shuffle whoosh, tile click) without external audio files.
- **Celebration Effects**: Confetti cannon animation on successful word solve.
- **Multiple Categories**: Tech & Code, Animals, Space & Science, Everyday.
- **Speed Bonus & Streaks**: 30-second timer bonus, streak multiplier, and local high score tracking.
- **Keyboard Support**: Play using on-screen interactive letter tiles or your device keyboard.

### Launching the Web Game
```bash
# Option A: One-click launcher
./start.sh

# Option B: Python HTTP server
python3 -m http.server 8080
```
Open **`http://localhost:8080`** in your browser.

---

## 💻 2. Python Terminal Game (`scramble_game.py`)

Play the word scramble directly in your terminal console!

### How to Run
```bash
python3 scramble_game.py
```
Commands during play:
- Type your guess and press **Enter**
- Type `hint` for category clue and first letter
- Type `skip` to reveal the word and move to the next
