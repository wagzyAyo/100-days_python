from tkinter import *

window = Tk()
window.title("Miles to kilometer converter")
window.minsize(width=200, height=200)
window.config(padx=20, pady=20)


def calculate():
    value = int(input.get())
    km = int(value * 1.61)
    my_label_ans.config(text=km)


# Entry
input = Entry(width=10)
input.grid(column=1, row=0)

# Label
my_label = Label(text="Miles", font=("Arial", 15))
my_label.grid(column=3, row=0)


# Label is equal to
my_label = Label(text="Is equal to", font=("Arial", 15))
my_label.grid(column=1, row=1)

# Answer
my_label_ans = Label(text="0", font=("Arial", 15, "bold"))
my_label_ans.grid(column=2, row=1)

# Km
my_label_km = Label(text="Km", font=("Arial", 15, "bold"))
my_label_km.grid(column=3, row=1)


# button
button = Button(text="Calculate", command=calculate)
button.grid(column=2, row=2)


window.mainloop()
