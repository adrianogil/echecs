
from .pawnmovement import parse_pawn_move, parse_pawn_capture_move
from .knightmovement import parse_knight_move, parse_knight_capture_move

import echecs.logics.boardposition as boardposition


def parse_move(algebraic_notation_str, board, color="white"):

    # === Parse pawn movement ===
    if len(algebraic_notation_str) == 2:
        piece_move = parse_pawn_move(algebraic_notation_str, board, color)
    elif len(algebraic_notation_str) == 4 and algebraic_notation_str[0].islower() and algebraic_notation_str[1] == 'x' and algebraic_notation_str[0] in boardposition.letter_columns:
        piece_move = parse_pawn_capture_move(algebraic_notation_str, board, color)
    # ===========================
    elif len(algebraic_notation_str) == 3:
        # === Parse knight movement ===
        if algebraic_notation_str[0] == 'N':
            piece_move = parse_knight_move(algebraic_notation_str, board, color)
    elif len(algebraic_notation_str) == 4 and algebraic_notation_str[1] == 'x':
        # === Parse knight movement ===
        if algebraic_notation_str[0] == 'N':
            piece_move = parse_knight_capture_move(algebraic_notation_str, board, color)

    return piece_move
