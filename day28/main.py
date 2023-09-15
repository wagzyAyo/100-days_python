from tkinter import *
# Constants

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BRAEK_MIN = 5
LONG_BREAK_MIN = 20


window = Tk()
window.title("Pamadoro")
window.config(padx=100, pady=50, bg=YELLOW)

title = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50,))
title.grid(column=1, row=0)

tomato_img = PhotoImage(file="./day28/tomato 2.png")
canvas = Canvas(width=202, height=204, bg=YELLOW, highlightthickness=0)
canvas.create_image(101, 102, image=tomato_img)
canvas.grid(column=1, row=1)
canvas.create_text(101, 102, text="00:00", fill="white",
                   font=(FONT_NAME, 35, "bold"))


start_button = Button(text="Start", highlightthickness=0)
start_button.grid(column=0, row=2)


reset_button = Button(text="Reset", highlightthickness=0)
reset_button.grid(column=2, row=2)


check_marks = Label(text="✔", fg=GREEN, bg=YELLOW)
check_marks.grid(column=1, row="3")

window.mainloop()
