import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "./day25/blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)
data = pandas.read_csv("./day25/50_states.csv")


all_state = data.state.to_list()
guess_state = []


while len(guess_state) < 50:
    answer_text = screen.textinput(
        title=f"{len(guess_state)}/50 Guess the state", prompt="What's another state").title()
    if answer_text == "Exit":
        missing_state = [
            state for state in all_state if state not in guess_state]

        df = pandas.DataFrame(missing_state)
        df.to_csv("./day25/state_to_learn.csv")
        break
    if answer_text in all_state:
        tim = turtle.Turtle()
        tim.hideturtle()
        tim.penup()
        state_data = data[data.state == answer_text]
        tim.goto(int(state_data.x), int(state_data.y))
        tim.write(answer_text)
        guess_state.append(answer_text)

# State to learn.csv
