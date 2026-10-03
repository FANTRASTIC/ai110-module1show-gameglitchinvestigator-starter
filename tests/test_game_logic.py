from logic_utils import (
    check_guess,
    get_range_for_difficulty,
    parse_guess,
)

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"
    assert message == "🎉 Correct!"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"
    assert message == "📉 Go LOWER!"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"
    assert message == "📈 Go HIGHER!"


def test_difficulty_ranges():
    assert get_range_for_difficulty("Easy") == (1, 20)
    assert get_range_for_difficulty("Normal") == (1, 100)
    assert get_range_for_difficulty("Hard") == (1, 50)


def test_parse_guess_accepts_integer():
    assert parse_guess("42") == (True, 42, None)


def test_parse_guess_rejects_non_number():
    assert parse_guess("not a number") == (False, None, "That is not a number.")


def test_parse_guess_requires_input():
    assert parse_guess("") == (False, None, "Enter a guess.")
