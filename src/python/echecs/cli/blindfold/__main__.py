import chess

board = chess.Board()
print(board)

is_playing = True

while is_playing:
    user_input = input(">> ")
    user_input = user_input.strip()

    if user_input in ["quit", "q"]:
        is_playing = True
        exit()
    if user_input == "show":
        print(board)
    else:
        board.push_san(user_input)
