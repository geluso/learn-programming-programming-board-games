from battleship_board_displayer import display_placement_preview


def prompt_player_ship(player):
    is_chosen = False
    while not is_chosen:
        print("Select a ship:")
        for i, ship in enumerate(player.ships):
            asterisks = "*" * ship.size
            padding = " " * (5 - ship.size)
            msg = i + 1, padding, asterisks, "Placed:", ship.is_placed, ship.name
            print(*msg)

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
        # choose the next direction and see if it is valid
        index = (index + 1) % len(directions)
        direction = directions[index]

        is_valid = display_placement_preview(player, ship, row, col, direction)
        if not is_valid:
            # notify the user and wait for them to press enter
            print("Invalid location. Choose again.")
            acknowledge = input()
        else:
            print("Confirm direction", direction, "(y):", end="")
            choice = input()
            if choice == "y":
                is_chosen = True
    return direction
