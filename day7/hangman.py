import random
from hangman_words import word_list
from hangman import logo, stages

chosen_word = random.choice(word_list)
chance = []
for x in chosen_word:
    chance += "_"
lives = 6
end_of_game = False
print(logo)
while end_of_game == False:
    guess = input("Guess a letter: ")
    guess = guess.lower()

    if guess in chance:
        print(f"You alraedy guessed {guess}")

    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            chance[position] = letter
    print(chance)
    print(stages[lives])
    if guess not in chosen_word:
        print(f"You guess {guess},Not in the chosen world, you loose a life")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("you lose!")

    if "_" not in chance:
        end_of_game = True
        print("You Win!")
