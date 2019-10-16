from tkinter import *
from tkinter import messagebox

root = Tk()


def Info():
    messagebox.showinfo("Processeur de Andres", "Processeur de texte version 2019")


def Licence():
    messagebox.showwarning("Licence", "produit sous licence ")


def Sortir():
    # value = messagebox.askquestion("Sortir", "¿Tu veux sortir?")
    value = messagebox.askokcancel("Sortir", "¿Tu veux sortir?")
    if value:
        root.destroy()


def FermeRoot():
    value = messagebox.askretrycancel("Reintentar", "No es posible cerrar. Documento bloqueado")


root.title("Mon Premier Menu")
BarMenu = Menu(root)
root.config(menu=BarMenu, width=300, height=300)

FicherMenu = Menu(BarMenu, tearoff=0)
FicherMenu.add_command(label="Nouveau")
FicherMenu.add_command(label="Enregistre")
FicherMenu.add_command(label="Enregistre comme")
FicherMenu.add_separator()
FicherMenu.add_command(label="Fermer", command=FermeRoot)
FicherMenu.add_command(label="Sortir", command=Sortir)

FicherEdition = Menu(BarMenu, tearoff=0)
FicherEdition.add_command(label="Couper")
FicherEdition.add_command(label="Couler")
FicherEdition.add_command(label="Copie")

FicherOutils = Menu(BarMenu, tearoff=0)

FicherAide = Menu(BarMenu, tearoff=0)
FicherAide.add_command(label="Licence", command=Licence)
FicherAide.add_command(label="Savoir plus...", command=Info)

BarMenu.add_cascade(label="Ficher", menu=FicherMenu)

BarMenu.add_cascade(label="Edition", menu=FicherEdition)

BarMenu.add_cascade(label="Outils", menu=FicherOutils)

BarMenu.add_cascade(label="Aide", menu=FicherAide)

root.mainloop()
