from tkinter import *
import random
import pandas as pd

BACKGROUND_COLOR = "#B1DDC6"
MAIN_FONT = ("Arial", 20, "bold")
MAIN_FONT_ITALIC = ("Arial", 20, "italic")
master = Tk()
FLASHCARD_FRONT = PhotoImage(file="images/card_front.png")
FLASHCARD_BACK = PhotoImage(file="images/card_back.png")
CORRECT = PhotoImage(file="images/right.png")
WRONG = PhotoImage(file="images/wrong.png")
DATA = pd.read_csv("data/french_words.csv")

to_learn = DATA.to_dict(orient="records")
_card_front = True
timer = None
current_word = None


# WORD SELECTION
def select_word():
    global timer
    global current_word
    current_word = random.choice(to_learn)
    canvas.itemconfig(_displayed_language, text="French")
    _displayed_word.config(text=current_word["French"])

    timer = master.after(3000, flip_card)


def new_word():
    global _card_front
    master.after_cancel(timer)

    if not _card_front:
        flip_card()
    select_word()


# Correct Button Event
def on_correct_selection():
    new_word()


# Wrong Button Event
def on_wrong_selection():
    new_word()


def flip_card():
    global _card_front
    if _card_front:
        canvas.itemconfig(_card_displayed, image=FLASHCARD_BACK)
        canvas.itemconfig(_displayed_language, fill="white", text="English")
        _displayed_word.config(fg="white", bg="#91C2AF", text=current_word["English"])

        _card_front = False

    else:
        canvas.itemconfig(_card_displayed, image=FLASHCARD_FRONT)
        canvas.itemconfig(_displayed_language, fill="black", text="French")
        _displayed_word.config(fg="black", bg="white")
        _card_front = True


# UI CONFIGURATION
master.title("Flashy!")
master.minsize(width=900, height=626)
master.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(master)
canvas.config(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
_card_displayed = canvas.create_image(400, 263, image=FLASHCARD_FRONT)

# LABELS
_displayed_language = canvas.create_text(400, 150, text="LANGUAGE", font=MAIN_FONT_ITALIC)
_displayed_word = Label(master, text="PLACEHOLDER", font=MAIN_FONT, fg="black", bg="white")

# BUTTONS
correct_button = Button(master, text="", image=CORRECT, highlightthickness=0, command=on_correct_selection)
wrong_button = Button(master, text="", image=WRONG, highlightthickness=0, command=on_wrong_selection)

# GRID CONFIGURATION
canvas.grid(row=0, column=0, columnspan=2)

_displayed_word.grid(row=0, column=0, columnspan=2)

correct_button.grid(row=1, column=0)
wrong_button.grid(row=1, column=1)

select_word()

master.mainloop()
