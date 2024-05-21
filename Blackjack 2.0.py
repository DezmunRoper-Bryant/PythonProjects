# Current game mechanics 6/18/23 @ 7:50pm

# Hid the dealer's second card800

# When it is time for the player to draw, the need to be able to see one of the dealer's cards
# Want to create a card that has the properties of the back of a card to "hide" a card500

# Logic idea. Play player is able to see the dealer's first card (the 0th index of their hand array)✅


# Changing the game so the player doesn't pick the number of players. I am making the game a player vs dealer.✅
# Getting rid of the player being able to pick the value of the ace. There is a systematic way to pick it.✅
# Need to adjust the game mechanics so that it is actually black jack ✅
# Need to add in money and bets and a way to actually win and lose ✅
# Might need to something like chips to ensure players spend a multiple
# Maybe need to implement a way to save the money you have for future use
# Want to also me about to have the user choose if they want traditional Current Game Versions (where the player is able to play themselves)
# or quick Current Game Versions where the game is instant and the AI plays for them.

import random
import subprocess
import sys
import time


def clear_screen():
    operating_system = sys.platform
    if operating_system == 'win32':
        subprocess.run('cls', shell=True)


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
ranks = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]

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
        self.score = 21
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
    if deck[0].rank == "Ace":
        if drawer.hand_value <= 10:
            # value = 11
            drawer.hand_value += 11
        else:
            # value = 1
            drawer.hand_value += 1
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


def card_Creation_Hidden(current_player):
    dealer_top_card = current_player.hand[0]
    rank_logo, suit_logo = logo_Definition(dealer_top_card)
    print(f"┌─────────┐ ╔═╤═╤═╤═╤═╗")
    if dealer_top_card.rank.isdigit():
        if int(dealer_top_card.rank) == 10:
            print(f"│{rank_logo}       │ ╟─┼─┼─┼─┼─╢")
        else:
            print(f"│{rank_logo}        │ ╟─┼─┼─┼─┼─╢")
    else:
        print(f"│{rank_logo}        │ ╟─┼─┼─┼─┼─╢")
    print(f"│         │ ║┌┴─┴─┴─┴┐║")
    print(f"│    {suit_logo}    │ ╟┤ ╳ ╳ ╳ ├╢")
    print(f"│         │ ║└┬─┬─┬─┬┘║")
    if dealer_top_card.rank.isdigit():
        if int(dealer_top_card.rank) == 10:
            print(f"│       {rank_logo}│ ╟─┼─┼─┼─┼─╢")
        else:
            print(f"│        {rank_logo}│ ╟─┼─┼─┼─┼─╢")
    else:
        print(f"│        {rank_logo}│ ╟─┼─┼─┼─┼─╢")
    print(f"└─────────┘ ╚═╧═╧═╧═╧═╝")


user = Player(1)
dealer = Player(2)

print("Welcome to the world of Black Jack")
game_on = True

money = 1000

