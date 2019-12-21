from connect_four_game import ConnectFourGame


def display_board(game):
    print()
    print("1  2  3  4  5  6  7")
    for row in game.board:
        line = "  ".join(row)
        print(line)


def prompt_player(game):
    player = game.get_current_player()
    print("%s: make a move: " % player, end="")
    column = int(input()) - 1
    return column


def display_winner(game):
    display_board(game)
    if game.winner is None:
        print("CATS! The game ended in a tie.")
    else:
        print(game.winner, "won!")


def main():
    game = ConnectFourGame()
    while not game.is_game_over:
        display_board(game)
        column = prompt_player(game)
        game.make_move(column)
    display_winner(game)


main()
