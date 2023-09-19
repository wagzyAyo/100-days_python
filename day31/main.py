import pandas
from tkinter import *
import random

BACKGROUND_COLOR = "#B1DDC6"


data = pandas.read_csv("./day31/data/words.csv")
to_learn = data.to_dict(orient="records")
current_card = {}


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(card_background, image=image1)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image=image2)


window = Tk()
window.title("Flashy")
window.config(padx=30, pady=30, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)
canvas = Canvas(width=600, height=404,
                bg=BACKGROUND_COLOR, highlightthickness=0)
image1 = PhotoImage(file="./day31/images/Rectangle 3.png")
card_background = canvas.create_image(300, 204, image=image1)
# Back image
image2 = PhotoImage(file="./day31/images/Rectangle 4.png")

card_title = canvas.create_text(
    300, 155, text="", font=("Ariel", 20, "italic"))
card_word = canvas.create_text(
    300, 220, text="", font=("Ariel", 30, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

wrong_image = PhotoImage(file="./day31/images/wrong 1.png")
wrong_btn = Button(image=wrong_image, bg=BACKGROUND_COLOR,
                   highlightthickness=0, command=next_card)
wrong_btn.grid(row=1, column=0)


right_image = PhotoImage(file="./day31/images/right 1.png")
right_btn = Button(image=right_image, bg=BACKGROUND_COLOR,
                   highlightthickness=0, command=next_card)
right_btn.grid(row=1, column=1)


next_card()


window.mainloop()
