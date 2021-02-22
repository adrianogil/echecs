from .chesspiece import ChessPiece, ChessBoardColor


class Rook(ChessPiece):
    PIECE_LETTER = 'r'

    def __init__(self, x=-1, y=-1, pos=None, color=ChessBoardColor.WHITE):
        super().__init__(
            piece_type=ChessPiece.ROOK,
            color=color,
            pos=pos,
            x=x,
            y=y
        )
