from .chesspiece import ChessPiece, ChessBoardColor


class Bishop(ChessPiece):
    PIECE_LETTER = 'b'

    def __init__(self, x=-1, y=-1, pos=None, color=ChessBoardColor.WHITE):
        super().__init__(
            piece_type=ChessPiece.BISHOP,
            color=color,
            pos=pos,
            x=x,
            y=y
        )
