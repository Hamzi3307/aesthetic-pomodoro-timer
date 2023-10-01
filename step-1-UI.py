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
check = "✔"
bg=YELLOW
fg=GREEN

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
img = PhotoImage(file="tomato.png")
canvas.create_image(100, 105, image=img)
timer_text = canvas.create_text(100, 120, text="00:00", fill="white", font=(FONT_NAME, 25, "bold"))
canvas.grid(column=2, row=2)

timer = Label(text="Timer", fg=GREEN, bg=bg, font=(FONT_NAME, 30, "bold"))
timer.grid(column=2, row=1)

timer = Label(text=check, fg=GREEN, bg=bg, font=(FONT_NAME, 30, "bold"))
timer.grid(column=2, row=4)

reset = Button(text="Reset", highlightthickness=0)
pause = Button(text="Pause", highlightthickness=0)
start = Button(text="Start", highlightthickness=0)

reset.grid(column=1, row=3)
pause.grid(column=2, row=3)
start.grid(column=3, row=3)

window.mainloop()