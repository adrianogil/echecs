
class ChessBoardColor:
    WHITE = 'white'
    BLACK = 'black'


class ChessPiece:
    PAWN = 1
    BISHOP = 2
    KNIGHT = 3
    ROOK = 4
    QUEEN = 5
    KING = 6

    PIECE_LETTER='a'

    def __init__(self, piece_type=None, x=-1, y=-1, pos=None, color=ChessBoardColor.WHITE):
        self.piece_type = piece_type
        self.x = x
        self.y = y
        self.color = color

        self._board = None
        # if pos is not None:

    def __str__(self):
        if self.color == ChessBoardColor.WHITE:
            return self.PIECE_LETTER.lower()

        return self.PIECE_LETTER.upper()

