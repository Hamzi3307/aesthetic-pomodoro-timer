from tkinter import *
import math
import time
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 5
SHORT_BREAK_MIN = 1
LONG_BREAK_MIN = 3
REPS = 0

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_screen():
    global REPS
    REPS = 0
    check_title.config(text="")
    window.after_cancel(session)
    text_title.config(text="Work",fg=RED)
    count_down(WORK_MIN*60)

def pause_screen():
    time.sleep(10)

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_screen():
    long = LONG_BREAK_MIN * 60
    short = SHORT_BREAK_MIN * 60
    work = WORK_MIN * 60
    global REPS
    REPS+=1
    if REPS % 2 == 1:
        count_down(work)
        text_title.config(text="Work",fg=RED)
    elif REPS%8 == 0:
        count_down(long)
        text_title.config(text="Take Tea",fg=GREEN)
    else:
        count_down(short)
        text_title.config(text="Break",fg=PINK)
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
        global session  
        # print(count)
        canvas.itemconfig(timer_text, text=timer)
        session = window.after(10, count_down, count-1) # , action, turn)
    else:
        start_screen()
        CHECK = ""
        for _ in range(math.floor(REPS/2)): 
            CHECK += "✔"
        check_title.config(text=CHECK)
            
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
canvas.create_image(100, 105, image=img)
timer_text = canvas.create_text(100, 120, text="00:00", fill="white", font=(FONT_NAME, 25, "bold"))
canvas.grid(column=2, row=2)

# count_down(5)

text_title = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 30, "bold"))
text_title.grid(column=2, row=1)

check_title = Label(text="", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 30, "bold"))
check_title.grid(column=2, row=4)

reset = Button(text="Reset", command=reset_screen, highlightthickness=0)
pause = Button(text="Pause", command=pause_screen, highlightthickness=0)
start = Button(text="Start", command=start_screen, highlightthickness=0)

reset.grid(column=1, row=3)
pause.grid(column=2, row=3)
start.grid(column=3, row=3)

window.mainloop()