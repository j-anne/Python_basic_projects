import random
from random import shuffle

SUITES = 'H D S C'.split()
RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()


class Deck:
    """
    This is the Deck class. This object will create a deck of cards to initiate play.
    You can then use this deck list of cards to split in half and give to the players.
    It will use SUITES and RANKS to create the deck. It should also have a method for
    splitting/cutting the deck in half and shuffling the deck.
    """
    def __init__(self):
        print("Creating new ordered of Decks!")
        self.all_cards = [(s, r) for s in SUITES for r in RANKS]

    def cards(self):
        print("Shuffling deck")
        shuffle(self.all_cards)
        return self.all_cards[:26], self.all_cards[26:]


class Hand:
    """
    This is the Hand class. Each player has a hand that can add or remove cards on their deck.
    """
    def __init__(self, deck):
        self.deck = deck

    def __str__(self):
        return f"You have {len(self.deck)} cards."

    def remove_card(self):
        return self.deck.pop()

    def add_card(self, new_card):
        return self.deck.extend(new_card)


class Player:
    """
    This is the Player class, which takes in a name and an instance of a Hand class object.
    The player can then play cards and check if they still have the cards
    """
    def __init__(self, name, hand):
        self.name = name
        self.hand = hand

    def play_card(self):
        drawn_card = self.hand.remove_card()
        print(f"{self.name} has drawn: {drawn_card}")
        print("\n")
        return drawn_card

    def remove_war_cards(self):
        war_cards = []
        if len(self.hand.deck) < 3:
            return self.hand.deck
        else:
            for x in range(3):
                war_cards.append(self.hand.remove_card())
            return war_cards

    def has_cards(self):
        """
        Return true if player still has cards left or otherwise
        """
        return len(self.hand.deck) != 0


# Start game
def start_game():
    print('Welcome to Card War. Let\'s begin!')

    # Start Game - Create variables
    # Create Deck
    game = Deck()
    player_one, player_two = game.cards()

    # Create Players
    comp = Player("computer", Hand(player_one))
    player_two_name = input("What is your name?: ")
    user = Player(player_two_name, Hand(player_two))

    total_rounds = 0
    war_count = 0

    # While there are still card for both user
    while user.has_cards() and comp.has_cards():
        total_rounds += 1
        print("Time for new round!")
        print(f"Current standing: "
              f"\n {comp.name} has the count:  {len(comp.hand.deck)} \n "
              f"{user.name} has the count:  {len(user.hand.deck)}")
        print("Draw a card \n")

        """
        Create table and start drawing cards from both player then add to table list
        """
        table_cards = []

        c_card = comp.play_card()
        p_card = user.play_card()

        table_cards.append(c_card)
        table_cards.append(p_card)
        print(f"user deck: {user.hand.deck} comp deck: {comp.hand.deck}")
        print(f" table is: {table_cards}")
        """
        Check if both players has drawn same number of card
        """
        if c_card[1] == p_card[1]:
            war_count += 1
            print("War!")
            """
            Both player will draw another three cards on the table
            """
            table_cards.extend(user.remove_war_cards())
            table_cards.extend(comp.remove_war_cards())

            """
            compare ranks of each player then whoever is less, all the cards in the table will be added on
            it's deck.
            """
            if SUITES.index(c_card[0]) < SUITES.index(p_card[0]):
                user.hand.add_card(table_cards)
            else:
                comp.hand.add_card(table_cards)

        else:
            if RANKS.index(c_card[1]) < RANKS.index(p_card[1]):
                user.hand.add_card(table_cards)
            else:
                comp.hand.add_card(table_cards)
    print("Game over! Number of rounds: ")
    print(f"Number of war: {war_count} \n"
          f"Number of Rounds: {total_rounds}")
    print(comp.has_cards(), user.has_cards())
    if comp.has_cards():
        print(f"{user.name} has won")
    else:
        print("Computer won")


start_game()