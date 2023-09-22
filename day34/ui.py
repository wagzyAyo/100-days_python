from tkinter import *
from quiz_brain import Quizbrain

THEME_COLOR = "#375362"
FONT = ("Arial", 20, "italic")


class QuizInterface:
    def __init__(self):
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        self.score_label = Label(text="Score: 0", bg=THEME_COLOR, fg="#ffffff")
        self.score_label.grid(row=0, column=2)

        self.canvas = Canvas(width=300, height=250, bg="#ffffff")

        self.question = self.canvas.create_text(
            150, 125, text="Some text", font=FONT)
        self.canvas.grid(row=1, column=1, pady=50)

        right = PhotoImage(file="./day34/images/right 1.png")
        self.right_btn = Button(
            image=right, bg=THEME_COLOR, highlightthickness=0)
        self.right_btn.grid(row=2, column=0,)

        wrong = PhotoImage(file="./day34/images/wrong 1.png")
        self.wrong_btn = Button(
            image=wrong, bg=THEME_COLOR, highlightthickness=0)
        self.wrong_btn.grid(row=2, column=2)

        self.window.mainloop()
