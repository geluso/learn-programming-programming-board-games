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
