from echecs.logics.pieces.chesspiece import ChessPiece


def parse_knight_move(algebraic_notation_str, board, color):
    x, y = board.get_pos(pos=algebraic_notation_str[1:])

    possible_positions = [
        [-2,  1],
        [-1,  2],
        [ 2,  1],
        [ 1,  2],
        [-2, -1],
        [-1, -2],
        [ 2, -1],
        [ 1, -2],
    ]

    for pos in possible_positions:
        piece_obj = board._get_piece(x=x + pos[0], y=y + pos[1])

        if piece_obj is not None and piece_obj.piece_type == ChessPiece.KNIGHT and piece_obj.color == color:
            break

    if piece_obj is not None:
        return {
            'piece': piece_obj,
            'next_x': x,
            'next_y': y
        }

    return None


def parse_knight_capture_move(algebraic_notation_str, board, color):
    algebraic_notation_str = algebraic_notation_str[0] + algebraic_notation_str[2:]
    piece_move = parse_knight_move(algebraic_notation_str, board, color)

    if piece_move is not None:
        next_x = piece_move['next_x']
        next_y = piece_move['next_y']

        piece_to_be_captured = board._get_piece(x=next_x, y=next_y)

        if piece_to_be_captured is None or piece_to_be_captured.color == color:
            return None

        piece_move['piece_to_be_captured'] = piece_to_be_captured

    return piece_move
