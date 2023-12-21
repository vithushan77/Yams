# test_yams.py
import pytest

from yams import roll_dice, is_yams, is_brelan, is_carre, is_full, is_grande_suite, is_chance

def test_is_yams():
    assert is_yams(roll_dice(0)) == 50

def test_is_brelan():
    assert is_brelan(roll_dice(7)) == 1

def test_is_carre():
    assert is_carre(roll_dice(1)) == 1


def test_is_full():
    assert is_full(roll_dice(2))


def test_is_grande_suite():
    assert is_grande_suite(roll_dice(5))
    assert is_grande_suite(roll_dice(6))

def test_score_chance():
    assert is_chance([1, 2, 3, 4, 5]) == 15
    assert is_chance([6, 6, 6, 6, 6]) == 30
    assert is_chance([2, 2, 2, 2, 2]) == 10