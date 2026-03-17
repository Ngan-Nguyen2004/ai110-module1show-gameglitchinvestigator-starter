import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from logic_utils import check_guess, is_guess_in_range

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"
    assert message == "🎉 Correct!"


def test_guess_in_range():
    assert is_guess_in_range(1, 1, 100)
    assert is_guess_in_range(50, 1, 100)
    assert is_guess_in_range(100, 1, 100)


def test_guess_out_of_range():
    assert not is_guess_in_range(0, 1, 100)
    assert not is_guess_in_range(101, 1, 100)

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
