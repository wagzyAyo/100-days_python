weight = input(
    "Hello there, welcome calculate your BMI here\nWhat is your weight in (kg): ")
height = input("What is your height in (meters): ")
weight = int(weight)
height = int(height)
BMI = weight / height ** 2
print("Your BMI is {}".format(BMI))
