SPADES = 'spades'
CLUBS = 'clubs'
DIAMONDS = 'diamonds'
HEARTS = 'hearts'
SUITS = [SPADES, CLUBS, DIAMONDS, HEARTS]
FACES = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']


class Card:
    def __init__(self, face, suit):
        self.face = face
        self.suit = suit

    @classmethod
    def from_str(cls, str):
        face = str[0]
        suit = str[1]
        if suit == 'S':
            return Card(face, SPADES)
        elif suit == 'C':
            return Card(face, CLUBS)
        elif suit == 'D':
            return Card(face, DIAMONDS)
        elif suit == 'H':
            return Card(face, HEARTS)

    def __gt__(self, other):
        if self.face == other.face:
            suits = [SPADES, CLUBS, DIAMONDS, HEARTS]
            rank_self = suits.index(self.suit)
            rank_other = suits.index(other.suit)
        else:
            faces = [2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"]
            rank_self = faces.index(self.face)
            rank_other = faces.index(other.face)
        return rank_self > rank_other
