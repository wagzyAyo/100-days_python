#!/usr/bin/python3
# Fizz buzz debug
number = range(1 -101)
for x in number:
    if x % 3 == 0 and number % 5 == 0:
        print("Fizz Buzz")
    elif x % 3 == 0:
        print("Fizz")
    elif x % 5 == 0:
        print("Buzz")
    else:
        print(x)

