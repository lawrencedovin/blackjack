import os
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def clear():
    os.system("cls")
    os.system("clear")

def print_cards(player_hand, player_score, dealers_hand):
    print(f"Your cards: {player_hand}, current score: {player_score}")
    print(f"Dealer's first card: {dealers_hand[0]}")

def check_win(player_hand, player_score, dealers_hand, dealers_score):
    if dealers_score < 17:
        dealers_hand.append(random.choice(cards))
        dealers_score = sum(dealers_hand)
    print(f"Your final hand: {player_hand}, final score: {player_score}")
    print(f"Dealer's final hand: {dealers_hand}, final score: {dealers_score}")
    if dealers_score <= 21 and player_score <= 21:
        if dealers_score == player_score:
            print("Tie!")
        else:
            print("Dealer won!") if dealers_score > player_score else print("Player won!")
    elif dealers_score > 21:
        print("Both have lost in a Tie!") if player_score > 21 else print("Dealer has went over 21, Player won!")
    else:
        print("Player has went over 21, Dealer won!")

def draw_card(choice, player_hand, player_score, dealers_hand, dealers_score):
    if choice == "y":
        player_hand.append(random.choice(cards))
        player_score = sum(player_hand)
        print_cards(player_hand, player_score, dealers_hand)
        check_win(player_hand, player_score, dealers_hand, dealers_score)
    else:
        check_win(player_hand, player_score, dealers_hand, dealers_score)