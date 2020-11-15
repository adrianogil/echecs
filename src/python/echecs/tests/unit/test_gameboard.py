from echecs.game.gameboard import GameBoard

import pytest


@pytest.fixture
def gameboard():
    '''Return a gameboard'''
    return GameBoard()


def test_pawn_positions_getter(gameboard):
    white_pawns = gameboard.get_pawns('white')
    assert len(white_pawns) == 8

    black_pawns = gameboard.get_pawns('black')
    assert len(black_pawns) == 8


def test_pawn_initial_positions(gameboard):
    white_pawns = gameboard.get_pawns('white')
    for pawn_pos in white_pawns:
        assert int(pawn_pos[1]) == 2

    black_pawns = gameboard.get_pawns('black')
    for pawn_pos in black_pawns:
        assert int(pawn_pos[1]) == 7
