from turtle import Turtle, Screen
import random

timmy = Turtle()
timmy.shape("turtle")
timmy.color("orange")

colors = ["turquoise", "medium blue", "dark slate gray",
          "light steel blue", "dark goldenrod", "slate blue"]


def draw_shape(num_of_sides):
    angle = 360 / num_of_sides
    for _ in range(num_of_sides):
        timmy.forward(100)
        timmy.right(angle)


for shape_side_n in range(3, 10):
    timmy.color(random.choice(colors))
    draw_shape(shape_side_n)


screen = Screen()
screen.exitonclick()
