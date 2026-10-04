#!/usr/bin/env python3
"""
Word Scramble Game
A terminal-based word scramble game with categories, hints, and scoring.
"""

import random
import time

WORDS = {
    "Programming": [
        ("PYTHON", "A popular snake-named language"),
        ("ALGORITHM", "A step-by-step problem solving procedure"),
        ("COMPILER", "Translates high-level code to machine code"),
        ("VARIABLE", "A named storage location in memory"),
        ("FUNCTION", "A reusable block of code"),
        ("DATABASE", "An organized collection of data"),
        ("DEBUGGER", "A tool used to find and fix bugs")
    ],
    "Animals": [
        ("ELEPHANT", "The largest existing land animal"),
        ("DOLPHIN", "An intelligent aquatic mammal"),
        ("CHAMELEON", "A reptile known for changing colors"),
        ("PENGUIN", "A flightless bird living in cold regions"),
        ("KANGAROO", "A marsupial famous for hopping"),
        ("GIRAFFE", "The tallest living terrestrial animal")
    ],
    "Space & Science": [
        ("GALAXY", "A gravitationally bound system of stars"),
        ("TELESCOPE", "An optical instrument for distant objects"),
        ("ASTEROID", "A rocky object orbiting the Sun"),
        ("GRAVITY", "The force that attracts objects toward each other"),
        ("SUPERNOVA", "A powerful and luminous stellar explosion")
    ]
}


def scramble_word(word: str) -> str:
    """Shuffle letters so the scrambled word is not identical to the original."""
    letters = list(word)
    if len(letters) <= 2:
        return "".join(reversed(letters))

    for _ in range(20):
        random.shuffle(letters)
        scrambled = "".join(letters)
        if scrambled != word:
            return scrambled
    return "".join(letters)


def play_round(category: str, word: str, clue: str, max_attempts: int = 3) -> int:
    """Plays one round of the scramble game. Returns points earned."""
    scrambled = scramble_word(word)
    revealed_hint = False

    print("\n" + "=" * 45)
    print(f" Category : {category}")
    print(f" Scramble : {' '.join(scrambled)}")
    print(f" Length   : {len(word)} letters")
    print("=" * 45)
    print("Commands: Type your guess, 'hint' for clue, or 'skip' to give up.\n")

    for attempt in range(1, max_attempts + 1):
        guess = input(f"Attempt {attempt}/{max_attempts} > ").strip().upper()

        if not guess:
            continue

        if guess == "SKIP":
            print(f"Skipped! The word was: {word}")
            return 0

        if guess == "HINT":
            if not revealed_hint:
                print(f"Hint: {clue} (Starts with '{word[0]}')")
                revealed_hint = True
            else:
                print(f"Hint already revealed: {clue}")
            continue

        if guess == word:
            points = 10 if not revealed_hint else 5
            print(f"Correct! You earned {points} points!")
            return points
        else:
            print("Incorrect guess. Try again!")

    print(f"\nOut of attempts! The correct word was: {word}")
    return 0


def main():
    print("*" * 45)
    print("       WELCOME TO THE WORD SCRAMBLE GAME!    ")
    print("*" * 45)

    score = 0
    rounds_played = 0

    while True:
        category = random.choice(list(WORDS.keys()))
        word, clue = random.choice(WORDS[category])

        points = play_round(category, word, clue)
        score += points
        rounds_played += 1

        print(f"\nCurrent Score: {score} pts after {rounds_played} round(s).")
        again = input("\nPlay another round? (y/n): ").strip().lower()
        if again not in ("y", "yes"):
            break

    print("\n" + "=" * 45)
    print(f" GAME OVER! Final Score: {score} across {rounds_played} round(s).")
    print(" Thanks for playing!")
    print("=" * 45 + "\n")


if __name__ == "__main__":
    main()
