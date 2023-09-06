from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()
screen.listen()


def move_forward():
    tim.forward(10)


def move_backward():
    tim.backward(10)


def move_right():
    tim.right(10)


def move_left():
    tim.left(10)


screen.onkey(fun=move_forward, key="w")
screen.onkey(fun=move_backward, key="s")
screen.onkey(fun=move_right, key="a")
screen.onkey(fun=move_left, key="d")

screen.exitonclick()
