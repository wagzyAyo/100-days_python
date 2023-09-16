from tkinter import *
window = Tk()
window.title("Password Manager")


canvas = Canvas(width=200, height=114)
logo = PhotoImage(file="./day29/password 1.png")
canvas.create_image(100, 52, image=logo)
canvas.pack()


window.mainloop()
