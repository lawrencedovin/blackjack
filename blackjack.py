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

# def check_win

def draw_card(choice, player_hand, player_score, dealers_hand, dealers_score):
    if choice == "y":
        player_hand.append(random.choice(cards))
        player_score = sum(player_hand)
        if dealers_score < 17:
            dealers_hand.append(random.choice(cards))
            dealers_score = sum(dealers_hand)
        print_cards(player_hand, player_score, dealers_hand)
        print(f"Your final hand: {player_hand}, final score: {player_score}")
        print(f"Dealer's final hand: {dealers_hand}, final score: {dealers_score}")
    else:
        print("hello")

if choice == "y":
    clear()
    print(logo)
    print_cards(player_hand, player_score, dealers_hand)

    draw_card_choice = input("Type 'y' to get another card, type 'n' to pass: ")
    draw_card(draw_card_choice, player_hand, player_score, dealers_hand, dealers_score)
else:
    exit()
