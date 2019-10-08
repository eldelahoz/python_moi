from tkinter import *

root = Tk()

VarOpction = IntVar()


def Imprimer():
    # print(VarOpction.get())
    if VarOpction.get() == 1:
        Etiquette.config(text="Tu as choisi Masculin")
    elif VarOpction.get() == 2:
        Etiquette.config(text="Tu as choisi Feminin")
    else:
        Etiquette.config(text="Tu as choisi Outres")


Label(root, text="Genre:").pack()
Radiobutton(root, text="Masculin", variable=VarOpction, value=1, command=lambda: Imprimer()).pack()
Radiobutton(root, text="Feminin", variable=VarOpction, value=2, command=lambda: Imprimer()).pack()
Radiobutton(root, text="Outres", variable=VarOpction, value=3, command=lambda: Imprimer()).pack()

Etiquette = Label(root)
Etiquette.pack()
root.mainloop()
