"""Unit tests for nflgame.statmap."""

import pytest
import nflgame.statmap


def test_statmap_values_basic_yds():
    result = nflgame.statmap.values(21, 99)
    assert result['receiving_yds'] == 99
    assert result['receiving_rec'] == 1


def test_statmap_values_basic_count():
    result = nflgame.statmap.values(2, 99)
    assert result['punting_blk'] == 1


def test_statmap_values_bad_category():
    # verify error raised by passing in an invalid category_id
    with pytest.raises(AssertionError):
        nflgame.statmap.values(-1, 0)


def test_statmap_values_typeerror():
    # verify no error raised by passing in None value
    result = nflgame.statmap.values(21, None)
    assert result['receiving_yds'] == 0
    assert result['receiving_rec'] == 1


def test_statmap_values_valueeerror():
    # verify no error raised by passing in str
    result = nflgame.statmap.values(21, 'bigly')
    assert result['receiving_yds'] == 0
    assert result['receiving_rec'] == 1
