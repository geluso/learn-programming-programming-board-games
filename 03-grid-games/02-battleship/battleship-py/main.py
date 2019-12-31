from battleship_game import BattleshipGame
from util import direction_to_dx_dy


def display_board(game):
    print()
    print("Ships left:")
    print("X: 2[  ] 3[   ] 3[   ] 4[    ] 5[     ]")
    print("O: 2[  ] 3[   ] 3[   ] 4[    ] 5[     ]")
    print()
    print("   1  2  3  4  5  6  7  8  9  ")

    rows = list("ABCDEFGH")
    for letter, row in zip(rows, game.board):
        line = letter + "  "
        line += "  ".join(row) + "  " + letter
        print(line)


def display_placement_preview(game, ship, irow, icol, direction):
    print()
    print("Ships left:")
    print("X: 2[  ] 3[   ] 3[   ] 4[    ] 5[     ]")
    print("O: 2[  ] 3[   ] 3[   ] 4[    ] 5[     ]")
    print()
    print("   1  2  3  4  5  6  7  8  9  ")

    # set
    dx, dy = direction_to_dx_dy(direction)
    for n in range(ship):
        drow = irow + dy * n
        dcol = icol + dx * n
        game.board[drow][dcol] = str(ship)

    rows = list("ABCDEFGH")
    for letter, row in zip(rows, game.board):
        line = letter + "  "
        line += "  ".join(row) + "  " + letter
        print(line)

    # unset
    for n in range(ship):
        drow = irow + dy * n
        dcol = icol + dx * n
        game.board[drow][dcol] = "."


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


def prompt_player_ship(game):
    print("Select a ship (2,3,3,4,5): ", end="")
    ship = int(input())
    return ship


def prompt_player_location(game):
    is_valid = False
    while not is_valid:
        print("Enter a location (B4): ", end="")
        location = input()
        if len(location) != 2:
            print("You must enter a valid two-letter coordinate like A2.")
        else:
            row, col = location
            if row not in "ABCDEFGH":
                print("Your row must be a letter ABCDEFGH.")
            elif col not in "123456789":
                print("Your column must be between 1 and 9.")
            else:
                row = "ABCDEFGH".index(row)
                col = int(col) - 1
                is_valid = True
    print("You chose", row, col)
    return row, col


def prompt_player_direction(game, ship, row, col):
    is_chosen = False

    index = 0
    directions = ["right", "down", "left", "up"]
    direction = directions[index]

    while not is_chosen:
        display_placement_preview(game, ship, row, col, direction)

        print("Confirm direction", direction, "(y):", end="")
        choice = input()
        if choice == "y":
            is_chosen = True
        else:
            index = (index + 1) % len(directions)
            direction = directions[index]
    return direction


def main():
    game = BattleshipGame()
    while not game.is_game_over:
        if game.phase == game.PLACING:
            display_board(game)

            ship = prompt_player_ship(game)
            row, col = prompt_player_location(game)
            direction = prompt_player_direction(game, ship, row, col)

            game.place_ship(ship, row, col, direction)
        elif game.phase == game.FIRING:
            column = prompt_player(game)
            game.make_move(column)
    display_winner(game)


main()
