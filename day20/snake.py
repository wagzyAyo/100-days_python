from turtle import Turtle

INITIAL_POSITION = [(0, 0), (-20, 0), (-40, 0)]


class Snake:

    def __init__(self):
        self.segment = []
        self.create_snake()

    def create_snake(self):
        for position in INITIAL_POSITION:
            fragment = Turtle(shape="square")
            fragment.color("white")
            fragment.penup()
            fragment.goto(position)
            self.segment.append(fragment)

    def move(self):

        for seg_num in range(len(self.segment) - 1, 0, -1):
            new_x = self.segment[seg_num - 1].xcor()
            new_y = self.segment[seg_num - 1].ycor()
            self.segment[seg_num].goto(new_x, new_y)
        self.segment[0].forward(20)
