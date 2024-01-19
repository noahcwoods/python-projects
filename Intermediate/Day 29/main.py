from tkinter import *
from tkinter import messagebox
import random

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

    # Eazy Level - Order not randomised:
    # e.g. 4 letter, 2 symbol, 2 number = JduE&!91
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

    if len(user_email) == 0 or len(user_password) == 0:
        messagebox.showerror("ERROR", "DONT LEAVE EMPTY FIELDS")
    else:
        is_ok = messagebox.askokcancel(title=user_website,
                                       message=f"Please confirm:\nEmail: {user_email}\nPassword: {user_password}")
        if is_ok:
            with open("password.txt", "a") as f:
                f.write(f"{user_email} | {user_password} | {user_website}\n")

            website_entry.delete(0, END)
            password_entry.delete(0, END)


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

# Grid Layout
canvas.grid(row=0, column=1, )

website_label.grid(row=1, column=0)
email_label.grid(row=2, column=0)
password_label.grid(row=3, column=0)

website_entry.grid(row=1, column=1, columnspan=2)
email_entry.grid(row=2, column=1, columnspan=2)
password_entry.grid(row=3, column=1, columnspan=2)

generate_password.grid(row=3, column=3)
add_password.grid(row=4, column=1, columnspan=2)

# Display
window.mainloop()
