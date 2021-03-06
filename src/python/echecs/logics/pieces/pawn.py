from .chesspiece import ChessPiece, ChessBoardColor


class Pawn(ChessPiece):
    PIECE_LETTER = 'p'

    def __init__(self, x=-1, y=-1, pos=None, color=ChessBoardColor.WHITE):
        super().__init__(
            piece_type=ChessPiece.PAWN,
            color=color,
            pos=pos,
            x=x,
            y=y
        )
