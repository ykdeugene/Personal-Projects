from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
TICK = "✔"
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #


def reset_timer():
    global reps
    reps = 0
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    tick_text.config(text="Click start and start working now!", fg="black", bg=YELLOW)
    timer_label.config(text="Timer")


# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if reps % 2 == 1:
        timer_label.config(text="Work", fg=GREEN)
        count_down(work_sec)
    elif reps == 8:
        timer_label.config(text="Break", fg=PINK)
        count_down(long_break_sec)
    elif reps % 2 == 0:
        timer_label.config(text="Break", fg=RED)
        count_down(short_break_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):
    count_sec = int(count % 60)
    count_min = int((count - count_sec) / 60)

    if count_sec < 10:
        count_sec = f"0{count_sec}"
    elif count_sec == 0:
        count_sec = "00"

    if count_min < 10:
        count_min = f"0{count_min}"
    elif count_min == 0:
        count_min = "00"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")

    if count >= 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        if reps % 2 == 0:
            number_of_ticks = int(reps/2)
            total_ticks_str = int(reps/2) * TICK
            tick_text.config(text=total_ticks_str, fg=GREEN)


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)
reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)

timer_label = Label(text="Timer", font=(FONT_NAME, 50), bg=YELLOW, fg=GREEN)
timer_label.grid(column=1, row=0)
tick_text = Label(text="Click start and start working now!", fg="black", bg=YELLOW)
tick_text.grid(column=1, row=3)

window.mainloop()
