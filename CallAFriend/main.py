import random
from tkinter import *
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"

# function to select a friend from given list without repetition
def call_a_friend():
    my_friends = ["Skifin", "Nayana", "Sanduana", "Navya", "Arya",
                  "Issac", "Eric", "Ramya", "Devika", "Archana", "Nayana JY", "Sanil", "Yadu"]
    with open(file="called_list.txt", mode="r") as file:
        called_list = file.read().splitlines()
    on = True
    while on:
        if len(called_list) == 13:
            cycle_display.config(text="Completed")
            called_list.clear()
            with open(file="called_list.txt", mode="w") as file:
                file.write("")
        else:
            cycle_display.config(text="")
        friend = random.choice(my_friends)
        if friend not in called_list:
            with open(file="called_list.txt", mode="a") as file:
                file.write(str(friend) + "\n")
            friend_display.config(text=friend)
            on=False


# GUI
window = Tk()
window.title("Call A Friend")
window.minsize(width=200, height=200)
window.config( bg=YELLOW)
button = Button(text="Choose!", fg=RED, bg=PINK, font=(FONT_NAME, 12, "bold"), highlightthickness=0, command=call_a_friend)
button.size()
button.grid(row=2, column=0)
title_display = Label(text="CALL A FRIEND", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 20, "bold"))
title_display.grid(row=0, column=0)
friend_display = Label(text="", fg=PINK, bg=YELLOW, font=(FONT_NAME, 20, "bold"))
friend_display.grid(row=1, column=0)
cycle_display = Label(text="", fg=RED, bg=YELLOW, font=(FONT_NAME, 20, "bold"))
cycle_display.grid(row=3, column=0)
window.mainloop()
