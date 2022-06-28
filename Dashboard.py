from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
import os
import sys
import testing as ts
import json

with open("userfiles.json", "r") as jsonFile:
    data = json.load(jsonFile)

cuser = data["username"]

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./dshbrdassets")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def prfOpen3():
    window.withdraw()
    os.system('python3 ~/Desktop/build1/Profile.py')
    sys.exit()

def paeOpen3():
    window.withdraw()
    os.system('python3 ~/Desktop/build1/pae.py')
    sys.exit()

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
    170.0,
    0.0,
    793.0,
    511.0,
    fill="#FFFFFF",
    outline="")

canvas.create_text(
    29.0,
    15.0,
    anchor="nw",
    text="Healert",
    fill="#FFFFFF",
    font=("Quicksand Bold", 36 * -1)
)

canvas.create_rectangle(
    0.0,
    171.0,
    167.0,
    220.0,
    fill="#FFB2F7",
    outline="")

canvas.create_text(
    42.0,
    185.0,
    anchor="nw",
    text="Dashboard",
    fill="#000000",
    font=("Quicksand Regular", 16 * -1)
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: prfOpen3(),
    relief="flat"
)
button_1.place(
    x=0.0,
    y=303.0,
    width=167.0,
    height=49.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: paeOpen3(),
    relief="flat"
)
button_2.place(
    x=0.0,
    y=237.0,
    width=167.0,
    height=49.0
)

canvas.create_rectangle(
    444.0,
    10.0,
    776.0,
    68.0,
    fill="#D9D9D9",
    outline="")

canvas.create_rectangle(
    444.0,
    84.0,
    776.0,
    142.0,
    fill="#D9D9D9",
    outline="")

canvas.create_text(
    648.0,
    115.0,
    anchor="nw",
    text="at ",
    fill="#000000",
    font=("Quicksand Regular", 16 * -1)
)

canvas.create_rectangle(
    178.0,
    10.0,
    430.0,
    245.0,
    fill="#FF8FAA",
    outline="")

canvas.create_rectangle(
    509.0,
    352.0,
    782.0,
    501.0,
    fill="#FFB2F7",
    outline="")

canvas.create_text(
    196.0,
    81.0,
    anchor="nw",
    text="Teext",
    fill="#ECECEC",
    font=("Prociono Regular", 24 * -1)
)

canvas.create_text(
    457.0,
    21.0,
    anchor="nw",
    text="Dont Forget to take your",
    fill="#000000",
    font=("Quicksand Regular", 16 * -1)
)

canvas.create_text(
    648.0,
    21.0,
    anchor="nw",
    text= ts.randomMedGen(cuser),
    fill="#000000",
    font=("Quicksand Regular", 16 * -1)
)

canvas.create_text(
    648.0,
    95.0,
    anchor="nw",
    text= ts.randomMedGen(cuser),
    fill="#000000",
    font=("Quicksand Regular", 16 * -1)
)

canvas.create_text(
    454.0,
    49.0,
    anchor="nw",
    text="Reminders",
    fill="#000000",
    font=("Quicksand Regular", 11 * -1)
)

canvas.create_text(
    454.0,
    120.0,
    anchor="nw",
    text="Reminders",
    fill="#000000",
    font=("Quicksand Regular", 11 * -1)
)

canvas.create_text(
    188.0,
    223.0,
    anchor="nw",
    text="Quote of The Day",
    fill="#000000",
    font=("Quicksand Regular", 11 * -1)
)

canvas.create_text(
    712.0,
    41.0,
    anchor="nw",
    text="Today",
    fill="#000000",
    font=("Quicksand Regular", 16 * -1)
)

canvas.create_text(
    668.0,
    115.0,
    anchor="nw",
    text="8 AM",
    fill="#000000",
    font=("Quicksand Regular", 16 * -1)
)

canvas.create_text(
    457.0,
    95.0,
    anchor="nw",
    text="Be sure to take your ",
    fill="#000000",
    font=("Quicksand Regular", 16 * -1)
)

canvas.create_text(
    712.0,
    115.0,
    anchor="nw",
    text="Today",
    fill="#000000",
    font=("Quicksand Regular", 16 * -1)
)

canvas.create_text(
    522.0,
    407.0,
    anchor="nw",
    text="Text",
    fill="#FFFFFF",
    font=("Quicksand Bold", 16 * -1)
)

canvas.create_text(
    522.0,
    363.0,
    anchor="nw",
    text="Did You Know?",
    fill="#FF8FAA",
    font=("Quicksand Bold", 20 * -1)
)

canvas.create_text(
    43.0,
    485.0,
    anchor="nw",
    text=cuser,
    fill="#FFFFFF",
    font=("Quicksand Regular", 16 * -1)
)

image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    329.0,
    371.0,
    image=image_image_1
)
window.resizable(False, False)
window.mainloop()