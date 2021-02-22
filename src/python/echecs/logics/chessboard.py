from .pieces.pawn import Pawn


class ChessBoard:
    def __init__(self):
        self._board = []
        self.board_size_x = 8
        self.board_size_y = 8

        self.clear_board()

        self.add_piece(x=0, y=1, piece_obj=Pawn(color='white'))

    def add_piece(self, piece_obj, x=None, y=None, pos=None):
        self._board[x][y] = piece_obj
        piece_obj.x = x
        piece_obj.y = y

    def clear_board(self):
        self._board = []

        for x in range(0, self.board_size_x):
            self._board.append([None] * self.board_size_y)

    def __str__(self):
        board_str = ''

        for y in reversed(range(0, self.board_size_y)):
            for x in range(0, self.board_size_x):
                piece = self._board[x][y]
                if piece is None:
                    piece = '.'
                board_str += str(piece) + ' '
            board_str += '\n'

        return board_str

        #     'white': [

        #         ChessPiece(ChessPiece.PAWN, pos='a2', color=ChessBoardColor.WHITE)
        #     ],
        #     'black': {
        #         'p0': 'a7',
        #         'p1': 'b7',
        #         'p2': 'c7',
        #         'p3': 'd7',
        #         'p4': 'e7',
        #         'p5': 'f7',
        #         'p6': 'g7',
        #         'p7': 'h7',
        #         'k': 'e8',
        #         'q': 'd8',
        #         'b0': 'c8',
        #         'b1': 'f8',
        #         'n0': 'b8',
        #         'n1': 'g8',
        #         'r0': 'a8',
        #         'r1': 'h8'
        #     }
        # }

        # self.pieces = {
        #     'white': {
        #         'p0': 'a2',
        #         'p1': 'b2',
        #         'p2': 'c2',
        #         'p3': 'd2',
        #         'p4': 'e2',
        #         'p5': 'f2',
        #         'p6': 'g2',
        #         'p7': 'h2',
        #         'k': 'e1',
        #         'q': 'd1',
        #         'b0': 'c1',
        #         'b1': 'f1',
        #         'n0': 'b1',
        #         'n1': 'g1',
        #         'r0': 'a1',
        #         'r1': 'h1'
        #     },
        #     'black': {
        #         'p0': 'a7',
        #         'p1': 'b7',
        #         'p2': 'c7',
        #         'p3': 'd7',
        #         'p4': 'e7',
        #         'p5': 'f7',
        #         'p6': 'g7',
        #         'p7': 'h7',
        #         'k': 'e8',
        #         'q': 'd8',
        #         'b0': 'c8',
        #         'b1': 'f8',
        #         'n0': 'b8',
        #         'n1': 'g8',
        #         'r0': 'a8',
        #         'r1': 'h8'
        #     }
        # }

    # def add_default_pieces(self):
    #     pass

    # def update_positions(self):
    #     self.positions = {}

    #     for piece_color in ['white', 'black']:
    #         for piece in self.pieces[piece_color]:
    #             position = self.pieces[piece_color][piece]
    #             self.positions[position] = (piece_color[0], piece[0])

    # def print_board(self):
    #     self.update_positions()

    #     for yrow in reversed(['1', '2', '3', '4', '5', '6', '7', '8']):
    #         line_str = ''
    #         for xrow in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']:
    #             line_str += self._get_str_piece(self.positions.get(xrow + yrow, None)) + ' '
    #         print(line_str)


    # def get_pawns(self, color='white'):
    #     pawns_positions = []

    #     for p in range(0, 8):
    #         pawns_positions.append(self.pieces[color]['p' + str(p)])

    #     return pawns_positions

    # def verify_valid_move(self, piece, next_pos):
    #     # Verify if is valid board position
    #     if len(next_pos) != 2:
    #         print('next_pos size different than 2')
    #         return False
    #     next_pos = next_pos.lower()

    #     pos0_letters = next_pos[0] in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    #     pos0_numbers = next_pos[0] in ['1', '2', '3', '4', '5', '6', '7', '8']
    #     pos1_letters = next_pos[1] in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    #     pos1_numbers = next_pos[1] in ['1', '2', '3', '4', '5', '6', '7', '8']

    #     pos_letter = None
    #     pos_number = None

    #     if pos0_letters and pos1_numbers:
    #         pos_letter = next_pos[0]
    #         pos_number = next_pos[1]
    #     elif pos0_numbers and pos1_letters:
    #         pos_number = next_pos[0]
    #         pos_letter = next_pos[1]
    #     else:
    #         print('Valid position should be a1 or 1a')
    #         return False

    #     piece = piece.lower()
    #     if piece not in self.pieces['white']:
    #         return False

    #     return True