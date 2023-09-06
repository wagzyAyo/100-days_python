from turtle import Turtle, Screen
import turtle
import random

timmy = Turtle()
timmy.shape("turtle")
turtle.colormode(255)


def random_colors():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


timmy.speed("fastest")


def spiral_graph(size):
    for _ in range(int(360 / size)):
        timmy.color(random_colors())
        timmy.circle(100)
        timmy.setheading(timmy.heading() + size)


spiral_graph(5)
screen = Screen()
screen.exitonclick()
