from .gameboard import GameBoard


class GameState:
    def __init__(self):
        self.board = GameBoard()

    def print_state(self):
        self.board.print_board()
