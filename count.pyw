import tkinter as tk
import time, keyboard

main_win = tk.Tk()

window_width = 300
window_height = 100

count = 0

screen_width = main_win.winfo_screenwidth()
screen_height = main_win.winfo_screenheight()

x = int((screen_width / 2) - (window_width / 2))
y = int((screen_height / 2) - (window_height / 2))

main_win.geometry(f"{window_width}x{window_height}+{x}+{0}")
main_win.wm_attributes("-topmost", True)
# main_win.attributes('-alpha', 0.5)
main_win.attributes("-transparentcolor", "#ab23ff")
main_win.resizable(width=False, height=False)
main_win["bg"] = "#ab23ff"
main_win.config(highlightbackground='#ab23ff')
main_win.overrideredirect(True)

main_win.title("Count Numbers")


frame = tk.Frame(main_win, padx=10, pady=5, bg="#ab23ff")
frame.pack()

# fcenter = tk.Frame(frame)
# fcenter.pack()

Lebel = tk.Label(frame, height=1, font=(
    "Helvetica", 16), fg="#fff", bg="#ab23ff")
Lebel.pack()

frame_button = tk.Frame(main_win, padx=10, pady=10, bg="#ab23ff")
frame_button.pack(side='bottom')

frame_center = tk.Frame(frame_button, bg="#ab23ff")
frame_center.pack()

def render():
    Lebel.config(text=count)


def increase(e=None):
    global count
    count += 1
    render()


def reduce(e=None):
    global count
    if (count == 0): return
    count -= 1
    render()
    
def reset(e=None):
    global count
    count = 0
    render()
    

keyboard.on_press_key('insert', increase)
keyboard.on_press_key('delete', reduce)
keyboard.on_press_key('home', reset)

render()

tk.Button(frame_center, font=(
    "Helvetica", 12, "bold"), text="+", command=increase, width=3).pack(side='left')
tk.Button(frame_center, font=(
    "Helvetica", 12, "bold"),  text="-", command=reduce, width=3).pack(side='left')
tk.Button(frame_center, font=(
    "Helvetica", 11),  text="Reset", command=reset, width=5).pack(side='left')
tk.Button(frame_center, font=(
    "Helvetica", 11),  text="Exit", command=main_win.destroy, width=5).pack(side='left')

main_win.mainloop()
