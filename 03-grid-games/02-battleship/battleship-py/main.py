from battleship_game import BattleshipGame

from util import random_row_col_direction
from battleship_board_displayer import display_board, display_placement_preview
from prompt_player_input import prompt_player_ship, prompt_player_location, prompt_player_direction


def display_winner(game):
    display_board(game)
    if game.winner is None:
        print("CATS! The game ended in a tie.")
    else:
        print(game.winner, "won!")


def player_place_ship(game, player):
    display_board(player.ship_placements)

    ship = prompt_player_ship(player)
    row, col = prompt_player_location()
    direction = prompt_player_direction(player, ship, row, col)

    player.place_ship(ship, row, col, direction)

    print("placed:", player.placed_ships, len(player.ships))
    if player.placed_ships == len(player.ships):
        game.next_phase()


def place_ship_randomly(cpu, ship):
    is_placed = False
    while not is_placed:
        row, col, direction = random_row_col_direction()
        print("trying", row, col, direction)
        if cpu.ship_placements.is_room_for_ship(ship, row, col, direction):
            cpu.ship_placements.place_ship(ship, row, col, direction)
            is_placed = True


def place_ships_randomly(player):
    print("Placing AI ships.")

    # reverse the ships so it places the largest ship first
    # when there's more open room around
    for ship in player.ships[::-1]:
        place_ship_randomly(player, ship)


def player_fire(game):
    print("Player fire")
    input()
    pass


def computer_fire(game):
    print("Computer fire")
    input()
    pass


def main():
    game = BattleshipGame()
    place_ships_randomly(game.players[0])
    place_ships_randomly(game.players[1])
    display_board(game.players[0].ship_placements.board)
    display_board(game.players[1].ship_placements.board)
    return

    while not game.is_game_over:
        player = game.get_current_player()
        if game.phase == game.PLACING:
            player_place_ship(game, player)
        elif game.phase == game.COMPUTER_PLACEMENT:
            place_ships_randomly(game.players[1])
        elif game.phase == game.FIRING:
            print("Entering Firing phase.")
            input()
            pass
    display_winner(game)


print("ARRRRR!! Welcome to the high seas. Prepare to play:    BATTLESHIP!!")
main()
