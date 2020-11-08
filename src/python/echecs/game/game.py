from .gamestate import GameState


class Game:
    def __init__(self):
        self.game_state = GameState()

    def show_board(self):
        self.game_state.print_board()
