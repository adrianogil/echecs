from .chesspiece import ChessPiece, ChessBoardColor


class King(ChessPiece):
    PIECE_LETTER = 'k'

    def __init__(self, x=-1, y=-1, pos=None, color=ChessBoardColor.WHITE):
        super().__init__(
            piece_type=ChessPiece.KING,
            color=color,
            pos=pos,
            x=x,
            y=y
        )
