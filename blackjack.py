from art import logo
import os
import random
############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
choice = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
player_hand = random.sample(cards,2)
player_score = sum(player_hand)
dealers_hand = random.sample(cards,2)
dealers_score = sum(dealers_hand)

def clear():
    os.system("cls")
    os.system("clear")

def print_cards(player_hand, player_score, dealers_hand):
    print(f"Your cards: {player_hand}, current score: {player_score}")
    print(f"Dealer's first card: {dealers_hand[0]}")


if choice == "y":
    clear()
    print(logo)
    print_cards(player_hand, player_score, dealers_hand)

    draw_card = input("Type 'y' to get another card, type 'n' to pass: ")
    if draw_card == "y":
        player_hand.append(random.choice(cards))
        player_score = sum(player_hand)
        print_cards(player_hand, player_score, dealers_hand)
    else:
        print("hello")
else:
    exit()
