from battleship_game import BattleshipGame

from battleship_board_displayer import display_board, display_placement_preview
from prompt_player_input import prompt_player_ship, prompt_player_location, prompt_player_direction


def display_winner(game):
    display_board(game)
    if game.winner is None:
        print("CATS! The game ended in a tie.")
    else:
        print(game.winner, "won!")


def main():
    game = BattleshipGame()
    while not game.is_game_over:
        player = game.get_current_player()
        if game.phase == game.PLACING:
            display_board(player.ship_placements)

            ship = prompt_player_ship(player)
            row, col = prompt_player_location()
            direction = prompt_player_direction(player, ship, row, col)

            player.place_ship(ship, row, col, direction)

            print("placed:", player.placed_ships, len(player.ships))
            if player.placed_ships == len(player.ships):
                game.next_phase()
        elif game.phase == game.COMPUTER_PLACEMENT:
            print("Placing AI ships.")
            input()
            game.place_ai_ships()
            game.next_phase()
        elif game.phase == game.FIRING:
            print("Entering Firing phase.")
            input()
            pass
    display_winner(game)


main()
