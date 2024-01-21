from json import JSONDecodeError
from tkinter import *
from tkinter import messagebox
import random
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def on_generate_password():
    password_entry.delete(0, END)

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
               'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
               'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
               'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    print("Welcome to the PyPassword Generator!")
    nr_letters = 6
    nr_symbols = 5
    nr_numbers = 4

    selectedLetters = ""
    selectedSymbols = ""
    selectedNumbers = ""

    for num in range(nr_letters):
        selectedLetters += random.choice(letters)
    for num in range(nr_symbols):
        selectedSymbols += random.choice(symbols)
    for num in range(nr_numbers):
        selectedNumbers += random.choice(numbers)

    password = selectedLetters + selectedSymbols + selectedNumbers
    password = list(password)
    random.shuffle(password)
    password = "".join(password)

    password_entry.insert(0, password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def on_add_password():
    user_email = email_entry.get()
    user_password = password_entry.get()
    user_website = website_entry.get()
    new_data = {
        user_website: {
            "email": user_email,
            "password": user_password,
        }
    }

    try:
        file = open("password.json")
    except FileNotFoundError:
        file = open("password.json", "w")
    finally:
        file.close()

    if len(user_email) == 0 or len(user_password) == 0:
        messagebox.showerror("ERROR", "DONT LEAVE EMPTY FIELDS")
    else:
        with open("password.json", "r") as f:
            # json.dump(new_data, f, indent=4)
            try:
                data = json.load(f)
                data.update(new_data)
            except JSONDecodeError:
                data = new_data
        with open("password.json", "w") as f:
            json.dump(data, f, indent=4)

        website_entry.delete(0, END)
        password_entry.delete(0, END)


def on_search_password():
    user_website = website_entry.get()

    try:
        with open("password.json", "r") as f:
            data = json.load(f)
            requested_password = data.get(user_website)["password"]
            requested_username = data.get(user_website)["email"]
    except TypeError as err2:
        messagebox.showerror("ERROR", f"No Website password is saved for that website")
    else:
        messagebox.showinfo("Website Info", f"Username: {requested_username}\nPassword: {requested_password}")

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.config(padx=50, pady=50)
window.title("Password Manager")

# Canvas
canvas = Canvas(width=200, height=200)
image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=image)

# Labels
website_label = Label(text="Wesbite:")
email_label = Label(text="Email/Username:")
password_label = Label(text="Password:")

# Inputs
website_entry = Entry(width=35)
website_entry.focus()
email_entry = Entry(width=35)
email_entry.insert(0, "noahcwoods@gmail.com")
password_entry = Entry(width=35)

# Buttons
generate_password = Button(text="Generate Password", width=14, command=on_generate_password)
add_password = Button(text="Add", width=26, command=on_add_password)
get_password = Button(text="Search", width=26, command=on_search_password)

# Grid Layout
canvas.grid(row=0, column=1, )

website_label.grid(row=1, column=0)
email_label.grid(row=2, column=0)
password_label.grid(row=3, column=0)

website_entry.grid(row=1, column=1, columnspan=2)
email_entry.grid(row=2, column=1, columnspan=2)
password_entry.grid(row=3, column=1, columnspan=2)

generate_password.grid(row=3, column=3)
add_password.grid(row=4, column=1, columnspan=1)
get_password.grid(row=4, column=2, columnspan=2)

# Display
window.mainloop()
