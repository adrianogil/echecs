from .chesspiece import ChessPiece, ChessBoardColor


class Queen(ChessPiece):
    PIECE_LETTER = 'q'

    def __init__(self, x=-1, y=-1, pos=None, color=ChessBoardColor.WHITE):
        super().__init__(
            piece_type=ChessPiece.QUEEN,
            color=color,
            pos=pos,
            x=x,
            y=y
        )
