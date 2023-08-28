import random
from art import logo
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def deal_card():
    card = random.choice(cards)
    return card


def compare(user_score, computer_score):
    '''Compare the user score with the computer score to know the winner'''
    if user_score == computer_score:
        return "Draw "
    elif computer_score == 0:
        return "You lose, opponent has black jack"
    elif user_score == 0:
        return "You win, You have black jack"
    elif user_score > 21:
        return "You went over, you lose"
    elif computer_score > 21:
        return "You win, your opponent went over"
    elif user_score > computer_score:
        return "You win"
    else:
        return "You lose"


def calculate_score(cards):
    '''Take a list of card and return the score calculated from the list of card'''
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


def play_game():
    print(logo)
    user_card = []
    computer_card = []
    is_game_over = False

    for _ in range(2):
        user_card.append(deal_card())
        computer_card.append(deal_card())
    while not is_game_over:
        user_score = calculate_score(user_card)
        computer_score = calculate_score(computer_card)
        print(f"Your card {user_card}, your score {user_score}")
        print(f"Computer first card {computer_card[0]}")
        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            more_card = input(
                "Do you want to deal another card 'y' for YES 'n' if NO: ")
            if more_card == 'y':
                user_card.append(deal_card())
            else:
                is_game_over = True
    while computer_score != 0 and computer_score < 17:
        computer_card.append(deal_card())
        computer_score = sum(computer_card)

    print(f" Your hand: {user_card}, Your score: {user_score}")
    print(f" Opponent hand: {computer_card}, opponent score: {computer_score}")
    print(compare(user_score, computer_score))


while input("Do you want to play the game of black  jack 'y' to play 'n' otherwise") == "y":
    play_game()

