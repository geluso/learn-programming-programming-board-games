from util import direction_to_dx_dy
from ship import Carrier, Battleship, Cruiser, Submarine, Destroyer

from battleship_board import BattleshipBoard
from battleship_player import BattleshipPlayer


PLACING = 0
COMPUTER_PLACEMENT = 1
FIRING = 2


class BattleshipGame:
    def __init__(self):
        self.reset()

    def reset(self):
        self.is_game_over = False
        self.winner = None
        self.phase = PLACING

        self.turn = 0
        self.players = [BattleshipPlayer(), BattleshipPlayer()]

    def next_phase(self):
        if self.phase == PLACING:
            self.phase = COMPUTER_PLACEMENT
        elif self.phase == COMPUTER_PLACEMENT:
            self.phase == FIRING

    def get_current_player(self):
        index = self.turn % len(self.players)
        return self.players[index]

    def get_other_player(self):
        index = (self.turn + 1) % len(self.players)
        return self.players[index]

    def fire(self, row, col):
        player = self.get_current_player()
        other = self.get_other_player()

        is_hit = other.receive_shot(row, col)
        player.mark_shot(row, col, is_hit)

    def place_ship(self, ship_type, row, col, direction):
        player = self.get_current_player()
        player.place_ship(ship_type, row, col, direction)

    def place_ai_ships(self):
        pass


BattleshipGame.PLACING = PLACING
BattleshipGame.COMPUTER_PLACEMENT = COMPUTER_PLACEMENT
BattleshipGame.FIRING = FIRING
