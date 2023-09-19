import pandas
from tkinter import *
import random

BACKGROUND_COLOR = "#B1DDC6"


data = pandas.read_csv("./day31/data/words.csv")
to_learn = data.to_dict(orient="records")


def next_card():
    current_card = random.choice(to_learn)
    print(current_card["French"])
    canvas.itemconfig(card_title, text="French")
    canvas.itemconfig(card_word, text=current_card["French"])


window = Tk()
window.title("Flashy")
window.config(padx=30, pady=30, bg=BACKGROUND_COLOR)

canvas = Canvas(width=600, height=404,
                bg=BACKGROUND_COLOR, highlightthickness=0)
image1 = PhotoImage(file="./day31/images/Rectangle 3.png")
canvas.create_image(300, 204, image=image1)

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
