import random
# Rock
Rock = ("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")

# Paper
Paper = ("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")

# Scissors
Scissors = ("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")
game_images = [Rock, Paper, Scissors]
choice = int(input("Enter 0 for Rock, 1 for Paper, 2 for Scissors:\n"))

if choice < 0 or choice >= 3:
    print("You select wrong number!")
    print("You Lose!")
else:
    computer = random.randint(0, 2)
    print(game_images[choice])
    print("You chose {}".format(choice))
    print(game_images[computer])

    if choice == computer:
        print("computer chose {}".format(computer))
        print("Draw!")
    elif choice == 0 and computer == 2:
        print("computer chose {}".format(computer))
        print("You Win!")
    elif choice == 1 and computer == 0:
        print("computer chose {}".format(computer))
        print("You Win!")
    elif choice == 2 and computer == 1:
        print("computer chose {}".format(computer))
        print("You Win!")
    else:
        print("computer chose {}".format(computer))
        print("You Lose!")
