import random


class Card:
    all_cards = []

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

        if self.rank.isdigit():
            self.value = int(self.rank)
        else:
            if self.rank in ["Jack", "Queen", "King"]:
                self.value = 10
            else:
                self.value = 0

        Card.all_cards.append(self)

    def __repr__(self):
        # The use of this is to kinda give the instance a new name...
        return f"{self.rank} of {self.suit}"


# Define the suits and ranks of the cards in a deck
original_deck = []
suit = ["Spades", "Clubs", "Hearts", "Diamonds"]
ranks = ["Ace", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]

# Creates an instance for every card that appears in the deck the adds that card into the deck
for suit in suit:
    for rank in ranks:
        card = Card(suit, rank)
        original_deck.append(card)


class Player:
    ai = []

    def __init__(self, id_num):
        self.id = id_num  # indicator for what player it is (Player 2, Player 3, etc)
        self.hand = []
        self.hand_value = 0
        Player.ai.append(self)

    def __repr__(self):
        return f"Player {self.id}"


def printPlayers():
    for player in Player.ai:
        print(player)
        card_Creation(player)
        print(player.hand_value)


def draw(drawer, deck):
    drawer.hand.append(deck[0])  # adding the top card to the drawer's hand
    if drawer.id > 1:
        if deck[0].rank == "Ace":
            if drawer.hand_value <= 10:
                # value = 11
                drawer.hand_value += 11
            else:
                # value = 1
                drawer.hand_value += 1
        else:
            drawer.hand_value += deck[0].value
        # Hand_Value += value  # Update the hand_value directly on the player object
    else:
        if deck[0].rank == "Ace":
            print(f"You drew {deck[0]}. What do you want the value of this ace to be?")
            choice = ""
            while choice not in ["1", "11"]:
                choice = input("> ")
                if choice.isdigit():
                    if int(choice) == 1:
                        # value = 1
                        drawer.hand_value += 1
                    elif int(choice) == 11:
                        # value = 11
                        drawer.hand_value += 11
                    else:
                        pass
                else:
                    pass
        else:
            drawer.hand_value += deck[0].value
    deck.pop(0)  # moves the top card out of the deck
    return deck


def logo_Definition(current_card):
    rank_logo = ""
    suit_logo = ""
    if current_card.rank.isdigit():
        rank_logo = current_card.rank
    elif current_card.rank == "Ace":
        rank_logo = "A"
    elif current_card.rank == "Jack":
        rank_logo = "J"
    elif current_card.rank == "Queen":
        rank_logo = "Q"
    elif current_card.rank == "King":
        rank_logo = "K"

    if current_card.suit == "Spades":
        suit_logo = "♠"
    elif current_card.suit == "Clubs":
        suit_logo = "♣"
    elif current_card.suit == "Hearts":
        suit_logo = "♥"
    elif current_card.suit == "Diamonds":
        suit_logo = "♦"
    return rank_logo, suit_logo


def card_Creation(current_player):
    for cards in current_player.hand:
        rank_logo, suit_logo = logo_Definition(cards)
        print(f"┌─────────┐", end=" ")
    print()
    for cards in current_player.hand:
        rank_logo, suit_logo = logo_Definition(cards)
        if cards.rank.isdigit():
            if int(cards.rank) == 10:
                print(f"│{rank_logo}       │", end=" ")
            else:
                print(f"│{rank_logo}        │", end=" ")
        else:
            print(f"│{rank_logo}        │", end=" ")
    print()
    for cards in current_player.hand:
        rank_logo, suit_logo = logo_Definition(cards)
        print(f"│         │", end=" ")
    print()
    for cards in current_player.hand:
        rank_logo, suit_logo = logo_Definition(cards)
        print(f"│    {suit_logo}    │", end=" ")
    print()
    for cards in current_player.hand:
        rank_logo, suit_logo = logo_Definition(cards)
        print(f"│         │", end=" ")
    print()
    for cards in current_player.hand:
        rank_logo, suit_logo = logo_Definition(cards)
        if cards.rank.isdigit():
            if int(cards.rank) == 10:
                print(f"│       {rank_logo}│", end=" ")
            else:
                print(f"│        {rank_logo}│", end=" ")
        else:
            print(f"│        {rank_logo}│", end=" ")
    print()
    for cards in current_player.hand:
        rank_logo, suit_logo = logo_Definition(cards)
        print(f"└─────────┘", end=" ")
    print()


# Creates a new deck which is just the original decks shuffled
shuffled_deck = original_deck[:]
random.shuffle(shuffled_deck)
player_count = 0

# Created an instance for the user with an id of 1 (For player 1)
user = Player(1)

print("Welcome to the world of Black Jack")
print("How many players would you like to play with between 2 and 7?")
player_count = 0

# Asks the user how many players are playing
while True:
    player_count = input("> ")
    if player_count.isdigit():
        if int(player_count) in range(2, 8):
            player_count = int(player_count)
            break
    else:
        pass

print(f"Player count: {player_count}")

# Create several instance for new players (AI designed) depending on the number of players - 1
for ai_id in range(2, player_count + 1):
    ai = Player(ai_id)
    print(f"New player created: {ai}")
print()

# Start game
# Create an initial draw phase for all the players:
# Cycle through every player and give them a card
round = 1
while round < 3:
    for player in Player.ai:
        draw(player, shuffled_deck)
    round += 1

# Print every player's hands/scores
printPlayers()
print()

print()
# user's turn to draw some cards!
print("It is your turn! Enter D for Draw | S for Stay")
choice = ""
while user.hand_value < 21:
    choice = ""
    exit_outer_loop = False

    while choice not in ["D", "S"]:
        choice = input(">")

        if choice == "D":
            draw(user, shuffled_deck)
            card_Creation(user)
            print(f"Value: {user.hand_value}")
            if user.hand_value > 21:
                print("Your hand is a bust ")
                break
        elif choice == "S":
            print("You decided to stay")
            exit_outer_loop = True
            break
    # card_Creation(user)
    # print(user.hand_value)
    if exit_outer_loop:
        break
