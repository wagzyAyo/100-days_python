from turtle import Turtle, Screen
import random

timmy = Turtle()
timmy.shape("turtle")

colors = ["turquoise", "medium blue", "dark slate gray",
          "light steel blue", "dark goldenrod", "slate blue"]


def random_colors():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    colors = (r, g, b)
    return colors


timmy.circle(100)
timmy.speed(0)


screen = Screen()
screen.exitonclick()
