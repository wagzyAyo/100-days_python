import random
print("Welcome to the Number Guessing game!")
print("I'm thinking of a number between 1 and 100")
range_number = range(1, 101)
THE_NUMBER = random.choice(range_number)
ATTEMPT = 0

level = input("Choose a difficulty, Type 'easy' or 'hard': ").lower()
if level == 'easy':
    ATTEMPT = 10
elif level == 'hard':
    ATTEMPT = 5


def compare(number, guess):
    '''Compares two integers and return output'''
    if number == guess:
        return "You win"
    if number > guess:
        return "Too low"
    else:
        return "Too high"


while ATTEMPT != 0:
    print(f"You have {ATTEMPT} guess")
    GUESS = int(input("make a guess: "))
    result = compare(THE_NUMBER, GUESS)
    print(result)
    if result == "You win":
        break
    ATTEMPT -= 1
if ATTEMPT == 0:
    print("Better luck next time!")

