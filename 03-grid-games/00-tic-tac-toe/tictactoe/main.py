from tic_tac_toe_game import TicTacToeGame


def display_board(game):
    # [f(x) if condition else g(x) for x in sequence]
    q, w, e = [' ' if mark is None else mark for mark in game.board[0]]
    a, s, d = [' ' if mark is None else mark for mark in game.board[1]]
    z, x, c = [' ' if mark is None else mark for mark in game.board[2]]

    lines = [
        "",
        " %s | %s | %s   q w e" % (q, w, e),
        "---+---+---",
        " %s | %s | %s   a s d" % (a, s, d),
        "---+---+---",
        " %s | %s | %s   z x c" % (z, x, c)
    ]

    for line in lines:
        print(line)


def letter_to_coordinate(letter):
    mapping = {
        "q": (0, 0), "w": (0, 1), "e": (0, 2),
        "a": (1, 0), "s": (1, 1), "d": (1, 2),
        "z": (2, 0), "x": (2, 1), "c": (2, 2),
    }
    if letter in mapping:
        return mapping[letter]
    return None


def prompt_player(game):
    player = game.get_current_player()

    prompt = "%s: enter your move: " % player
    print(prompt, end="")

    letter = input()
    coordinate = letter_to_coordinate(letter)
    return coordinate


def display_winner(game):
    display_board(game)
    if game.winner in game.players:
        print("%s wins!" % game.winner)
    else:
        print("CATS! The game ended in a tie.")


def main():
    game = TicTacToeGame()

    while not game.is_game_over:
        display_board(game)
        choice = prompt_player(game)
        if choice is None:
            print("Invalid choice! Enter a letter.")
        else:
            row, col = choice
            game.make_move(row, col)

    display_winner(game)


main()
