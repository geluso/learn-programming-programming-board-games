EMPTY = "."


class Ship:
    def __init__(self, size):
        self.size = size
        self.hits = {}
        self.dx = None
        self.dy = None
        self.direction = None


class Carrier(Ship):
    def __init__(self):
        super(self, 5)


class Battleship(Ship):
    def __init__(self):
        super(self, 4)


class Cruiser(Ship):
    def __init__(self):
        super(self, 3)


class Submarine(Ship):
    def __init__(self):
        super(self, 3)


class Destroyer(Ship):
    def __init__(self):
        super(self, 2)


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
        return "X"

    def make_move(self, col):
        pass

    def place_ship(self, ship, row, col, direction):
        pass


BattleshipGame.PLACING = PLACING
BattleshipGame.FIRING = FIRING
