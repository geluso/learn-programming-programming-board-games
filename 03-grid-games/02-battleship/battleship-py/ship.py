class Ship:
    def __init__(self, size):
        self.size = size
        self.hits = []

        self.is_placed = False
        self.is_sunk = False

        self.dx = None
        self.dy = None
        self.direction = None

    def take_hit(self, row, col):
        self.hits.append([row, col])
        if len(self.hits) == self.size:
            self.is_sunk = True


class Carrier(Ship):
    def __init__(self):
        super(Carrier, self).__init__(5)


class Battleship(Ship):
    def __init__(self):
        super(Battleship, self).__init__(4)


class Cruiser(Ship):
    def __init__(self):
        super(Cruiser, self).__init__(3)


class Submarine(Ship):
    def __init__(self):
        super(Submarine, self).__init__(3)


class Destroyer(Ship):
    def __init__(self):
        super(Destroyer, self).__init__(2)
