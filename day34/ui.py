from tkinter import *
from quiz_brain import Quizbrain

THEME_COLOR = "#375362"
FONT = ("Arial", 20, "italic")


class QuizInterface:
    def __init__(self):
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        self.label = Label(text="Score: 0", bg=THEME_COLOR)
        self.label.grid(row=0, column=1, columnspan=2)

        self.canvas = Canvas(width=300, height=250, bg="#ffffff")

        self.question = self.canvas.create_text(150, 125, text="", font=FONT)
        self.canvas.grid(row=1, column=1)

        self.right = PhotoImage(file="./day34/images/right 1.png")
        self.right_btn = Button(
            image=self.right, bg=THEME_COLOR, highlightthickness=0)
        self.right_btn.grid(row=2, column=0)

        self.wrong = PhotoImage(file="./day34/images/wrong 1.png")
        self.wrong_btn = Button(
            image=self.wrong, bg=THEME_COLOR, highlightthickness=0)
        self.wrong_btn.grid(row=2, column=1)

        self.window.mainloop()
