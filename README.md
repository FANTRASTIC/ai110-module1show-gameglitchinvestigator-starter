# 🎮 Game Glitch Investigator: The Impossible Guesser

## Purpose

This Streamlit number-guessing game lets a player choose a difficulty, guess
the secret number, receive higher/lower hints, and earn a score.

## Fixes

- Moved range selection, guess parsing, guess comparison, and score calculation
  into `logic_utils.py`.
- Corrected higher/lower hints and removed the string-versus-integer comparison
  workaround.
- Made a new game reset its secret, score, attempts, history, and win/loss
  status; changing difficulty starts a game in the selected range.
- Invalid input now reports an error without using an attempt.

## Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the game: `python -m streamlit run app.py`
3. Run the logic tests: `python -m pytest tests/test_game_logic.py -q`

## Bug Notes

The starter `logic_utils.py` contained `NotImplementedError` placeholders. The
reported pytest run showed all three initial guess-comparison tests failing at
`check_guess`. The original comparison code also paired "Too High" with "Go
HIGHER" and "Too Low" with "Go LOWER". The original New Game button changed the
secret and attempts but left the score/history/status unchanged and always
selected a number from 1 to 100, regardless of difficulty.

## Demo Walkthrough

1. Choose Normal difficulty; the game shows a range of 1 to 100.
2. For a game whose secret is 50, enter 40; the game says "Too Low" and
   "Go HIGHER!"
3. Enter 60; the game says "Too High" and "Go LOWER!"
4. Enter 50; the game reports a win and displays the final score.
5. Select New Game; the game starts fresh with reset score, attempts, history,
   and status. The secret remains available in Developer Debug Info for testing.

## 🧪 Test Results

```
Initial run (before adding the range and input-parsing tests):
...                                                                    [100%]
3 passed in 0.05s
```

The expanded test file now contains seven tests. Its final result has not yet
been captured; run the command in Setup to verify the latest changes.

## Document Your Experience

The investigation and fixes are recorded in [reflection.md](./reflection.md).
