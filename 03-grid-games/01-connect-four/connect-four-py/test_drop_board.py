from connect_four_game import ConnectFourGame


def display_board(game):
    print("1  2  3  4  5  6  7")
    for row in game.board:
        line = "  ".join(row)
        print(line)


test_drop_board = [
    [".", ".", ".", ".", ".", "O", "."],
    [".", ".", ".", ".", "O", "O", "."],
    [".", ".", ".", "O", "O", "O", "."],
    [".", ".", "O", "O", "O", "O", "."],
    [".", "O", "O", "O", "O", "O", "."]
]


game = ConnectFourGame()
game.board = test_drop_board

token = "X"
for column in range(-2, 10):
    result = game.drop(column, token)
    print("drop in column", column, result)

display_board(game)
