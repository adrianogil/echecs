
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

    PIECE_LETTER = 'a'

    def __init__(self, piece_type=None, x=-1, y=-1, pos=None, color=ChessBoardColor.WHITE):
        self.piece_type = piece_type
        self.x = x
        self.y = y
        self.color = color

        self._board = None

    @property
    def pos(self):
        return self.x, self.y

    @pos.setter
    def pos(self, new_pos):
        self.x = new_pos[0]
        self.y = new_pos[1]

    def __str__(self):
        if self.color == ChessBoardColor.WHITE:
            return self.PIECE_LETTER.lower()

        return self.PIECE_LETTER.upper()

