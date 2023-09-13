import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "./day25/blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)
data = pandas.read_csv("./day25/50_states.csv")
score = 0


all_state = data.state.to_list()
guess_state = []


while len(guess_state) < 50:
    answer_text = screen.textinput(
        title=f"{score}/50 Guess the state", prompt="What's another state").title()

    if answer_text in all_state:
        tim = turtle.Turtle()
        tim.hideturtle()
        tim.penup()
        state_data = data[data.state == answer_text]
        tim.goto(int(state_data.x), int(state_data.y))
        tim.write(answer_text)
        score += 1
        guess_state.append(answer_text)


screen.exitonclick()
