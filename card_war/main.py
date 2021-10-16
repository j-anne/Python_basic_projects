import random
from random import shuffle

SUITES = 'H D S C'.split()
RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()


class Deck:
    def __init__(self, suites, ranks):
        self.suites = suites
        self.ranks = ranks

    def card(self):
        deck = []
        for suite in self.suites:
            for card in self.ranks:
                deck.append(suite + " : " + card)
        random.shuffle(deck)
        return deck[:3]


class Hand:
    def __init__(self, deck):
        self.deck = deck

    def remove(self, num):
        num = int(num)
        self.deck.remove(self.deck[num])
        return self.deck

    def add(self, deck):
        new_card = deck[0]
        return self.deck + [new_card]


class Player:
    pass


# Play Time
print('Welcome to War. Let\'s begin!')

draw = Deck(RANKS, SUITES).card()
additional = Deck(RANKS, SUITES).card()
print(draw)
print(Hand(draw).remove(2))
print(additional)
print(Hand(draw).add(additional))