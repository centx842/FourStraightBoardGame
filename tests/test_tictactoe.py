import pytest
from Resources.TicTacToe_Agent import Players

def test_players_switch_turn():
    players = Players()
    assert players.player == 1, "Initial player should be 1 (Square)"
    players.switch_turn()
    assert players.player == 2, "Should switch to player 2 (Circle)"
    players.switch_turn()
    assert players.player == 1, "Should switch back to player 1 (Square)"

def test_players_reset():
    players = Players()
    players.switch_turn()  # Change to player 2
    assert players.player == 2, "Player should be 2 after switch"
    players.reset_player()
    assert players.player == 1, "Player should reset to 1 (Square)"