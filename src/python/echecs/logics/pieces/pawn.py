from . import ChessPiece, ChessBoardColor

class Pawn(ChessPiece):
    def __init__(self, x=-1, y=-1, pos=None, color=ChessBoardColor.WHITE):
        super().__init__(
            piece_type=ChessPiece.PAWN,
            color=color,
            pos=pos,
            x=x,
            y=y
        )

    def __str__(self):
        if self.color == ChessBoardColor.WHITE:
            return 'p'

        return 'P'
