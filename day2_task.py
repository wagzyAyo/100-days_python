weight = input(
    "Hello there, welcome calculate your BMI here\nWhat is your weight in (kg): ")
height = input("What is your height in (meters): ")
weight = int(weight)
height = int(height)
BMI = weight / height ** height
if BMI <= 18.5:
    w = "underweigth"
if BMI > 18.5:
    w = "normal"
if BMI > 25 and BMI < 30:
    w = "overweight"
if BMI > 30 and BMI < 35:
    w = "obese"
if BMI > 35:
    w = "chronically obese"
print("Your BMI is {},you are {}".format(BMI,w))
