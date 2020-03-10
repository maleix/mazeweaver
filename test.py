"""
Some pytests to check that levels are compliant
"""

import re
import pytest

from levels import LEVELS, SONGS, LEVEL_TIMER


def test_level_length():
    for level in LEVELS:
        # assert each line has the same length
        first_line_length = len(level[0])
        for line in level:
            assert first_line_length == len(line)


def test_level_walls():
    # assert all borders are walls
    for level in LEVELS:
        assert re.match(r"^W*$", level[0])
        assert re.match(r"^W*$", level[-1])
        for line in level:
            assert re.match(r"^W.*W$", line)


def test_level_player():
    # check there is at least one player
    for level in LEVELS:
        assert "1" in str(level)


def test_exit():
    for level in LEVELS:
        assert "E" in str(level)


def test_supported_words():
    # ensure all characters
    for level in LEVELS:
        for line in level:
            for char in line:
                assert char in [" ", "E", "W"] or char.isdigit()


def test_enough_songs():
    assert len(SONGS) >= len(LEVELS)


def test_enough_timers():
    assert len(LEVEL_TIMER) >= len(LEVELS)
