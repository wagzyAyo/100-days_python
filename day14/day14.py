from name import data
from art import logo, vs
import random


def compare(guess, a_dic, b_dic):
    '''Compares an int and return the 
    the one with most value
    '''
    if a_dic > b_dic:
        if guess == 'a':
            return True
    elif b_dic > a_dic:
        if guess == 'b':
            return True
    else:
        False


print(logo)
B = random.choice(data)
score = 0
game = True

while game:
    A = B
    B = random.choice(data)
    if A == B:
        B = random.choice(data)
    print(
        f"Compare A: {A['name']} a {A['description']} from {A['country']}")

    print(vs)

    print(
        f"with B: {B['name']} a {B['description']} from {B['country']}")
    select = (input("Who has the most Instagram followers 'A' or 'B': ")).lower()
    choice_A = A['followers_count']
    choice_B = B['followers_count']
    if compare(select, choice_A, choice_B):
        score += 1
        print(f"You're right! your score is {score}")
    else:
        print(f"wrong your total score is {score}")
        game = False
