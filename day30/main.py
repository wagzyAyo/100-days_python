import random
from tkinter import *
from tkinter import messagebox
import pyperclip
import json

FONT_NAME = "Courier"


def save():
    web = web_input.get()
    mail = mail_input.get()
    psw = psw_input.get()
    new_data = {
        web: {
            "email": mail,
            "password": psw,
        }
    }

    if len(web) == 0 or len(mail) == 0:
        messagebox.showinfo(
            title="oops", message="Please dont leave any field empty!")

    else:
        try:
            with open("data.json", mode="r") as data_file:
                # Reading old data
                data = json.load(data_file)
                # Updating old data with new data

        except FileNotFoundError:
            with open("data.json", mode="w") as data_file:
                # Saving Updated data
                json.dump(new_data, data_file, indent=4)
        else:
            # Updating old data with new data
            data.update(new_data)
            with open("data.json", mode="w") as data_file:
                # Saving Updated data
                json.dump(data, data_file, indent=4)
        finally:
            web_input.delete(0, END)
            psw_input.delete(0, END)


# Paword generator
def psw_gen():

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
               'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
               ]
    numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '@', '#', '$', '%', '&', '^', '(', ')', '+']

    lett = random.randint(8, 10)
    numb = random.randint(2, 4)
    symb = random.randint(2, 4)

    password_letter = [random.choice(letters) for char in range(lett)]

    password_number = [random.choice(numbers) for number in range(numb)]

    password_symbols = [random.choice(symbols) for sym in range(symb)]

    password = password_letter + password_symbols + password_number

    random.shuffle(password)

    gen_psw = "".join(password)

    psw_input.insert(0, gen_psw)
    pyperclip.copy(gen_psw)


def find_password():
    web = web_input.get()
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)

    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No data found")
    else:
        if web in data:
            email = data[web]["email"]
            password = data[web]["password"]
            messagebox.showinfo(
                title=web, message=f"Email: {email}\npassword: {password}")
        else:
            messagebox.showinfo(
                title="Error", message=f"No details for {web} exists")


window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)


canvas = Canvas(width=200, height=114)
logo = PhotoImage(file="./day29/password 1.png")
canvas.create_image(100, 52, image=logo)
canvas.grid(row=0, column=1)


web_label = Label(text="Website:", font=(FONT_NAME))
web_label.grid(row=1, column=0)
web_input = Entry(width=21)
web_input.grid(row=1, column=1)
web_input.focus()
search_btn = Button(text="search", width=13, command=find_password)
search_btn.grid(row=1, column=2)


mail_label = Label(text="Email/username:", font=(FONT_NAME))
mail_label.grid(row=2, column=0)
mail_input = Entry(width=35)
mail_input.grid(row=2, column=1, columnspan=2)
mail_input.insert(0, "talktoayo@gmail.com")


psw_label = Label(text="password:", font=(FONT_NAME))
psw_label.grid(row=3, column=0)
psw_input = Entry(width=21)
psw_input.grid(row=3, column=1)

gen_btn = Button(text="Generate password", command=psw_gen)
gen_btn.grid(row=3, column=2)

add_btn = Button(text="Add", width=36, command=save)
add_btn.grid(row=4, column=1, columnspan=2)


window.mainloop()
