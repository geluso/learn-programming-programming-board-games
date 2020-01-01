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


def display_placement_preview(player, ship, irow, icol, direction):
    print()
    print("Ships left:")
    print("X: 2[  ] 3[   ] 3[   ] 4[    ] 5[     ]")
    print("O: 2[  ] 3[   ] 3[   ] 4[    ] 5[     ]")
    print()
    print("   1  2  3  4  5  6  7  8  9  ")

    is_valid = True

    # set
    dx, dy = direction_to_dx_dy(direction)
    for n in range(ship.size):
        drow = irow + dy * n
        dcol = icol + dx * n
        if player.ship_placements.board[drow][dcol] != ".":
            is_valid = False
            player.ship_placements.board[drow][dcol] = "X"
        else:
            player.ship_placements.board[drow][dcol] = str(ship.size)

    rows = list("ABCDEFGH")
    for letter, row in zip(rows, player.ship_placements.board):
        line = letter + "  "
        line += "  ".join(row) + "  " + letter
        print(line)

    # unset
    for n in range(ship.size):
        drow = irow + dy * n
        dcol = icol + dx * n
        player.ship_placements.board[drow][dcol] = "."
    return is_valid
