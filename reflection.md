# 💭 Reflection: Game Glitch Investigator

## 1. What was broken when I started

I ran the pytest and the output was: all three guess tests raised `NotImplementedError` from `check_guess` in `logic_utils.py`. Reading the starter comparison logic also showed that its high/low hint messages were reversed, and its New Game handler failed to reset all game state.

**Bug Reproduction Log**

| Input / Trigger | Expected Behavior | Actual Behavior in Starter | Console Error / Output | Suspected Code Location |
|---|---|---|---|---|
| The test calls `check_guess(50, 50)` | Return a win outcome and message | The starter helper raised `NotImplementedError` | `NotImplementedError: Refactor this function from app.py into logic_utils.py`; user-reported original run: 3 failed | `logic_utils.py`, `check_guess` |
| Secret is 50; submit guess 60, then 40 | 60 should say "Too High / Go LOWER"; 40 should say "Too Low / Go HIGHER" | The original comparison paired "Too High" with "Go HIGHER" and "Too Low" with "Go LOWER" | No console error; wrong hint text | Original `check_guess` logic in `app.py` |
| Finish a round and click "New Game", or start a new game on Hard | Reset score, attempts, history, and status; use the selected difficulty's range | The original handler reset only attempts and secret, chose 1–100 for every difficulty, and could preserve a finished status | No console error; stale game state or a secret outside the selected range | `app.py`, New Game handler |

These reproduction steps identify the starter-code behavior. I did not run the live app to independently observe the UI, so that manual check remains to be done.

## 2. How I used AI as a teammate

I used the AI assistant in this coding conversation. One useful suggestion was to test the `(outcome, message)` pair returned by `check_guess`, matching the app's unpacking call; the user then reported that the original three pytest cases passed. An absolute path suggested for running pytest did not work in the restricted shell, so I changed to `python -m pytest` from the activated project environment; the user confirmed the command ran successfully. I reviewed the helper implementation and added further tests for the difficulty ranges and input parsing.

## 3. Debugging and testing my fixes

I used the exception in the user's traceback to locate the unimplemented function, then compared its callers and the original game logic before changing the return behavior. The user reported `3 passed in 0.05s` for the initial win, too-high, and too-low tests after the helper was implemented. I subsequently added tests for difficulty ranges and input parsing, but have not run those newer tests or manually checked the Streamlit app; the project command to run next is `python -m pytest tests/test_game_logic.py -q`. The tests were designed to check both the outcome and the user-visible hint, rather than only checking that the function returned without raising.

## 4. What I learned about Streamlit and state

Streamlit reruns the Python script when a user interacts with a widget instead of continuing from the exact line where execution paused. Values in `st.session_state` survive those reruns for the current browser session, which is how the game can keep the secret, score, and history between guesses. A deliberate New Game action must reset those values; changing difficulty should also start a game whose secret matches the selected range.

## 5. Looking ahead: my developer habits

I want to reuse the habit of turning each bug into a small, repeatable test and checking the exact user-visible result. Next time I would verify the current directory and active Python environment before asking an AI assistant for a command to run. This project reminded me that generated code needs to be checked against its callers and exercised with tests; plausible-looking code is not evidence that a game behaves correctly.
