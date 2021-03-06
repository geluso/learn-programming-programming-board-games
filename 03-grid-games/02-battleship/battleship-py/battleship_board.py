from util import direction_to_dx_dy

EMPTY = "."


class BattleshipBoard:
    def __init__(self, player):
        self.reset()
        self.player = player

    def reset(self):
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

    def is_valid(self, row, col):
        if row < 0 or col < 0 or row >= len(self.board) or col >= len(self.board[row]):
            return False
        return True

    def fire(self, row, col):
        pass

    def is_room_for_ship(self, ship, row, col, direction):
        dx, dy = direction_to_dx_dy(direction)
        for n in range(ship.size):
            drow = row + dy * n
            dcol = col + dx * n
            if not self.is_valid(drow, dcol):
                return False
            if self.board[drow][dcol] is not EMPTY:
                return False
        return True

    def place_ship(self, ship, row, col, direction):
        dx, dy = direction_to_dx_dy(direction)
        for n in range(ship.size):
            drow = row + dy * n
            dcol = col + dx * n
            self.board[drow][dcol] = str(ship.size)


BattleshipBoard.EMPTY = EMPTY
