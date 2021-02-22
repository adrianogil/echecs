from echecs.logics.pieces.chesspiece import ChessPiece

import echecs.logics.boardposition as boardposition


def parse_pawn_move(algebraic_notation_str, board, color):
    x, y = board.get_pos(pos=algebraic_notation_str)

    if color == "white":
        piece_obj = board._get_piece(x=x, y=y - 1)
    else:
        piece_obj = board._get_piece(x=x, y=y + 1)

    if piece_obj is None:
        if color == "white" and y == 3:
            # Get pawn from white's initial rank
            piece_obj = board._get_piece(x=x, y=1)
        if color == "black" and y == 4:
            # Get pawn from black's initial rank
            piece_obj = board._get_piece(x=x, y=6)

    if piece_obj.piece_type == ChessPiece.PAWN and piece_obj.color == color:
        return {
            'piece': piece_obj,
            'next_x': x,
            'next_y': y
        }

    return None


def parse_pawn_capture_move(algebraic_notation_str, board, color):
    x, y = board.get_pos(pos=algebraic_notation_str[2:])

    last_x = boardposition.letter_columns.index(algebraic_notation_str[0])

    if color == "white":
        piece_obj = board._get_piece(x=last_x, y=y - 1)
    else:
        piece_obj = board._get_piece(x=last_x, y=y + 1)

    piece_to_be_captured = board._get_piece(x=x, y=y)

    if piece_obj is not None and piece_obj.piece_type == ChessPiece.PAWN and piece_obj.color == color and piece_to_be_captured is not None:
        return {
            'piece': piece_obj,
            'piece_to_be_captured': piece_to_be_captured,
            'next_x': x,
            'next_y': y
        }

    return None
