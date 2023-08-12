print("Welcome to love Calculator!")
your_name = input("What is your name? \n")
there_name = input("What is there name? \n")
# For true ##
name1 = int((your_name.lower().count("t")))
name1 += (your_name.lower().count("r"))
name1 += (your_name.lower().count("u"))
name1 += (your_name.lower().count("e"))

# there name
name2 = int((there_name.lower().count("t")))
name2 += int((there_name.lower().count("r")))
name2 += int((there_name.lower().count("u")))
name2 += int((there_name.lower().count("e")))

score1 = name1 + name2
score1 = str(score1)

# For Love
name1_2 = int((your_name.lower().count("l")))
name1_2 += int((your_name.lower().count("o")))
name1_2 += int((your_name.lower().count("v")))
name1_2 += int((your_name.lower().count("e")))

# There name
name2_2 = int((there_name.lower().count("t")))
name2_2 += int((there_name.lower().count("r")))
name2_2 += int((there_name.lower().count("u")))
name2_2 += int((there_name.lower().count("e")))

score2 = name1_2 + name2_2
score2 = str(score2)

score = score1 + score2
score = int(score)
if score < 10 and score > 90:
    print(f"Your score is {score},you go together like coke and mentos")
elif score >= 40 and score <= 50:
    print(f"Your score is {score},you are alright together")
else:
    print(f"Your score is {score}")
