"""Unit tests for nflgame.player functionality."""
import os
import pytest
import nflgame


# set up a few pytest fixtures

@pytest.fixture(scope='session')
def players():
    # use a static copy of tests/players.json to ensure values don't change
    jsonf = os.path.join(os.path.dirname(__file__), 'players.json')
    return nflgame.player._create_players(jsonf)


@pytest.fixture(scope='session')
def player(players):
    return players['00-0000045']  # Flozell Adams


@pytest.fixture(scope='session')
def stats(player):
    return player.stats(2010, 3)


@pytest.fixture(scope='session')
def plays(player):
    return player.plays(2010, 3)


def test_players_types(players):
    # verify that players returns a dict ...
    assert isinstance(players, dict)

    # verify that players is comprised of Player objects
    items = [players[k] for k in players]
    assert all(map(lambda x: isinstance(x, nflgame.player.Player), items))


def test_player_attributes(player):
    # verify that player attributes are working
    assert player.gsis_id == '00-0000045'
    assert player.player_id == '00-0000045'
    assert player.gsis_name == 'F.Adams'
    assert player.full_name == 'Flozell Adams'
    assert player.first_name == 'Flozell'
    assert player.last_name == 'Adams'
    assert player.team == ''
    assert player.position == ''
    assert player.profile_id == 2499355
    assert player.profile_url == 'http://www.nfl.com/player/flozelladams/2499355/profile'
    assert player.uniform_number == 0
    assert player.birthdate == '5/18/1975'
    assert player.college == 'Michigan State'
    assert player.height == 79
    assert player.weight == 338
    assert player.years_pro == 13
    assert player.status == ''
    assert player.gsis_id == '00-0000045'
    assert player.playerid == '00-0000045'
    assert player.name == 'Flozell Adams'
    assert player.number == 0

    assert str(player) == 'Flozell Adams (, )'


def test_player_stats_type(stats):
    # verify that player.stats() returns a GamePlayerStats object
    assert isinstance(stats, nflgame.player.GamePlayerStats)


def test_player_plays_type(plays):
    # verify that player.plays() returns a seq.GenPlays object
    assert isinstance(plays, nflgame.seq.GenPlays)
