from pathlib import Path
import os
import sys
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./intro3assets")

def loginOpen():
    window.withdraw()
    os.system('python3 ~/Desktop/build1/gui1.py')
    sys.exit()

def signupOpen():
    window.withdraw()
    os.system('python3 ~/Desktop/build1/gui.py')
    sys.exit()

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


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
    fill="#FFA6F0",
    outline="")

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: loginOpen(),
    relief="flat"
)
button_1.place(
    x=727.0,
    y=535.0,
    width=168.0,
    height=51.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: signupOpen(),
    relief="flat"
)
button_2.place(
    x=512.0,
    y=535.0,
    width=168.0,
    height=51.0
)

image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    232.0,
    462.0,
    image=image_image_1
)

canvas.create_text(
    24.0,
    15.0,
    anchor="nw",
    text="Healert",
    fill="#FFFFFF",
    font=("Quicksand SemiBold", 36 * -1)
)

canvas.create_text(
    43.0,
    132.0,
    anchor="nw",
    text="Come start your journey with us",
    fill="#635563",
    font=("Quicksand Medium", 24 * -1)
)

canvas.create_text(
    63.0,
    169.0,
    anchor="nw",
    text="and aim for a better lifestyle",
    fill="#635563",
    font=("Quicksand Medium", 24 * -1)
)

canvas.create_text(
    581.0,
    414.0,
    anchor="nw",
    text="Lets get started!",
    fill="#635563",
    font=("Quicksand Medium", 32 * -1)
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    697.0,
    154.0,
    image=image_image_2
)
window.resizable(False, False)
window.mainloop()
