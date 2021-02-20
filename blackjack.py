from art import *
from blackjack_functions import *
import random

def blackjack():
    play_game_choice = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
    player_hand = random.sample(cards,2)
    player_score = sum(player_hand)
    dealers_hand = random.sample(cards,2)
    dealers_score = sum(dealers_hand)

    if play_game_choice == "y":
        clear()
        print(logo)
        print_cards(player_hand, player_score, dealers_hand)
        draw_card_choice = input("Type 'y' to get another card, type 'n' to pass: ")
        draw_card(draw_card_choice, player_hand, player_score, dealers_hand, dealers_score)
        continue_choice = input("Play again? Type 'y' or 'n': ").lower()
        blackjack() if continue_choice == "y" else exit()
    else:
        exit()

blackjack()
