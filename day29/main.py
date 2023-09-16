from tkinter import *


def save():
    web = web_input.get()
    mail = mail_input.get()
    psw = psw_input.get()
    with open("data.text", mode="a") as file:
        file.write(f"{web} | {mail} | {psw}")


FONT_NAME = "Courier"


window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)


canvas = Canvas(width=200, height=114)
logo = PhotoImage(file="./day29/password 1.png")
canvas.create_image(100, 52, image=logo)
canvas.grid(row=0, column=1)


web_label = Label(text="Website:", font=(FONT_NAME))
web_label.grid(row=1, column=0)
web_input = Entry(width=35)
web_input.grid(row=1, column=1, columnspan=2)
web_input.focus()


mail_label = Label(text="Email/username:", font=(FONT_NAME))
mail_label.grid(row=2, column=0)
mail_input = Entry(width=35)
mail_input.grid(row=2, column=1, columnspan=2)
mail_input.insert(0, "talktoayo@hmail.com")


psw_label = Label(text="password:", font=(FONT_NAME))
psw_label.grid(row=3, column=0)
psw_input = Entry(width=21)
psw_input.grid(row=3, column=1)

gen_btn = Button(text="Generate password")
gen_btn.grid(row=3, column=2)

add_btn = Button(text="Add", width=36, command=save)
add_btn.grid(row=4, column=1, columnspan=2)


window.mainloop()
