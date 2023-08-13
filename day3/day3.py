print('''
      *******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************''')
print("Welcome to treasure island your mission is to find the lost treasure of your queen from the south")
side = input("You find yourself in enchated forest,where do u go from here? N  E S W\n")
if side == "N":
    decide = input("You find a river but no boat to cross ahead, what do you do? wait or swim?\n")
    if decide == "wait".lower():
       final = input("you wait for boat and make your way to an island, you find 3 doors red, yellow and blue:\nS")
       if final == "yellow".lower():
           print("You find the treasure!, you made your way south and return the treasure to your queen") 
           print("You are reward beyond measures!") 
           print("You win!")
       else:
           print(f"You enter {final} and see different beast!")
           print("you fight to your full strength, but died a hero!")
           print("Game over!")

    else:
        print("You try your luck to swim but drown in the enchated river!")
        print("Game over!")
elif side == "S":
    print("You return home, you are branded a coward by your people!")
    print("Game over!")
else:
    print(f"After walking through the {side} for 2 days you get tired and starving")
    survive = input("You find a hunt house with food and drinks inside what do you do? Enter or head south?\n")
    if survive == "Enter".lower():
        print("You fiest till sunset, you later hear a sound of beast nearby... oooh oh oooh! u are eaten by the beast")
        print("Game over !")
    elif survive == "south".lower():
        print("You find your way back home without the treasure!")
        print("Game over!")

