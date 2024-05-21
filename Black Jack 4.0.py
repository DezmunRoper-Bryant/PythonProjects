# This will be the new black jack file made from scratch.
# Rules
"""
Rules
Standard Pack 52 Card Deck
Multiple Decks are used at a single time
Each player tries to beat the dealer by getting as close to 21 as possible
Numbers are their values, aces are 1 or 11, faces are 10
Player bets in chips
$2 to $500 bets

The deck is shuffled
One of the players cut and a plastic card is inserted
So that the last 60-75 or so card will not be used (no card counting)

All players get 2 face up cards
The dealer gets a face up and face down card



Natural BJ:
If any player has one and the dealer does not, they get 1.5 times their bet
If the dealer has one and no player does, every player loses their money
If the dealer and a player have one, the player gets their money back

If the dealer's face up card is a 10 card or Ace, they look at the other card to see if ther have an ace

Player to the left goes first
Clockwise fashion
If a player busts, their best is collected

DEALER'S PLAY
1. The face down card is turned
2. score > 17: Stay
3. score < 17: Hit
4. If the dealer has an ace, and counting it as 11 brings the total to at least 17 but not over 21, the dealer must count the ace as 11 and stand.

SPLITTING
If a player has two of the same card (Two 3s, two 4s, etc), they can choose to split the hand into to
When splitting the player must put an equal bet onto the second hand
The player now has two separate hands to play
If the aces are split, they draw one card per hand and their turn is done
    ->if a ten-card is dealt to one of these aces, the payoff is equal to the bet


"""

