from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
import os
import tkinter
import sys
import testing as ts


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./gui1assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("790x511")
window.configure(bg = "#FFFFFF")

def signupOpen():
    window.withdraw()
    os.system('python3 ~/Desktop/build1/gui.py')
    sys.exit()

def dshbrdOpen():
    window.withdraw()
    os.system('python3 ~/Desktop/build1/Dashboard.py')
    sys.exit()

def pupOpen2():
    os.system('python3 ~/Desktop/build1/invalid_popup.py')

def check(name, pswd):
    a = ts.checking(name,pswd)
    if (a):
        if ts.checkpswd(name, pswd):
            dshbrdOpen()
        else:
            pupOpen2()
    else:
        signupOpen()

def extract_vals():
    name = username.get()
    password = pswd.get()
    check(name, password)
    username.set("")
    pswd.set("")

pswd = tkinter.StringVar()
username = tkinter.StringVar()

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
    1.0,
    790.0,
    512.0,
    fill="#FBFBFB",
    outline="")

canvas.create_text(
    346.0,
    26.0,
    anchor="nw",
    text="Welcome Back!",
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
    500.0,
    477.0,
    anchor="nw",
    text="If you dont have an account",
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
    textvariable=username
)
entry_1.place(
    x=346.0,
    y=107.0,
    width=415.0,
    height=47.0
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
    textvariable=pswd
)
entry_2.place(
    x=346.0,
    y=179.0,
    width=415.0,
    height=47.0
)

canvas.create_text(
    346.0,
    84.0,
    anchor="nw",
    text="Username",
    fill="#000000",
    font=("Quicksand Medium", 16 * -1)
)

canvas.create_text(
    346.0,
    159.0,
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
    command=lambda: extract_vals(),
    relief="flat"
)
button_1.place(
    x=344.0,
    y=240.0,
    width=208.0,
    height=54.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png")
    )
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: signupOpen(),
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
    text="Get your Medications",
    fill="#000000",
    font=("Quicksand Medium", 16 * -1)
)

canvas.create_text(
    25.0,
    215.0,
    anchor="nw",
    text="In Check",
    fill="#FFFFFF",
    font=("Quicksand Medium", 24 * -1)
)
window.resizable(False, False)
window.mainloop()