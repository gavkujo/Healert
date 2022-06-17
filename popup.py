import os
from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./pupassets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("301x190")
window.configure(bg = "#FFFFFF")


canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 190,
    width = 301,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_rectangle(
    0.0,
    0.0,
    301.0,
    190.0,
    fill="#FBA0F2",
    outline="")

canvas.create_text(
    99.0,
    29.0,
    anchor="nw",
    text="Are you Sure?",
    fill="#000000",
    font=("Quicksand Regular", 16 * -1)
)

canvas.create_text(
    9.0,
    64.0,
    anchor="nw",
    text="You would have to log back in to see your details again.",
    fill="#000000",
    font=("Quicksand Regular", 11 * -1)
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: window.destroy(),
    relief="flat"
)
button_1.place(
    x=171.0,
    y=121.0,
    width=115.0,
    height=38.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: exit(),
    relief="flat"
)
button_2.place(
    x=17.0,
    y=121.0,
    width=115.0,
    height=38.0
)
window.resizable(False, False)
window.mainloop()
