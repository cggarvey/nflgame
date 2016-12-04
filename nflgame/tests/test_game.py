"""Unit tests for nflgame.game functionality."""
import pytest
import nflgame


def test_gameclock_pregame():
    gc = nflgame.game.GameClock('Pregame', '15:00')
    assert gc.is_pregame()
    assert not gc.is_halftime()
    assert not gc.is_final()
    assert gc._minutes == 15
    assert gc._seconds == 0


def test_gameclock_halftime():
    gc = nflgame.game.GameClock('Halftime', '15:00')
    assert not gc.is_pregame()
    assert gc.is_halftime()
    assert not gc.is_final()
    assert gc._minutes == 15
    assert gc._seconds == 0


def test_gameclock_final():
    gc = nflgame.game.GameClock('Final', '15:00')
    assert not gc.is_pregame()
    assert not gc.is_halftime()
    assert gc.is_final()
    assert gc._minutes == 15
    assert gc._seconds == 0


def test_gameclock_error():
    gc = nflgame.game.GameClock('', '')
    assert gc.is_pregame()
    assert not gc.is_halftime()
    assert not gc.is_final()
    assert gc._minutes == 0
    assert gc._seconds == 0


def test_gameclock_comparison_lt_qtr():
    a = nflgame.game.GameClock(3, '2:00')
    b = nflgame.game.GameClock(4, '2:00')
    assert a.__lt__(b)
    assert a.__cmp__(b) < 0
    assert a < b


def test_gameclock_comparison_lt_min():
    a = nflgame.game.GameClock(4, '2:00')
    b = nflgame.game.GameClock(4, '1:00')
    assert a.__lt__(b)
    assert a.__cmp__(b) < 0
    assert a < b


def test_gameclock_comparison_lt_sec():
    a = nflgame.game.GameClock(4, '2:20')
    b = nflgame.game.GameClock(4, '2:15')
    assert a.__lt__(b)
    assert a.__cmp__(b) < 0
    assert a < b


def test_gameclock_comparison_eq():
    a = nflgame.game.GameClock(4, '2:00')
    b = nflgame.game.GameClock(4, '2:00')
    assert b == a


def test_possession_time():
    pt = nflgame.game.PossessionTime('15:00')
    assert pt.total_seconds() == 900


def test_possession_time_lt():
    a = nflgame.game.PossessionTime('1:00')
    b = nflgame.game.PossessionTime('2:00')
    assert a.__lt__(b)
    assert a.__cmp__(b) < 0
    assert a < b


def test_possession_time_eq():
    a = nflgame.game.PossessionTime('1:00')
    b = nflgame.game.PossessionTime('1:00')
    assert a == b


def test_possession_time_add():
    a = nflgame.game.PossessionTime('1:00')
    b = nflgame.game.PossessionTime('1:00')
    c = a + b
    assert isinstance(c, nflgame.game.PossessionTime)
    assert c.total_seconds() == 120


def test_possession_time_sub():
    a = nflgame.game.PossessionTime('3:00')
    b = nflgame.game.PossessionTime('1:00')
    c = a - b
    assert isinstance(c, nflgame.game.PossessionTime)
    assert c.total_seconds() == 120


def test_possession_time_error():
    pt = nflgame.game.PossessionTime(None)
    assert pt.total_seconds() == 0

    pt = nflgame.game.PossessionTime('')
    assert pt.total_seconds() == 0


def test_field_position():
    fp = nflgame.game.FieldPosition(offset=20)
    assert fp.offset == 20
    assert fp.offset < 50


def test_field_position_str():
    a = nflgame.game.FieldPosition(offset=-20)
    assert str(a) == 'OWN 30'
    b = nflgame.game.FieldPosition(offset=0)
    assert str(b) == 'MIDFIELD'
    c = nflgame.game.FieldPosition(offset=20)
    assert str(c) == 'OPP 30'


def test_field_position_add():
    fp1 = nflgame.game.FieldPosition(offset=20)
    fp2 = nflgame.game.FieldPosition(offset=10)
    fp = fp1 + fp2
    assert fp.offset == 30
    assert fp.offset < 50


def test_field_position_add_int():
    fp = nflgame.game.FieldPosition(offset=20)
    fp = fp + 10
    assert fp.offset == 30
    assert fp.offset < 50


def test_field_position_sub():
    a = nflgame.game.FieldPosition(offset=20)
    b = nflgame.game.FieldPosition(offset=10)
    fp = a - b
    assert fp.offset == 10


def test_field_position_sub_int():
    fp = nflgame.game.FieldPosition(offset=20)
    fp = fp - 10
    assert fp.offset == 10


def test_field_position_lt():
    a = nflgame.game.FieldPosition(offset=10)
    b = nflgame.game.FieldPosition(offset=20)
    assert a.__cmp__(b) < 0
    assert a.__lt__(b)
    assert a < b
    assert a + 10 == b


def test_tryint():
    assert nflgame.game._tryint(0) == 0
    assert nflgame.game._tryint(1) == 1
    assert nflgame.game._tryint(None) == 0
    assert nflgame.game._tryint('') == 0

