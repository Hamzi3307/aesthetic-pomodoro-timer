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
check = "✔"
bg=YELLOW
fg=GREEN
reps = 0

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_screen():
    pass

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_screen():
    long = LONG_BREAK_MIN * 60
    short = SHORT_BREAK_MIN * 60
    work = WORK_MIN * 60
    global reps
    reps+=1
    if reps % 2 == 1:
        count_down(work)
        text_timer.config(text="Work",fg=RED)
    elif reps%8 == 0:
        count_down(long)
        text_timer.config(text="Take Tea",fg=GREEN)
    else:
        count_down(short)
        text_timer.config(text="Break",fg=PINK)
    # count_down(15*6, "work", 1)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min = math.floor(count/60)
    if count_min < 10:
        count_min = f"0{count_min}"
    count_sec = count%60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    timer = f"{count_min}:{count_sec}"
    if count>=0:    
        # print(count)
        canvas.itemconfig(timer_text, text=timer)
        window.after(10, count_down, count-1) # , action, turn)
    else:
        start_screen()    
        # if timer == "00:00" and action == "work":
        #     if turn == 4:
        #         count_down(10*6,  "break", turn)
        #     count_down(4*6, "break", turn)
        # elif timer == "00:00" and action == "break":
        #     if turn==4:
        #         print(f"{turn}:{action}")
        #     count_down(15*6, "work", turn+1)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 25, "bold"))
canvas.grid(column=2, row=2)

# count_down(5)

text_timer = Label(text="Timer", fg=GREEN, bg=bg, font=(FONT_NAME, 30, "bold"))
text_timer.grid(column=2, row=1)

check_timer = Label(text=check, fg=GREEN, bg=bg, font=(FONT_NAME, 30, "bold"))
check_timer.grid(column=2, row=4)

reset = Button(text="Reset", command=reset_screen, highlightthickness=0)
start = Button(text="Start", command=start_screen, highlightthickness=0)

reset.grid(column=1, row=3)
start.grid(column=3, row=3)

window.mainloop()