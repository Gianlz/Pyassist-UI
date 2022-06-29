# Assitente Virtual 2.0 com UI.

# Feito por Gianluca Zugno

# Data da ultima versão: 28/06/2022

from ast import FormattedValue, While
from tkinter import *
from tkinter.font import BOLD
from tkinter.tix import COLUMN
from PIL import Image, ImageTk
from game import *
import color as cl

root = Tk()

root.geometry("648x800+750+80")
root.title("Assistente")
root.configure(bg="#1a1818")


# Logo (change path)
Logo = Image.open(
    r"C:\Users\skyla\Desktop\Assist\Assistente-UI\Versions\1.1\Image\unknown.png"
)
test = ImageTk.PhotoImage(Logo)
label1 = Label(image=test)
label1.image = test
label1.grid(column=0, row=0)

# Title
labeltextr = Label(root, bg="#1a1818", fg="green", text="Selecione operação:")
labeltextr.grid(
    column=0,
    row=1,
    pady=20,
)


def newWindow():
    global gc
    gc = Tk()
    gc.geometry("648x400+750+80")
    gc.configure(bg="#1a1818")
    gc.title("Assistente")
    root.destroy()

    jlabel = Label(gc, bg="#1a1818", fg="white", text="Escolha seu jogo :")
    jlabel.grid(column=0, row=0, pady=35, padx=40, sticky="w")

    r6lbl = Button(gc, text="[1] - Rainbow Six Siege")  # command=RainbowSix())
    r6lbl.grid(column=0, row=1, pady=15, padx=40, sticky="w")

    cslbl = Button(gc, text="[2] - Counter Strike Global Offensive")
    cslbl.grid(column=0, row=2, pady=15, padx=40, sticky="w")

    vallbl = Button(gc, text="[3] - Valorant (Soon)")
    vallbl.grid(column=0, row=3, pady=15, padx=40, sticky="w")

    dblbl = Button(gc, text="[4] - Driver Booster")
    dblbl.grid(column=0, row=4, pady=15, padx=40, sticky="w")

    suplbl = Button(gc, text="[5] - Surpresa")
    suplbl.grid(column=0, row=5, pady=15, padx=40, sticky="w")

    gc.mainloop()


def arduino():
    global ard
    ard = Tk()
    ard.geometry("648x400+750+80")
    ard.configure(bg="#1a1818")
    ard.title("Assistente")
    root.destroy()

    ardlbl = Label(ard, bg="#1a1818", fg="white", text="Escolha sua opção: ")
    ardlbl.grid(column=0, row=0, pady=35, padx=40, sticky="w")

    aiproc = Button(ard, text="[1] - AI Process (Soon)")
    aiproc.grid(column=0, row=1, pady=15, padx=40, sticky="w")

    colaim = Button(ard, text="[2] - Valorant Coilaim", command=Valcol)
    colaim.grid(column=0, row=2, pady=15, padx=40, sticky="w")

    VY5 = Button(ard, text="[3] - Valorant AI Yolov5 (Soon)")
    VY5.grid(column=0, row=3, pady=15, padx=40, sticky="w")

    ard.mainloop()


def save():
    for item in actlist.curselection():
        global var
        value = item + 1
        if value == 1:
            var = 162
        elif value == 2:
            var = 1
        elif value == 3:
            var = 2
        elif value == 4:
            var = 9
        elif value == 5:
            var = 160
        elif value == 6:
            var = 164
        else:
            o = 1

    fov = fovent.get()
    xspeed = speedx.get()
    yspeed = speedy.get()
    yspeed = float(yspeed)
    xspeed = float(xspeed)
    fov = int(fov)


    cl.Colaim(fov, var)


def Valcol():
    global ardcol
    ardcol = Tk()
    ardcol.geometry("648x400+750+80")
    ardcol.configure(bg="#1a1818")
    ardcol.title("Color Aim")
    ard.destroy()

    chlbl = Label(
        ardcol, bg="#1a1818", fg="white", text="Configurations:  ", font="arial 15 bold"
    )
    chlbl.grid(column=0, row=0)

    fovlbl = Label(ardcol, bg="#1a1818", fg="white", text="Fov (40): ", font=25)
    fovlbl.grid(column=0, row=1, sticky="w", pady=20)

    global fovent
    fovent = Entry(ardcol, bg="#1a1818", fg="white", font=15)
    fovent.grid(column=1, row=1, sticky="w", padx=10)

    actkey = Label(ardcol, bg="#1a1818", fg="white", text="Key:  ", font=15)
    actkey.grid(column=0, row=2, sticky="w")

    global actlist
    actlist = Listbox(ardcol, height=7)
    actlist.grid(column=0, row=3)
    actlist.insert(
        "end",
        "R_CTRL",
        "VK_LBUTTON",
        "VK_RBUTTON",
        "VK_TAB",
        "VK_LSHIFT",
        "VK_LMENU(alt)",
    )

    global xspeed
    global yspeed
    speedxlbl = Label(ardcol, bg="#1a1818", fg="white", text="X speed:  ", font=15)
    speedxlbl.grid(column=0, row=4, sticky="w", pady=10)

    speedylbl = Label(ardcol, bg="#1a1818", fg="white", text="Y speed:  ", font=15)
    speedylbl.grid(column=0, row=5, sticky="w", pady=10)

    global speedx
    speedx = Entry(ardcol, bg="#1a1818", fg="white", font=15)
    speedx.grid(column=1, row=4, sticky="w", padx=10)
    global speedy
    speedy = Entry(ardcol, bg="#1a1818", fg="white", font=15)
    speedy.grid(column=1, row=5, sticky="w", padx=10)

    btna = Button(ardcol, text="Get", command=save, width=20)
    btna.grid(column=0, row=6)

    ardcol.mainloop()


# Button
but1 = Button(root, width=34, text="-- Abrir Jogo[1] --", command=newWindow)
but1.grid(column=0, row=2)


def callgoogle():
    wb.open("https://www.google.com.br")
    print("a")


but2 = Button(root, width=34, text="-- Abrir Google[2] --")
but2.grid(
    column=0,
    row=3,
    pady=20,
)  # command= callgoogle() )

but3 = Button(root, width=34, text="-- Arduino[3] --", command=arduino)
but3.grid(column=0, row=4)

root.mainloop()
