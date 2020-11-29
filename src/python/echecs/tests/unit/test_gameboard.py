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


def test_invalid_board_position(gameboard):
    assert gameboard.verify_valid_move('p0', 'w1') == False
    assert gameboard.verify_valid_move('p1', 'i8') == False
    assert gameboard.verify_valid_move('p2', '%6') == False
    assert gameboard.verify_valid_move('p3', 'i9') == False
    assert gameboard.verify_valid_move('p4', 'i9') == False
    assert gameboard.verify_valid_move('p5', 'i9') == False
    assert gameboard.verify_valid_move('p6', 'i9') == False
    assert gameboard.verify_valid_move('p7', 'i9') == False
    assert gameboard.verify_valid_move('p8', 'i9') == False


def test_invalid_pieces(gameboard):
    assert gameboard.verify_valid_move('0p', 'b2') == False
    assert gameboard.verify_valid_move('g1', 'g3') == False
    assert gameboard.verify_valid_move('e3', 'h2') == False
    assert gameboard.verify_valid_move('12', 'j4') == False
    assert gameboard.verify_valid_move('p9', 'a1') == False
    assert gameboard.verify_valid_move('12', 'k2') == False
    assert gameboard.verify_valid_move('34', 'd2') == False
    assert gameboard.verify_valid_move('2', 'c3') == False
    assert gameboard.verify_valid_move('19', 'e6') == False


def test_valid_pieces(gameboard):
    for piece_number in range(8):
        assert gameboard.verify_valid_move('p' + str(piece_number), 'b2')
