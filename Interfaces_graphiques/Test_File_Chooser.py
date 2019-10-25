from tkinter import *
from tkinter import filedialog

root = Tk()


def OuvrirFiche():
    Ficher = filedialog.askopenfile(title="Ouvrir", initialdir="C:/",
                                    filetypes=(("Format JPG", "*.jpg"), ("Format Excel", "*.xmls"), ("All Format", "*.*")))

    print(Ficher)


Button(root, text="Ouvrir Ficher", command=OuvrirFiche).pack()

root.mainloop()
