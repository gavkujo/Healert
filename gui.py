from logging import root
from pathlib import Path
import os


from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
import tkinter

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def loginOpen():
    window.destroy()
    os.system('python3 ~/Desktop/build1/gui1.py')

def dshbrdOpen():
    window.destroy()
    os.system('python3 ~/Desktop/build1/Dashboard.py')

def submit():
    name = username.get()
    password = pswd.get()
    email = emailz.get()
    print(name," ", password, " ", email)
    username.set("")
    pswd.set("")
    emailz.set("")

window = Tk()

pswd = tkinter.StringVar()
username = tkinter.StringVar()
emailz = tkinter.StringVar()

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
    325.0,
    0.0,
    790.0,
    511.0,
    fill="#FBFBFB",
    outline="")

canvas.create_text(
    346.0,
    26.0,
    anchor="nw",
    text="Create Account",
    fill="#FFA6F6",
    font=("Quicksand Medium", 20 * -1)
)

canvas.create_text(
    25.0,
    16.0,
    anchor="nw",
    text="TEST",
    fill="#FFFFFF",
    font=("Quicksand Regular", 36 * -1)
)

canvas.create_text(
    481.0,
    477.0,
    anchor="nw",
    text="If you already have an account",
    fill="#000000",
    font=("Quicksand Medium", 14 * -1)
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    553.5,
    131.5,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#d9d9d9",
    highlightthickness=0,
    textvariable=emailz
)
entry_1.place(
    x=346.0,
    y=107.0,
    width=415.0,
    height=47.0
)

canvas.create_text(
    348.0,
    87.0,
    anchor="nw",
    text="E-mail",
    fill="#000000",
    font=("Quicksand Medium", 16 * -1)
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    553.5,
    203.5,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#d9d9d9",
    highlightthickness=0,
    textvariable=username
)
entry_2.place(
    x=346.0,
    y=179.0,
    width=415.0,
    height=47.0
)

canvas.create_text(
    348.0,
    159.0,
    anchor="nw",
    text="Username",
    fill="#000000",
    font=("Quicksand Medium", 16 * -1)
)

entry_image_3 = PhotoImage(
    file=relative_to_assets("entry_3.png"))
entry_bg_3 = canvas.create_image(
    553.5,
    274.5,
    image=entry_image_3
)
entry_3 = Entry(
    bd=0,
    bg="#d9d9d9",
    highlightthickness=0,
    textvariable=pswd,
    show = "*"
)
entry_3.place(
    x=346.0,
    y=250.0,
    width=415.0,
    height=47.0
)

canvas.create_text(
    348.0,
    230.0,
    anchor="nw",
    text="Password",
    fill="#000000",
    font=("Quicksand Medium", 16 * -1)
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: [submit(), dshbrdOpen()],
    relief="flat"
)
button_1.place(
    x=344.0,
    y=314.0,
    width=208.0,
    height=54.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: loginOpen(),
    relief="flat"
)
button_2.place(
    x=696.0,
    y=471.0,
    width=65.0,
    height=30.0
)

canvas.create_text(
    25.0,
    194.0,
    anchor="nw",
    text="Get your stuff",
    fill="#000000",
    font=("Quicksand Medium", 14 * -1)
)

canvas.create_text(
    25.0,
    215.0,
    anchor="nw",
    text="In Track",
    fill="#FFFFFF",
    font=("Quicksand Medium", 20 * -1)
)
window.resizable(False, False)
window.mainloop()