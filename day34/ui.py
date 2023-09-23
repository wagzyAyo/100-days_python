from tkinter import *
from quiz_brain import Quizbrain

THEME_COLOR = "#375362"
FONT = ("Ariel", 20, "italic")


class QuizInterface:
    def __init__(self, quiz_brain: Quizbrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        self.score_label = Label(text="Score: 0", bg=THEME_COLOR, fg="#ffffff")
        self.score_label.grid(row=0, column=2)

        self.canvas = Canvas(width=300, height=250, bg="#ffffff")

        self.question = self.canvas.create_text(
            150, 125, width=280, text="Some text", font=FONT)
        self.canvas.grid(row=1, column=1, pady=50)

        right = PhotoImage(file="./day34/images/right 1.png")
        self.right_btn = Button(
            image=right, bg=THEME_COLOR, highlightthickness=0, command=self.check_true)
        self.right_btn.grid(row=2, column=0,)

        wrong = PhotoImage(file="./day34/images/wrong 1.png")
        self.wrong_btn = Button(
            image=wrong, bg=THEME_COLOR, highlightthickness=0, command=self.check_false)
        self.wrong_btn.grid(row=2, column=2)
        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="#ffffff")
        self.score_label.config(text=f"score: {self.quiz.score}")
        if self.quiz.still_has_question():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question, text=q_text)
        else:
            self.canvas.itemconfig(
                self.question, text="You've reached the end of the quiz.")
            self.right_btn.config(state="disabled")
            self.wrong_btn.config(state="disabled")

    def check_true(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def check_false(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
