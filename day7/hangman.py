import random
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
      |
      |
      |
      |
=========''']
word_list = ["ardverk", "baboon", "camel"]
chosen_word = random.choice(word_list)
chance = []
for x in chosen_word:
    chance += "_"
lives = 6
end_of_game = False

while end_of_game == False:
    guess = input("Guess a letter: ")
    guess = guess.lower()

    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            chance[position] = letter
    print(chance)
    print(stages[lives])
    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("you lose!")

    if "_" not in chance:
        end_of_game = True
        print("You Win!")
