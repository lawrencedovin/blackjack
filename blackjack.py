from art import logo
import os
from random import sample
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
your_hand = sample(cards,2)
your_score = sum(your_hand)
dealers_hand = sample(cards,2)
dealers_score = sum(dealers_hand)

def clear():
    os.system("cls")
    os.system("clear")

if choice == "y":
    clear()
    print(logo)
    print(f"Your cards: {your_hand}, current score: {your_score}")
    print(f"Dealer's first card: {dealers_hand[0]}")
else:
    exit()
