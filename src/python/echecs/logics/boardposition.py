
letter_columns = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']


def get_position(x=None, y=None, pos=None, board_size_x=8, board_size_y=8):

    if pos is not None:
        if pos.__class__ in [tuple, list] and len(pos) == 2:
            x = pos[0]
            y = pos[1]
        elif pos.__class__ == str and len(pos) == 2 and pos[0] in letter_columns:
            x = letter_columns.index(pos[0])
            y = int(pos[1]) - 1

    if x is not None and x in range(0, board_size_x) and \
       y is not None and y in range(0, board_size_y):
        return (x, y)

    return (-1, -1)
