from turtle import Turtle, Screen
import random

timmy = Turtle()
timmy.shape("turtle")
timmy.color("orange")

colors = ["turquoise", "medium blue", "dark slate gray",
          "light steel blue", "dark goldenrod", "slate blue"]


direction = [0, 90, 180, 270]
timmy.width(15)
timmy.speed(0)

for _ in range(200):
    timmy.color(random.choice(colors))
    timmy.forward(30)
    timmy.setheading(random.choice(direction))


screen = Screen()
screen.exitonclick()
