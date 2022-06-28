# Assitente Virtual 2.0 com UI.

# Feito por Gianluca Zugno 

# Data da ultima versão: 28/06/2022

from tkinter import *
from tkinter.tix import COLUMN
from PIL import Image, ImageTk
from game import *

root = Tk()

root.geometry("648x800+750+80")
root.title("Assistente")
root.configure(bg= '#1a1818')


# Logo
Logo = Image.open(r"C:\Users\skyla\Desktop\Nova pasta\Random\Image\unknown.png")
test = ImageTk.PhotoImage(Logo)
label1 = Label(image=test)
label1.image = test
label1.grid(column=0, row=0)

# Title
labeltextr = Label(root, bg= '#1a1818',fg= 'green', text="Selecione operação:")
labeltextr.grid(column=0, row=1, pady=20, )

# Button
def newWindow():
    gc = Tk()
    gc.geometry("648x400+750+80")
    gc.configure(bg= '#1a1818')
    gc.title("Assistente")
    root.destroy()

    jlabel = Label(gc,bg= '#1a1818', fg= "white", text= "Escolha seu jogo :")
    jlabel.grid(column=0, row=0, pady= 35, padx= 40,sticky = 'w')

    r6lbl = Button(gc, text = "[1] - Rainbow Six Siege")#command=RainbowSix())
    r6lbl.grid(column=0, row=1, pady= 15, padx= 40,sticky = 'w')

    cslbl = Button(gc, text= '[2] - Counter Strike Global Offensive')
    cslbl.grid(column=0, row=2, pady= 15, padx= 40,sticky = 'w')

    vallbl = Button(gc, text= '[3] - Valorant (Soon)')
    vallbl.grid(column=0, row=3, pady= 15, padx= 40,sticky = 'w')

    dblbl = Button(gc, text = '[4] - Driver Booster')
    dblbl.grid(column=0, row=4, pady= 15, padx= 40,sticky = 'w')

    suplbl = Button(gc, text = '[5] - Surpresa')
    suplbl.grid(column=0, row=5, pady= 15, padx= 40,sticky = 'w')

    

    gc.mainloop()
    

but1 = Button(root,width=34, text="-- Abrir Jogo[1] --", command=newWindow)
but1.grid(column=0, row= 2)

def callgoogle():
    wb.open('https://www.google.com.br')
    print("a")

but2 = Button(root, width=34, text="-- Abrir Google[2] --")
but2.grid(column=0, row= 3, pady=20,) #command= callgoogle() )


root.mainloop()