while game_on:

    bet = ""

    stay = True
    while stay:
        clear_screen()
        print(f"Your Account Balance: ${money}")
        print("How much would you like to bet250 250 ?")
        boolean = True
        while boolean:
            bet = input("> ")
            if bet.isdigit():
                if int(bet) in range(1, money + 1):
                    print("Are you sure? y/n")
                    choice = ""
                    while choice not in ["y", "n"]:
                        choice = input(">")
                        if choice == "y":
                            bet = int(bet)
                            money -= bet
                            print(f"Your remaining balance: {money}")
                            boolean = False
                            stay = False
                        else:
                            boolean = False

    # Creates a new deck which is just the original decks shuffled
    shuffled_deck = original_deck[:]
    random.shuffle(shuffled_deck)
    player_count: int = 0

    # Created an instance for the user and dealer
    print(f"Your deck as {len(shuffled_deck)} cards in it")

    user.hand = []
    user.hand_value = 0
    dealer.hand = []
    dealer.hand_value = 0
    winnings = 0
    print(user.hand_value)
    print(dealer.hand_value)
    leave_game = False
    input("Press enter to start")

    player_count = 2  # This is a 2 player experience. The user (player 1) vs the dealer (player 2)

    # Start game
    # Create an initial draw phase for the players:
    # Cycle through every player and give them a card
    round = 1
    while round < 3:
        for player in Player.ai:
            draw(player, shuffled_deck)
            if player == user:
                clear_screen()
                print("Your Hand:")
                card_Creation(user)
                time.sleep(0.5)
        round += 1

    # Print every player's hands/scores
    # printPlayers()5
    # print()

    print()
    # user's turn to draw some cards!
    clear_screen()
    print("Your Hand:")
    card_Creation(user)
    print(user.hand_value)
    if user.hand_value == 21:
        print("BLACK JACK!")
        time.sleep(0.5)
        print("Great Job!")
        time.sleep(0.5)
        print("Now let's see what the dealer has...")
        time.sleep(1)
        player_bj = True
    print("Dealer's Hand:")
    card_Creation_Hidden(dealer)
    print("It is your turn! Enter D for Draw | S for Stay")
    choice = ""

    user_bust = False
    user_bj = False
    dealer_bust = False
    dealer_bj = False
    player_win = False
    if not user_bj:
        while user.hand_value < 21:
            choice = ""

            while choice not in ["D", "S"]:
                choice = input(">")

                if choice == "D":
                    draw(user, shuffled_deck)
                    print(f"You Drew {user.hand[-1]}")
                    time.sleep(1)
                    card_Creation(user)
                    print(f"Value: {user.hand_value}")
                    if user.hand_value > 21:
                        time.sleep(1)
                        print("Your hand is a bust")
                        user_bust = True
                        time.sleep(1)
                        break
                    elif user.hand_value == 21:
                        time.sleep(1)
                        print("You scored a 21 and can no longer draw.")
                        time.sleep(1)
                        player_bust = True
                        break
                elif choice == "S":
                    print("You decided to stay")
                    break
            # card_Creation(user)
            # print(user.hand_value)
            if choice == "S":
                break

    if not user_bust:
        print(f"It is the dealer's turn!")
        if dealer.hand_value == 21:
            print("THE DEALER GOT BLACK JACK")
            dealer_bj = True
        if not dealer_bj:
            for ai in Player.ai[1:]:
                clear_screen()
                time.sleep(0.75)
                card_Creation(ai)
                time.sleep(0.5)
                while ai.hand_value < 21:
                    if ai.hand_value < 17:
                        draw(ai, shuffled_deck)
                        clear_screen()
                        print(f"Dealer's Hand:")
                        card_Creation(ai)
                        time.sleep(0.5)
                        if ai.hand_value > 21:
                            print(f"The dealer bust and they are out. You win")
                            time.sleep(2)
                            dealer_bust = True
                            player_win = True
                            winnings = 2
                            leave_game = True
                            break
                    else:
                        break

                if leave_game:
                    print("Round is ending")
                    break

                print(ai)
                clear_screen()
                print(f"Dealer's Hand:")

                card_Creation(ai)
                time.sleep(0.75)
                print(dealer.hand_value)
                time.sleep(2.5)

    clear_screen()
    time.sleep(4)
    if not user_bust and not dealer_bust:
        if user_bj and not dealer_bj:
            print("You got a black jack and the dealer did not. You win")
            winnings = 2.5
            player_win = True
        if user.hand_value > dealer.hand_value:
            winnings = 2
            player_win = True
        elif user.hand_value == dealer.hand_value:
            winnings = 1
            print("You both have the same hand")
            player_win = True
        else:
            player_win = False

    if player_win:
        print("You win!")
        money += (bet * winnings)
        if winnings == 1:
            print(f"Although you did not win, you won your money back!")
        else:
            print(f"You won your money back plus an additional {(bet * winnings) - bet}!")
    else:
        print("YOU LOSE!!")

    clear_screen()

    print("The round is over. Press Enter to play again | q to leave")
    choice = " "

    while choice not in ["", "q"]:
        choice = input(">")

        if choice == "":
            pass
        elif choice == "q":
            print("Leaving Black Jack")
            game_on = False

