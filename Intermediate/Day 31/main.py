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

_french_word = None
_english_word = None
_random_index = None

# POPULATE DATA ###############################################################

# FRENCH SELECTION
def select_word():
    global _french_word
    global _english_word
    global _random_index

    _random_index = random.randint(0, len(DATA))

    try:
        _french_word = DATA.French[_random_index]
        _english_word = DATA.English[_random_index]
    except KeyError:
        print("French Word Selection Error: Index out of range")


# UI SETUP ###############################################################
master.title("Flashy!")
master.minsize(width=900, height=626)
master.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(master)
canvas.config(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)


# LABELS
_displayed_language = canvas.create_text(400, 150, text="LANGUAGE", font=MAIN_FONT_ITALIC)
_displayed_word = Label(master, text="PLACEHOLDER", font=MAIN_FONT, fg="black")

# BUTTONS
correct_button = Button(master, text="", image=CORRECT, highlightthickness=0)
wrong_button = Button(master, text="", image=WRONG, highlightthickness=0)

# GRID CONFIGURATION
canvas.grid(row=0, column=0, columnspan=2)

_displayed_word.grid(row=0, column=0, columnspan=2)

correct_button.grid(row=1, column=0)
wrong_button.grid(row=1, column=1)


select_word()

master.mainloop()
