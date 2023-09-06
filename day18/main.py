import turtle
from turtle import Turtle
import random

turtle.colormode(255)
tim = Turtle()

color_list = [(202, 164, 109), (238, 240, 245), (150, 75, 49,), (223, 201, 135), (152, 93, 124), (172, 154, 40), (140, 30, 19), (30, 68, 100),
              (107, 127, 153), (107, 127, 153), (174, 94, 97), (176, 192, 209), (18, 86, 90), (81, 148, 129), (152, 93, 90)]
tim.speed("fastest")
tim.penup()
tim.hideturtle()
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 101

for dot_count in range(1, number_of_dots):

    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)


screen = turtle.Screen()
screen.exitonclick()
