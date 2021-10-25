from tkinter import *
import math
from winsound import PlaySound, SND_ASYNC

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25*60
SHORT_BREAK_MIN = 5*60
LONG_BREAK_MIN = 20*60
reps = 0
timer = None
n = 0


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global reps
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    l1.config(text="Timer", fg=GREEN)
    check_marks.config(text="")
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1
    if reps % 8 == 0:
        count_down(LONG_BREAK_MIN)
        l1.config(text="Long Break", fg=RED)
        PlaySound("alarm.wav", SND_ASYNC)
    elif reps % 2 == 0:
        count_down(SHORT_BREAK_MIN)
        l1.config(text="Short Break", fg=PINK)
        PlaySound("alarm.wav", SND_ASYNC)
    else:
        #if reps != 1:
        PlaySound("alarm.wav", SND_ASYNC)
        count_down(WORK_MIN)
        l1.config(text="Work")


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if len(str(count_sec)) == 1:
        count_sec = f"0{count_sec}"
    if len(str(count_min)) == 1:
        count_min = f"0{count_min}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count >= 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        global n
        start_timer()
        mark = ""
        session = reps - (8 * n)
        if reps % 8 == 0:
            n = n + 1
        for _ in range(math.floor(session / 2)):
            if len(mark) < 4:
                mark += "✔"
        check_marks.config(text=mark)


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

l1 = Label(text="TIMER", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 20, "bold"))
l1.grid(row=0, column=1)

b1 = Button(text="Start", fg=RED, bg=PINK, font=(FONT_NAME, 12, "bold"),
            highlightthickness=0, command=start_timer)
b1.grid(row=2, column=0)

b2 = Button(text="Reset", fg=RED, bg=PINK, font=(FONT_NAME, 12, "bold"),
            highlightthickness=0, command=reset_timer)
b2.grid(row=2, column=2)

check_marks = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 12, "bold"))
check_marks.grid(row=3, column=1)

window.mainloop()
