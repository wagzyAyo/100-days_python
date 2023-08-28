import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def deal_card():
    card = random.choice(cards)
    return card


def calculate_score(cards):
    '''Take a list of card and return the score calculated from the list of card'''
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


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

