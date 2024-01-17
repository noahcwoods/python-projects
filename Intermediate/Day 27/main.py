from tkinter import *


# window = Tk()
# window.title("Noah's Test GUI")
# window.minsize(1920, 1080)
#
# my_label = Label(text="Hello World!", font=("Arial", 24, "bold"))
# my_label.pack()
#
# my_label["text"] = "New Text Motherfucker!"
#
#
# def button_clicked():
#     my_label["text"] = input.get()
#
#
#
# button = Button(window, text="Help Me!", command=button_clicked)
# button.pack()
#
# input = Entry(width=10)
# input.pack()

def on_button_clicked() -> None:
    user_input_miles = float(entry.get())
    l3.config(text=f"{user_input_miles * 1.60934}")


converted_to_km: float = 0.0

master = Tk()
master.minsize(500, 500)

l1 = Label(master, text="Miles")
l2 = Label(master, text="is equal to")
l3 = Label(master, text="0", width=15)
l4 = Label(master, text="Km")

entry = Entry(master)

button = Button(master, text="Calculate", command=on_button_clicked)

entry.grid(row=0, column=1, sticky=W, padx=5, pady=5)
l1.grid(row=0, column=2, sticky=W, pady=2)
l2.grid(row=1, column=0, sticky=W, pady=2)
l3.grid(row=1, column=1, sticky=W, pady=2)
l4.grid(row=1, column=2, sticky=W, pady=2)
button.grid(row=2, column=1, sticky=W, padx=5, pady=5)

master.mainloop()
