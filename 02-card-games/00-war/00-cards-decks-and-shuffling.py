import math
import random

class Player:
    def __init__(self):
        self.hand = []
        self.discard = []

    
    def total_cards(self):
        return len(self.hand) + len(self.discard)


    def is_empty(self):
        if self.total_cards() == 0:
            return True
        return False


    def draw(self):
        if self.is_empty():
            return None
        if len(self.hand) == 0:
            self.shuffle_discard_into_hand()
        return self.hand.pop()


    def shuffle_discard_into_hand(self):
        shuffle_deck(self.discard)

        self.hand = self.discard
        self.discard = []


class Card:
    def __init__(self, face, suit):
        self.face = face
        self.suit = suit

    def __str__(self):
        template = "%s of %s"
        return template % (self.face, self.suit)

    def __repr__(self):
        return self.__str__()

    def __gt__(self, other):
        faces = [2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"]
        rank_self = faces.index(self.face)
        rank_other = faces.index(other.face)
        return rank_self > rank_other

class Deck:
    def __init__(self):
        self.cards = create_deck()

    def draw():
        self.cards.pop()


def create_deck():
    deck = []
    suits = ["spades", "clubs", "diamonds", "hearts"]
    faces = [2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"]

    for suit in suits:
        for face in faces:
            card = Card(face, suit)
            deck.append(card)
    return deck


# shuffle the deck in place
def shuffle_deck(deck):
    # famous Fischer-Yates shuffle algorithm
    # awesome explanation and visualization by Mike Bostock
    # https://bost.ocks.org/mike/shuffle/
    # 
    # iterate over every card in the deck
    # pick another random index
    # swap the first index with the card at the random index
    for i in range(len(deck)):
        # pick the other random index
        swap_index = math.floor(random.random() * len(deck))

        # get a reference to each card
        card1 = deck[i]
        card2 = deck[swap_index]

        # swap the two cards
        deck[i] = card2
        deck[swap_index] = card1


def deal(deck, players):
    player_index = 0
    for card in deck.cards:
        player = players[player_index]
        player.hand.append(card)

        player_index += 1
        player_index = player_index % len(players)

def battle(player1, player2):
    card1 = player1.draw()
    card2 = player2.draw()

    print("player1:", card1)
    print("player2:", card2)

    if card1 > card2:
        print("player1 takes")
        winner = player1
    elif card1 < card2:
        print("player2 takes")
        winner = player2
    else:
        print("tie!")
        return

    winner.discard.append(card1)
    winner.discard.append(card2)


def display_players_cards(turn, player1, player2):
    print()

    p1_total = player1.total_cards()
    p2_total = player2.total_cards()

    print("Turn:", turn)
    print(f"player1 cards {p1_total:02}:", p1_total * "C")
    print(f"player2 cards {p2_total:02}:", p2_total * "C")

def war(player1, player2):
    turn = 0
    display_players_cards(turn, player1, player2)

    while not player1.is_empty() and not player2.is_empty():
        turn += 1

        display_players_cards(turn, player1, player2)
        battle(player1, player2)

    if player1.is_empty():
        print("player 2 wins!")

    if player2.is_empty():
        print("player 2 wins!")


def main():
    deck = Deck()

    player1 = Player()
    player2 = Player()

    deal(deck, [player1, player2])

    war(player1, player2)


main()
