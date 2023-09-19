from tkinter import *
BACKGROUND_COLOR = "#B1DDC6"
ASH = "#C0BFBF"
window = Tk()
window.title("Flashy")
window.config(padx=30, pady=30, bg=BACKGROUND_COLOR)

canvas = Canvas(width=600, height=404,
                bg=BACKGROUND_COLOR, highlightthickness=0)
image1 = PhotoImage(file="./day31/images/Rectangle 3.png")
canvas.create_image(300, 204, image=image1)
canvas.grid(row=0, column=0)


text_top = Label(text="Title")
text_top.grid(row=0, column=0)


window.mainloop()
