class GameBoard:
    def __init__(self):
        self.pieces = {
            'white': {
                'p0': 'a2',
                'p1': 'b2',
                'p2': 'c2',
                'p3': 'd2',
                'p4': 'e2',
                'p5': 'f2',
                'p6': 'g2',
                'p7': 'h2',
                'k': 'e1',
                'q': 'd1',
                'b0': 'c1',
                'b1': 'f1',
                'n0': 'b1',
                'n1': 'g1',
                'r0': 'a1',
                'r1': 'h1'
            },
            'black': {
                'p0': 'a7',
                'p1': 'b7',
                'p2': 'c7',
                'p3': 'd7',
                'p4': 'e7',
                'p5': 'f7',
                'p6': 'g7',
                'p7': 'h7',
                'k': 'e8',
                'q': 'd8',
                'b0': 'c8',
                'b1': 'f8',
                'n0': 'b8',
                'n1': 'g8',
                'r0': 'a8',
                'r1': 'h8'
            }
        }

    def update_positions(self):
        self.positions = {}

        for piece_color in ['white', 'black']:
            for piece in self.pieces[piece_color]:
                position = self.pieces[piece_color][piece]
                self.positions[position] = piece_color[0] + piece[0]

    def print_board(self):
        self.update_positions()

        for yrow in reversed(['1', '2', '3', '4', '5', '6', '7', '8']):
            line_str = ''
            for xrow in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']:
                line_str += self.positions.get(xrow + yrow, '. ') + ' '
            print(line_str)

    def get_pawns(self, color='white'):
        pawns_positions = []

        for p in range(0, 8):
            pawns_positions.append(self.pieces[color]['p' + str(p)])

        return pawns_positions

    def verify_valid_move(self, piece, next_pos):
        # Verify if is valid board position
        if len(next_pos) != 2:
            return False
        next_pos = next_pos.lower()
        if next_pos[0] not in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'] or \
           next_pos[1] not in ['1', '2', '3', '4', '5', '6', '7', '8']:
            return False

        # TODO
