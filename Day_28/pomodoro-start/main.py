import time
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
REPS = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 
def rst_btn():
    global REPS, timer
    # Ensure there is an active timer to cancel
    if timer:
        window.after_cancel(timer)
        # Reset the timer reference
        timer = None
    # Reset REPS to initial state
    REPS = 0
    # Reset UI label
    title_label.config(text="Timer", fg=GREEN)
    # Reset the timer display
    canvas.itemconfig(canvas_start_text, text="00:00")
    # Clear work session checkmarks
    work_checks.config(text="")

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global REPS
    work_sec = WORK_MIN * 60
    break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    # Forcing work timer at rep 0
    REPS += 1
    # Designating break and work conditions
    if REPS % 8 == 0:
        count_down(long_break_sec)
        title_label.config(text="Long Break", fg=RED)
    elif REPS % 2 == 0:
        count_down(break_sec)
        title_label.config(text="Short Break", fg=PINK)
    else:
        count_down(work_sec)
        title_label.config(text="Work", fg=GREEN)





# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    # Formatting Minutes and Seconds
    minutes = count // 60
    seconds = count % 60
    # Adding a leading 0 if there is less than ten seconds
    if seconds < 10:
        seconds = f"0{seconds}"
    # Update canvas display
    canvas.itemconfig(canvas_start_text, text=f"{minutes}:{seconds}")
    # Run the loop while valid
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        worksessions = REPS // 2
        for i in range(worksessions):
            marks += "✓"
        work_checks.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
# Initializing a Tk window
window = Tk()
# Title of the window
window.title("Pomodoro")
# Setting Window Geometry
window.config(padx=100, pady=50, bg=YELLOW)
# Creating the GUI canvas
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_image = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_image)

canvas_start_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=2)
start_button = Button(text="Start" ,fg=GREEN, bg=YELLOW, font=(FONT_NAME, 35, "bold"), command=start_timer)
start_button.grid(row=2, column=0)
reset_button = Button(text="Reset", fg=RED, bg=YELLOW, font=(FONT_NAME, 35, "bold"), command=lambda:rst_btn())
reset_button.grid(row=2, column=4)

title_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50, "bold"))
title_label.grid(row=0, column=2)

work_checks = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 15, "bold"))
work_checks.grid(row=3, column=2)



window.mainloop()