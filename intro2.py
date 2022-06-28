from pathlib import Path
import os
import sys
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./intro2assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)
def intro3open():
    window.withdraw()
    os.system('python3 ~/Desktop/build1/intro3.py')
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
    fill="#E8E8E8",
    outline="")

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: intro3open(),
    relief="flat"
)
button_1.place(
    x=775.0,
    y=550.0,
    width=142.0,
    height=51.0
)

image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    234.0,
    308.0,
    image=image_image_1
)

canvas.create_text(
    500.0,
    47.0,
    anchor="nw",
    text="Keep your Medications in check",
    fill="#FF7BF9",
    font=("Quicksand SemiBold", 30 * -1)
)

canvas.create_text(
    555.0,
    270.0,
    anchor="nw",
    text="Track your prescriptions",
    fill="#000000",
    font=("Quicksand Regular", 23 * -1)
)

canvas.create_text(
    555.0,
    322.0,
    anchor="nw",
    text="Get Reminders for Medications",
    fill="#000000",
    font=("Quicksand Regular", 23 * -1)
)
window.resizable(False, False)
window.mainloop()
