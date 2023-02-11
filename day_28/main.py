import math
from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 


def reset_timer():
    root.after_cancel(id=str(timer))
    mi_label1.config(text="Timer")
    canvas.itemconfig(timer_text, text="00:00")
    mi_label2.config(text="")


# ---------------------------- TIMER MECHANISM ------------------------------- # 


def start_timer():
    global reps
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    reps += 1
    if reps <= 8:
        if reps % 2 != 0:
            count_down(work_sec)
            mi_label1.config(text="Work", fg=GREEN)
        elif reps != 8 and reps % 2 == 0:
            count_down(short_break_sec)
            mi_label1.config(text="short Break", fg=PINK)
        else:
            count_down(long_break_sec)
            mi_label1.config(text="Long Break", fg=RED)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 


def count_down(count):
    global timer
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        timer = root.after(1000, count_down, count-1)
    else:
        start_timer()
        mark = ''
        worked_time = math.floor(reps / 2)
        for i in range(worked_time):
            mark += "✓"
        mi_label2.config(text=mark)

# ---------------------------- UI SETUP ------------------------------- #


root = Tk()
root.title('Pomodoro')
root.config(padx=100, pady=50, bg=YELLOW)

mi_label1 = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 30, 'normal'))
mi_label1.grid(column=1, row=0)
mi_label2 = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 15, 'normal'))
mi_label2.grid(column=1, row=3)


mi_button = Button(text="Start", command=start_timer, font=(FONT_NAME, 10, 'normal'))
mi_button.grid(column=0, row=2)

mi_button1 = Button(text="Reset", command=reset_timer, font=(FONT_NAME, 10, 'normal'))
mi_button1.grid(column=2, row=2)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_ing = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_ing)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 15, 'bold'))
canvas.grid(column=1, row=1)

root.mainloop()
