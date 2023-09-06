from turtle import Turtle, Screen
import time


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
segment = []


initial_position = [(0, 0), (-20, 0), (-40, 0)]
for position in initial_position:
    fragment = Turtle(shape="square")
    fragment.color("white")
    fragment.penup()
    fragment.goto(position)
    segment.append(fragment)


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    for seg_num in range(len(segment) - 1, 0, -1):
        new_x = segment[seg_num - 1].xcor()
        new_y = segment[seg_num - 1].ycor()
        segment[seg_num].goto(new_x, new_y)
    segment[0].forward(20)


screen.exitonclick()
