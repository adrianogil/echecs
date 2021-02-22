from .pieces.pawn import Pawn
from .pieces.king import King
from .pieces.queen import Queen
from .pieces.rook import Rook
from .pieces.knight import Knight
from .pieces.bishop import Bishop
from .boardposition import get_position

from .algebraicnotation.parsenotation import parse_move


class ChessBoard:
    def __init__(self):
        self._board = []
        self.board_size_x = 8
        self.board_size_y = 8

        self.reset_board()

    def reset_board(self):
        self.clear_board()
        self.add_piece(pos="a2", piece_obj=Pawn(color="white"))
        self.add_piece(pos="b2", piece_obj=Pawn(color="white"))
        self.add_piece(pos="c2", piece_obj=Pawn(color="white"))
        self.add_piece(pos="d2", piece_obj=Pawn(color="white"))
        self.add_piece(pos="e2", piece_obj=Pawn(color="white"))
        self.add_piece(pos="f2", piece_obj=Pawn(color="white"))
        self.add_piece(pos="g2", piece_obj=Pawn(color="white"))
        self.add_piece(pos="h2", piece_obj=Pawn(color="white"))

        self.add_piece(pos="a1", piece_obj=Rook(color="white"))
        self.add_piece(pos="b1", piece_obj=Knight(color="white"))
        self.add_piece(pos="c1", piece_obj=Bishop(color="white"))
        self.add_piece(pos="d1", piece_obj=Queen(color="white"))
        self.add_piece(pos="e1", piece_obj=King(color="white"))
        self.add_piece(pos="f1", piece_obj=Bishop(color="white"))
        self.add_piece(pos="g1", piece_obj=Knight(color="white"))
        self.add_piece(pos="h1", piece_obj=Rook(color="white"))

        self.add_piece(pos="a7", piece_obj=Pawn(color="black"))
        self.add_piece(pos="b7", piece_obj=Pawn(color="black"))
        self.add_piece(pos="c7", piece_obj=Pawn(color="black"))
        self.add_piece(pos="d7", piece_obj=Pawn(color="black"))
        self.add_piece(pos="e7", piece_obj=Pawn(color="black"))
        self.add_piece(pos="f7", piece_obj=Pawn(color="black"))
        self.add_piece(pos="g7", piece_obj=Pawn(color="black"))
        self.add_piece(pos="h7", piece_obj=Pawn(color="black"))

        self.add_piece(pos="a8", piece_obj=Rook(color="black"))
        self.add_piece(pos="b8", piece_obj=Knight(color="black"))
        self.add_piece(pos="c8", piece_obj=Bishop(color="black"))
        self.add_piece(pos="d8", piece_obj=Queen(color="black"))
        self.add_piece(pos="e8", piece_obj=King(color="black"))
        self.add_piece(pos="f8", piece_obj=Bishop(color="black"))
        self.add_piece(pos="g8", piece_obj=Knight(color="black"))
        self.add_piece(pos="h8", piece_obj=Rook(color="black"))

    def get_pos(self, x=None, y=None, pos=None):
        return get_position(
            x=x,
            y=y,
            pos=pos,
            board_size_x=self.board_size_x,
            board_size_y=self.board_size_y,
        )

    def add_piece(self, piece_obj, x=None, y=None, pos=None):
        x, y = self.get_pos(x=x, y=y, pos=pos)
        self._board[x][y] = piece_obj
        piece_obj.x = x
        piece_obj.y = y
        piece_obj._board = self

    def clear_board(self):
        self._board = []

        for x in range(0, self.board_size_x):
            self._board.append([None] * self.board_size_y)

    def __str__(self):
        board_str = ""

        for y in reversed(range(0, self.board_size_y)):
            for x in range(0, self.board_size_x):
                piece = self._board[x][y]
                if piece is None:
                    piece = "."
                board_str += str(piece) + " "
            board_str += "\n"

        return board_str

    def move(self, algebraic_notation_str, color="white"):
        piece_move = parse_move(algebraic_notation_str, color=color, board=self)

        if piece_move is not None:
            piece_obj = piece_move['piece']
            next_x = piece_move['next_x']
            next_y = piece_move['next_y']
            if 'piece_to_be_captured' in piece_move:
                captured_piece = piece_move['piece_to_be_captured']
                print('Captured piece %s at %s' % (captured_piece, captured_piece.pos))
            self._move_piece(piece_obj, x=next_x, y=next_y)

    def _move_piece(self, piece_obj, x=None, y=None, pos=None):
        x, y = self.get_pos(x=x, y=y, pos=pos)
        last_x, last_y = piece_obj.pos
        self._board[last_x][last_y] = None
        self._board[x][y] = piece_obj
        piece_obj.pos = (x, y)

    def _get_piece(self, x=None, y=None, pos=None):
        x, y = self.get_pos(x=x, y=y, pos=pos)
        return self._board[x][y]

    # def get_pawns(self, color='white'):
    #     pawns_positions = []

    #     for p in range(0, 8):
    #         pawns_positions.append(self.pieces[color]['p' + str(p)])

    #     return pawns_positions

    # def verify_valid_move(self, piece, next_pos):
    #     # Verify if is valid board position
    #     if len(next_pos) != 2:
    #         print('next_pos size different than 2')
    #         return False
    #     next_pos = next_pos.lower()

    #     pos0_letters = next_pos[0] in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    #     pos0_numbers = next_pos[0] in ['1', '2', '3', '4', '5', '6', '7', '8']
    #     pos1_letters = next_pos[1] in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    #     pos1_numbers = next_pos[1] in ['1', '2', '3', '4', '5', '6', '7', '8']

    #     pos_letter = None
    #     pos_number = None

    #     if pos0_letters and pos1_numbers:
    #         pos_letter = next_pos[0]
    #         pos_number = next_pos[1]
    #     elif pos0_numbers and pos1_letters:
    #         pos_number = next_pos[0]
    #         pos_letter = next_pos[1]
    #     else:
    #         print('Valid position should be a1 or 1a')
    #         return False

    #     piece = piece.lower()
    #     if piece not in self.pieces['white']:
    #         return False

    #     return True
