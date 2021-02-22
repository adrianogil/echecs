from .chesspiece import ChessPiece, ChessBoardColor


class Knight(ChessPiece):
    PIECE_LETTER = 'n'

    def __init__(self, x=-1, y=-1, pos=None, color=ChessBoardColor.WHITE):
        super().__init__(
            piece_type=ChessPiece.KNIGHT,
            color=color,
            pos=pos,
            x=x,
            y=y
        )
