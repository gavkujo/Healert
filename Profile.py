from pathlib import Path
import os

from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./prfassets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def dshbrdOpen1():
    window.destroy()
    #os.system('python3 ~/Desktop/build1/Dashboard.py')

def paeOpen1():
    window.destroy()
    os.system('python3 ~/Desktop/build1/pae.py')

def pupOpen1():
    os.system('python3 ~/Desktop/build1/popup.py')


window = Tk()

window.geometry("790x511")
window.configure(bg = "#FFFFFF")


canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 511,
    width = 790,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_rectangle(
    0.0,
    1.0,
    790.0,
    511.0,
    fill="#FFA6F6",
    outline="")

canvas.create_rectangle(
    167.0,
    1.0,
    790.0,
    512.0,
    fill="#FFFFFF",
    outline="")

canvas.create_text(
    229.0,
    60.0,
    anchor="nw",
    text="xyz@gmail.com",
    fill="#000000",
    font=("Quicksand Regular", 11 * -1)
)

canvas.create_text(
    39.0,
    15.0,
    anchor="nw",
    text="TEST",
    fill="#FFFFFF",
    font=("Quicksand Regular", 36 * -1)
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: dshbrdOpen1(),
    relief="flat"
)
button_1.place(
    x=0.0,
    y=171.0,
    width=167.0,
    height=49.0
)

canvas.create_rectangle(
    0.0,
    303.0,
    167.0,
    352.0,
    fill="#FFB2F7",
    outline="")

canvas.create_text(
    58.0,
    318.0,
    anchor="nw",
    text="Profile",
    fill="#000000",
    font=("Quicksand Regular", 16 * -1)
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: paeOpen1(),
    relief="flat"
)
button_2.place(
    x=0.0,
    y=237.0,
    width=167.0,
    height=49.0
)

canvas.create_text(
    43.0,
    485.0,
    anchor="nw",
    text="Username",
    fill="#FFFFFF",
    font=("Quicksand Regular", 16 * -1)
)

canvas.create_text(
    193.0,
    22.0,
    anchor="nw",
    text="Username",
    fill="#000000",
    font=("Quicksand Bold", 24 * -1)
)

canvas.create_text(
    193.0,
    60.0,
    anchor="nw",
    text="Email:",
    fill="#000000",
    font=("Quicksand Regular", 11 * -1)
)

canvas.create_rectangle(
    193.0,
    101.0,
    510.0,
    485.0,
    fill="#FEDFFF",
    outline="")

image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    720.0,
    158.0,
    image=image_image_1
)

canvas.create_text(
    666.0,
    112.0,
    anchor="nw",
    text="Number of PAE",
    fill="#000000",
    font=("Quicksand SemiBold", 15 * -1)
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    234.0,
    452.0,
    image=image_image_2
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    469.0,
    134.0,
    image=image_image_3
)

image_image_4 = PhotoImage(
    file=relative_to_assets("image_4.png"))
image_4 = canvas.create_image(
    721.0,
    285.0,
    image=image_image_4
)

image_image_5 = PhotoImage(
    file=relative_to_assets("image_5.png"))
image_5 = canvas.create_image(
    577.0,
    154.0,
    image=image_image_5
)

canvas.create_text(
    702.0,
    127.0,
    anchor="nw",
    text="9",
    fill="#000000",
    font=("Quicksand SemiBold", 64 * -1)
)

canvas.create_text(
    214.0,
    217.0,
    anchor="nw",
    text="Text",
    fill="#000000",
    font=("Quicksand SemiBold", 16 * -1)
)

canvas.create_text(
    214.0,
    357.0,
    anchor="nw",
    text="Text",
    fill="#000000",
    font=("Quicksand SemiBold", 16 * -1)
)

canvas.create_text(
    214.0,
    329.0,
    anchor="nw",
    text="Text",
    fill="#000000",
    font=("Quicksand SemiBold", 16 * -1)
)

canvas.create_text(
    214.0,
    301.0,
    anchor="nw",
    text="Text",
    fill="#000000",
    font=("Quicksand SemiBold", 16 * -1)
)

canvas.create_text(
    214.0,
    273.0,
    anchor="nw",
    text="Text",
    fill="#000000",
    font=("Quicksand SemiBold", 16 * -1)
)

canvas.create_text(
    214.0,
    245.0,
    anchor="nw",
    text="Text",
    fill="#000000",
    font=("Quicksand SemiBold", 16 * -1)
)

canvas.create_text(
    210.0,
    127.0,
    anchor="nw",
    text="Medications:",
    fill="#000000",
    font=("Quicksand SemiBold", 20 * -1)
)

canvas.create_text(
    688.0,
    22.0,
    anchor="nw",
    text="Profile",
    fill="#FFB2F7",
    font=("Quicksand Bold", 24 * -1)
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: pupOpen1(),
    relief="flat"
)
button_3.place(
    x=634.0,
    y=452.0,
    width=109.0,
    height=33.0
)

image_image_6 = PhotoImage(
    file=relative_to_assets("image_6.png"))
image_6 = canvas.create_image(
    586.0,
    291.0,
    image=image_image_6
)
window.resizable(False, False)
window.mainloop()
