
from pathlib import Path
import os
import sys
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./intro1assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def intro2open():
    window.withdraw()
    os.system('python3 ~/Desktop/build1/intro2.py')
    sys.exit()

window = Tk()

window.geometry("930x616")
window.configure(bg = "#FFFFFF")


canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 616,
    width = 930,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_rectangle(
    0.0,
    0.0,
    930.0,
    616.0,
    fill="#FFB6FC",
    outline="")

canvas.create_text(
    398.0,
    238.0,
    anchor="nw",
    text="Welcome to",
    fill="#000000",
    font=("Quicksand Regular", 24 * -1)
)

canvas.create_text(
    356.0,
    268.0,
    anchor="nw",
    text="Healert",
    fill="#FFFFFF",
    font=("Quicksand Regular", 64 * -1)
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: intro2open(),
    relief="flat"
)
button_1.place(
    x=775.0,
    y=550.0,
    width=142.0,
    height=51.0
)
window.resizable(False, False)
window.mainloop()
