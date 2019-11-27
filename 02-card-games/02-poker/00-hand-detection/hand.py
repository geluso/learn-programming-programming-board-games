import card
from collections import defaultdict


class AssessedHand:
    """
    Represents a poker hand that's been sorted and processed to easily determine different hands.

    the hand has the original hand
    the high card represents the card with the combined highest face and suit
    faces is an array of the most-occuring faces and number of occurences (sorted most occurences to least)
    suits in an array of the most-occuring suits and number of occurences (sorted most occurences to least)

    hand: [{8, hearts}, {8 spades}, {4 hearts}, {4 diamonds}, {4 spades}]
    high_card: Card(8, hearts)
    faces: [[4, 3], [8, 2]]
    suits: [[hearts, 2], [spades, 2], [diamonds, 1]]
    """

    def __init__(self, hand):
        self.hand = hand
        self.assess()

    @classmethod
    def from_string_array(cls, cards):
        hand = []
        for card in cards:
            hand.append(card.Card.from_str(card))
        return hand

    def assess(self):
        self.faces = []
        self.suits = []
        self.high_card = self.hand[0]

        faces = defaultdict(0)
        suits = defaultdict(0)

        for card in self.hand:
            suits[hand.face] += 1
            suits[hand.suit] += 1

            if card > high_card:
                high = card

        def sort(key_value): return key_value[1]
        self.faces = sorted(faces.items(), key=sort, reverse=True)
        self.suits = sorted(suits.items(), key=sort, reverse=True)

    def identify_hand(self):
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

    def is_royal_flush(self):
        if self.is_straight_flush() and self.faces[0][0] == 'A':
            return True
        return False

    def is_straight_flush(self):
        if self.is_straight() and self.is_flush():
            return True
        return False

    def is_four_of_a_kind(self):
        if self.faces[0][1] == 4:
            return True
        return False

    def is_full_house(self):
        if self.faces[0][1] == 3 and self.faces[1][1] == 2:
            return True
        return False

    def is_flush(self):
        if self.suits[0][1] == 5:
            return True
        return False

    def is_straight(self):
        pass

    def is_three_of_a_kind(self):
        if self.faces[0][1] == 3:
            return True
        return False

    def is_two_pair(self):
        if self.faces[0][1] == 2 and self.faces[1][1] == 2:
            return True
        return False

    def is_pair(self):
        if self.faces[0][1] == 2:
            return True
        return False

    def is_high_card(self):
        return self.high_card
