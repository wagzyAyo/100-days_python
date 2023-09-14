from tkinter import *

window = Tk()
window.title("My First GUI")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

# label
my_label = Label(text="I am a label", font=("Arial", 24, "bold"))
my_label.grid(column=0, row=0)

my_label.config(text="New text")


def clicked_button():
    print("I got clicked")
    value = input.get()
    my_label.config(text=value)


# button
button = Button(text="click me", command=clicked_button)
button.grid(column=1, row=1)

# input
input = Entry(width=10)
input.grid(column=3, row=3)

new_button = Button(text="click me now")
new_button.grid(column=2, row=0)


window.mainloop()
