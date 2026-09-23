from tkinter import *
import math

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
    global reps
    window.after_cancel(timer)
    label.config(text="Timer")
    canvas.itemconfig(timer_text, text=f"00:00")
    check_mark.config(text="")
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1

    if reps % 8 == 0:
        count_down(LONG_BREAK_MIN * 60 )
        label.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        count_down(SHORT_BREAK_MIN * 60 )
        label.config(text="Break", fg=PINK)
    else:
        count_down(WORK_MIN * 60)
        label.config(text="Work", fg=GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    minits = math.floor(count / 60)
    second = count % 60
    if minits < 10:
        minits = f"0{minits}"
    if second < 10:
        second = f"0{second}"
    canvas.itemconfig(timer_text, text=f"{minits}:{second}")
    if count > 0:
        # print(count)
        global timer
        timer = window.after(1000,count_down, count-1)
    else:
        start_timer()
        check = ""
        work_sesson = reps // 2
        for _ in range(work_sesson):
            check += "✔️"
        check_mark.config(text=check)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")

# label
label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 40 ,"bold"))
label.grid(column=1, row=0)

check_mark = Label(fg=GREEN)
check_mark.grid(column=1,row=3)

window.config(padx=100, pady=50, bg=YELLOW)
canvas = Canvas(width=200, height=224, bg=YELLOW)
tomato = PhotoImage(file="tomato.png")
canvas.create_image(102,112,image=tomato)
timer_text = canvas.create_text(102,130, text="00:00", fill="white", font=(FONT_NAME, 30 ,"bold"))
canvas.grid(column=1,row=1)


# button
start = Button(text="Start", command=start_timer)
start.grid(column=0,row=2)
reset = Button(text="Reset", command=reset_timer)
reset.grid(column=2,row=2)

# Checkbox
def checkbutton_used():
    print(checked_state.get())

checked_state = IntVar()
checkbutton = Checkbutton(variable=checked_state,fg=GREEN, command=checkbutton_used)
checked_state.get()

window.mainloop()
