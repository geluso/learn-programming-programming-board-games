from battleship_board_displayer import display_placement_preview


def prompt_player_ship(player):
    is_chosen = False
    while not is_chosen:
        print("Select a ship:")
        print("1.    ** Destroyer")
        print("2.   *** Submarine")
        print("3.   *** Cruiser")
        print("4.  **** Battleship")
        print("5. ***** Carrier")

        # subtract one to convert the number to a zero-index
        ship_index = int(input()) - 1
        ship = player.ships[ship_index]

        if ship.is_placed:
            print("Ship already placed! Choose another.")
        else:
            is_chosen = True
    return ship


def prompt_player_location():
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


def prompt_player_direction(player, ship, row, col):
    is_chosen = False

    index = 0
    directions = ["right", "down", "left", "up"]
    direction = directions[index]

    while not is_chosen:
        display_placement_preview(player, ship, row, col, direction)

        print("Confirm direction", direction, "(y):", end="")
        choice = input()
        if choice == "y":
            is_chosen = True
        else:
            index = (index + 1) % len(directions)
            direction = directions[index]
    return direction
