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

canvas.create_text(300, 155, text="Title", font=("Ariel", 20, "italic"))
canvas.create_text(300, 220, text="Word", font=("Ariel", 30, "bold"))
canvas.grid(row=0, column=0)

wrong_image = PhotoImage(file="./day31/images/wrong 1.png")
wrong_btn = Button(image=wrong_image)
wrong_btn.grid(row=1, column=0)


right_image = PhotoImage(file="./day31/images/right 1.png")
right_btn = Button(image=right_image)
right_btn.grid(row=1, column=1)


window.mainloop()
