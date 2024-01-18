from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    global reps
    window.after_cancel(timer)
    reps = 0
    bottom_label.config(text="")
    top_label.config(text="Timer")
    canvas.itemconfig(timer_text, text="00:00")




# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break = SHORT_BREAK_MIN * 60
    long_break = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        countdown(long_break)
        top_label.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        countdown(short_break)
        top_label.config(text="Break", fg=PINK)
    else:
        countdown(work_sec)
        top_label.config(text="Work", fg=GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def countdown(count):
    minutes_remaining = math.floor(count / 60)
    seconds_remaining = count % 60

    if seconds_remaining <= 9:
        seconds_remaining = "0" + str(seconds_remaining)

    if minutes_remaining <= 9:
        minutes_remaining = "0" + str(minutes_remaining)

    formatted_string = f"{minutes_remaining}:{seconds_remaining}"

    canvas.itemconfig(timer_text, text=formatted_string)

    if count > 0:
        global timer
        timer = window.after(1000, countdown, count - 1)
    else:
        start_timer()
        if reps % 2 == 0:
            checkmark = u'\u2713'
            bottom_label["text"] += checkmark



# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro Timer")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
image = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=image)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))

top_label = Label(text="Timer", font=(FONT_NAME, 35, "bold"), bg=YELLOW, fg=GREEN, pady=0)
top_label.grid(row=0, column=1)

bottom_label = Label(pady=20, bg=YELLOW, fg=GREEN, font=(FONT_NAME, 15, "bold"))
bottom_label.grid(row=3, column=1)

start_button = Button(text="Start", font=(FONT_NAME, 12, "bold"), command=start_timer)
reset_button = Button(text="Reset", font=(FONT_NAME, 12, "bold"), command=reset_timer)

start_button.grid(row=2, column=0)
reset_button.grid(row=2, column=2)

canvas.grid(row=1, column=1)




window.mainloop()
