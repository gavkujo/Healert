from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
import os


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./paeassets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def dshbrdOpen2():
    window.destroy()
    #os.system('python3 ~/Desktop/build1/Dashboard.py')

def prfOpen2():
    window.destroy()
    os.system('python3 ~/Desktop/build1/Profile.py')

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
    0.0,
    790.0,
    511.0,
    fill="#FFFFFF",
    outline="")

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
    command=lambda: dshbrdOpen2(),
    relief="flat"
)
button_1.place(
    x=0.0,
    y=171.0,
    width=167.0,
    height=49.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: prfOpen2(),
    relief="flat"
)
button_2.place(
    x=0.0,
    y=303.0,
    width=167.0,
    height=49.0
)

canvas.create_rectangle(
    0.0,
    237.0,
    167.0,
    286.0,
    fill="#FFB2F7",
    outline="")

canvas.create_text(
    17.0,
    252.0,
    anchor="nw",
    text="Post Appointment",
    fill="#000000",
    font=("Quicksand Regular", 16 * -1)
)

canvas.create_text(
    43.0,
    485.0,
    anchor="nw",
    text="Username",
    fill="#FFFFFF",
    font=("Quicksand Regular", 16 * -1)
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    331.0,
    109.5,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#FFB2F7",
    highlightthickness=0
)
entry_1.place(
    x=179.0,
    y=85.0,
    width=304.0,
    height=47.0
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    481.0,
    250.0,
    image=entry_image_2
)
entry_2 = Text(
    bd=0,
    bg="#D9D9D9",
    highlightthickness=0
)
entry_2.place(
    x=179.0,
    y=174.0,
    width=604.0,
    height=150.0
)

entry_image_3 = PhotoImage(
    file=relative_to_assets("entry_3.png"))
entry_bg_3 = canvas.create_image(
    329.5,
    385.0,
    image=entry_image_3
)
entry_3 = Entry(
    bd=0,
    bg="#D9D9D9",
    highlightthickness=0
)
entry_3.place(
    x=179.0,
    y=366.0,
    width=301.0,
    height=36.0
)

entry_image_4 = PhotoImage(
    file=relative_to_assets("entry_4.png"))
entry_bg_4 = canvas.create_image(
    625.0,
    385.0,
    image=entry_image_4
)
entry_4 = Entry(
    bd=0,
    bg="#D9D9D9",
    highlightthickness=0
)
entry_4.place(
    x=544.0,
    y=366.0,
    width=162.0,
    height=36.0
)

canvas.create_text(
    179.0,
    343.0,
    anchor="nw",
    text="Medicine Prescribed",
    fill="#000000",
    font=("Quicksand Regular", 16 * -1)
)

canvas.create_text(
    179.0,
    60.0,
    anchor="nw",
    text="Examination conducted by:",
    fill="#000000",
    font=("Quicksand Regular", 16 * -1)
)

canvas.create_text(
    496.0,
    7.0,
    anchor="nw",
    text="Post Appointment Entry",
    fill="#FFB2F7",
    font=("Quicksand Bold", 24 * -1)
)

canvas.create_text(
    179.0,
    151.0,
    anchor="nw",
    text="Description",
    fill="#000000",
    font=("Quicksand Regular", 16 * -1)
)

canvas.create_text(
    543.0,
    343.0,
    anchor="nw",
    text="For how long",
    fill="#000000",
    font=("Quicksand Regular", 16 * -1)
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_3 clicked"),
    relief="flat"
)
button_3.place(
    x=629.0,
    y=461.0,
    width=154.0,
    height=40.0
)
window.resizable(False, False)
window.mainloop()
