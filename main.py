# Capstone Project- Black-Jack Game

import random


cards_dic = {
    "1": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "10": 10,
    "Jack": 10,
    "Queen": 10,
    "King": 10,
    "Ace": 11
}


def get_card_list(num):
    card_list = random.sample(list(cards_dic.keys()), k=num)
    return card_list


def get_score(list):
    score = 0
    for card in list:
        score += cards_dic[card]
    return score


def result_presentation():
    print(f"Your Cards: {your_cards},   Your Score: {current_score}")
    print(f"Computers Cards: {computer_cards}, Computer Score: {computer_score}")


game_start = input("Do you want to play a game of Blackjack? (y/n) ").lower()

if game_start == "y":
    your_cards = get_card_list(2)
    current_score = get_score(your_cards)

    computer_cards = get_card_list(2)
    computer_score = get_score(computer_cards)

    print(f"Your Cards: {your_cards},   Your Score: {current_score}")
    print(f"Computers First Card: {computer_cards[0]}")

    high_score = True
    while high_score:

        another_card = input("What do you want to do next 'Hit' or 'Stand':").lower()
        if another_card == "hit":
            one_more_card = get_card_list(1)
            your_cards.append(one_more_card[0])
            current_score = get_score(your_cards)

            print(f"Your Cards: {your_cards},   Your Score: {current_score}")
            print(f"Computers First Card: {computer_cards[0]}")

            if current_score > 21:
                high_score = False
                result_presentation()
                print("Ohh you lose!!!!")

            elif current_score == 21:
                one_more_card_com = get_card_list(1)
                computer_cards.append(one_more_card_com[0])
                computer_score = get_score(computer_cards)

                if computer_score > 21:
                    high_score = False
                    result_presentation()
                    print("Ohh you Win!!!!")
                elif current_score == computer_score:
                    high_score = False
                    result_presentation()
                    print("It is a Draw!!!!")

            elif (current_score < 21) and (computer_score < current_score):
                one_more_card_com = get_card_list(1)
                computer_cards.append(one_more_card_com[0])
                computer_score = get_score(computer_cards)
                if computer_score > 21:
                    high_score = False
                    result_presentation()
                    print("Ohh you Win!!!!")

        elif another_card == "stand":
            computer_score = get_score(computer_cards)
            current_score = get_score(your_cards)

            if computer_score > current_score:
                high_score = False
                result_presentation()
                print("Ohh you lose!!!!")
            elif computer_score < current_score:
                high_score = False
                result_presentation()
                print("Ohh you win!!!!")
            elif computer_score == current_score:
                high_score = False
                result_presentation()
                print("Ohh It is a Draw!!!!")