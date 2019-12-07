class Rank:
    def __init__(self):
        pass

    def rank(self):
        """Stuff

        hand is an array of five Cards
        """
        hands = [
            self.is_royal_flush, self.is_straight_flush,
            self.is_four_of_a_kind, self.is_full_house, self.is_flush,
            self.is_straight, self.is_three_of_a_kind, self.is_two_pair,
            self.is_pair, self.is_high_card
        ]

        for hand in hands:
            if hand():
                return hand(self.hand)

        if is_royal_flush():
            pass


class RoyalFlush(Rank):
    def is_royal_flush(self):
        if self.is_straight_flush() and self.faces[0][0] == 'A':
            return True
        return False


class StraightFlush:
    def is_straight_flush(self):
        if self.is_straight() and self.is_flush():
            return True
        return False


class FourOfAKind:
    def is_four_of_a_kind(self):
        if self.faces[0][1] == 4:
            return True
        return False


class FullHouse:
    def is_full_house(self):
        if self.faces[0][1] == 3 and self.faces[1][1] == 2:
            return True
        return False


class Flush:
    def is_flush(self):
        if self.suits[0][1] == 5:
            return True
        return False


class Straight:
    def is_straight(self):
        pass


class ThreeOfAKind:
    def is_three_of_a_kind(self):
        if self.faces[0][1] == 3:
            return True
        return False


class TwoPair:
    def is_two_pair(self):
        if self.faces[0][1] == 2 and self.faces[1][1] == 2:
            return True
        return False


class Pair:
    def is_pair(self):
        if self.faces[0][1] == 2:
            return True
        return False


class HighCard:
    def is_high_card(self):
        return self.high_card
