from ship import Carrier, Battleship, Cruiser, Submarine, Destroyer
from battleship_board import BattleshipBoard
from shot_result import ShotResult


class BattleshipPlayer:
    def __init__(self):
        self.ships = [
            Destroyer(), Submarine(), Cruiser(),
            Battleship(), Carrier()
        ]

        self.placed_ships = 0
        self.ship_placements = BattleshipBoard(self)
        self.shots_taken = BattleshipBoard(self)

    def place_ship(self, ship, row, col, direction):
        self.ship_placements.place_ship(ship, row, col, direction)
        ship.is_placed = True
        self.placed_ships += 1

    def is_all_ships_sunk(self):
        for ship in self.ships:
            if not ship.is_sunk:
                return False
        return True

    def mark_shot(self, row, col, shot_result):
        self.shots_taken[row][col] = shot_result

    def has_player_taken_shot(self, row, col):
        if self.shots_taken[row][col] is BattleshipBoard.EMPTY:
            return False
        return True

    def receive_shot(self, row, col):
        result = ShotResult()
        ship = self.ship_placements[row][col]
        if ship is not None:
            ship.take_hit(row, col)

            result.is_hit = True
            if ship.is_sunk:
                result.is_sunk = True
                result.ship_type = ship.ship_type
        return result
