from tkinter import *

window = Tk()
window.title("My First GUI")
window.minsize(width=500, height=300)


my_label = Label(text="I am a label", font=("Arial", 24, "bold"))
my_label.pack()

my_label.config(text="New text")


def clicked_button():
    print("I got clicked")


button = Button(text="click me", command=clicked_button)
button.pack()

window.mainloop()
