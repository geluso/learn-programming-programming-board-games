from util import direction_to_dx_dy
from ship import Carrier, Battleship, Cruiser, Submarine, Destroyer

EMPTY = "."


PLACING = 0
FIRING = 1


class BattleshipGame:
    def __init__(self):
        self.reset()

    def reset(self):
        self.is_game_over = False
        self.winner = None
        self.phase = PLACING

        self.turn = 0
        self.players = ["X", "O"]

        self.pieces = [2, 3, 3, 4, 5]
        self.board = [
            [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
        ]

    def get_current_player(self):
        index = self.turn % len(self.players)
        return self.players[index]

    def make_move(self, col):
        pass

    def place_ship(self, ship, row, col, direction):
        player = self.get_current_player()
        dx, dy = direction_to_dx_dy(direction)
        for n in range(ship):
            drow = row + dy * n
            dcol = col + dx * n
            self.board[drow][dcol] = player


BattleshipGame.PLACING = PLACING
BattleshipGame.FIRING = FIRING
