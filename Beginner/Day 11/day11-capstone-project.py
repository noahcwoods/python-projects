import cards
import random

print("Welcome to BlackJack!")
done = False
fresh_cards = cards.all_possible_cards

def shuffle_cards():
    """Shuffles the cards in the deck"""
    random.shuffle(fresh_cards)


def deal_cards():
    """Deals the cards in the deck. Returns one card"""
    return fresh_cards.pop()


def check_winner():
    """Checks for winner of blackjack"""
    while sum(dealers_cards) < 17:
        dealers_cards.append(deal_cards())

    print(f"\nYour cards are: {players_cards}")
    print(f"The dealers cards are: {dealers_cards}")

    if (sum(players_cards) > sum(dealers_cards) and sum(players_cards) <= 21) or (
            sum(dealers_cards) > 21 and sum(players_cards) <= 21):
        return "You Win!"
    else:
        return "You Lose!"


def hit_loop():
    """Runs until user decides not to hit, or until they go over 21"""
    # Start hit loop until bust or stand
    game_in_progress = True
    while game_in_progress:
        player_decision = input("Press [s] to stand. Press [h] to hit: ")

        # Stand, check for winner, break game loop and restart
        if player_decision == "s":
            print(check_winner())
            game_in_progress = False
        else:

            # Deal a card
            players_cards.append(deal_cards())
            print(f"\nYour cards are: {players_cards}")

            # If over 21, check for any 11(Ace's) and replace with a 1, or end game
            while sum(players_cards) > 21:
                if 11 not in players_cards:
                    print(f"\nYour cards are: {players_cards}")
                    print(f"The dealers cards are: {dealers_cards}")
                    print("You Lose!")
                    game_in_progress = False
                    break
                else:
                    players_cards[players_cards.index(11)] = 1
                    print(f"\nYour cards are: {players_cards}")


while not done:
    print("\nLet's Deal the cards!")

    # All Empty Card Containers
    players_cards = []
    dealers_cards = []

    # Shuffle The Deck
    shuffle_cards()

    # Assign initial cards to dealer and player
    for _ in range (2):
        players_cards.append(deal_cards())
        dealers_cards.append(deal_cards())

    # Display Cards
    print(f"Your cards are: {players_cards}")
    print(f"The dealer has drawn: {dealers_cards[0]}")

    # Check for BlackJack
    if sum(players_cards) == 21:
        print("BLACKJACK! You Win!")
        if input("Would you like to play again?") == "N":
            done = True
            continue
        else:
            continue

    hit_loop()

    if input("\n\nWould you like to play again? [y/n]") == "n":
        done = True
