from tkinter import *
from tkinter import filedialog

root = Tk()


def OuvrirFiche():
    Ficher = filedialog.askopenfile(title="Ouvrir")

    print(Ficher)


Button(root, text="Ouvrir Ficher", command=OuvrirFiche).pack()

root.mainloop()
