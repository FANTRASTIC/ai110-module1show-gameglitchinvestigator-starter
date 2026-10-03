def get_range_for_difficulty(difficulty: str):
    """Return the inclusive guessing range for a difficulty."""
    if difficulty == "Easy":
        return 1, 20
    if difficulty == "Normal":
        return 1, 100
    if difficulty == "Hard":
        return 1, 50
    return 1, 100


def parse_guess(raw: str | None):
    """Parse user input into an integer guess."""
    if raw is None or raw == "":
        return False, None, "Enter a guess."

    try:
        if "." in raw:
            value = int(float(raw))
        else:
            value = int(raw)
    except (ValueError, TypeError, OverflowError):
        return False, None, "That is not a number."

    return True, value, None


def check_guess(guess: int, secret: int):
    """Return the outcome label and matching hint for a guess."""
    # FIX: AI-assisted extraction keeps the result and directional hint consistent.
    if guess == secret:
        return "Win", "🎉 Correct!"
    if guess > secret:
        return "Too High", "📉 Go LOWER!"
    return "Too Low", "📈 Go HIGHER!"


def update_score(current_score: int, outcome: str, attempt_number: int):
    """Update the score based on the outcome and attempt number."""
    if outcome == "Win":
        points = max(10, 100 - 10 * (attempt_number + 1))
        return current_score + points

    if outcome == "Too High":
        if attempt_number % 2 == 0:
            return current_score + 5
        return current_score - 5

    if outcome == "Too Low":
        return current_score - 5

    return current_score
