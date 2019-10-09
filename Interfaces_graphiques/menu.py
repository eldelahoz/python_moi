from tkinter import *

root = Tk()
root.title("Mon Premier Menu")
BarMenu = Menu(root)
root.config(menu=BarMenu, width=300, height=300)

FicherMenu = Menu(BarMenu, tearoff=0)
FicherMenu.add_command(label="Nouveau")
FicherMenu.add_command(label="Enregistre")
FicherMenu.add_command(label="Enregistre comme")
FicherMenu.add_separator()
FicherMenu.add_command(label="Fermer")
FicherMenu.add_command(label="Sortir")

FicherEdition = Menu(BarMenu, tearoff=0)
FicherEdition.add_command(label="Couper")
FicherEdition.add_command(label="Couler")
FicherEdition.add_command(label="Copie")

FicherOutils = Menu(BarMenu, tearoff=0)

FicherAide = Menu(BarMenu, tearoff=0)
FicherAide.add_command(label="Savoir plus...")

BarMenu.add_cascade(label="Ficher", menu=FicherMenu)

BarMenu.add_cascade(label="Edition", menu=FicherEdition)

BarMenu.add_cascade(label="Outils", menu=FicherOutils)

BarMenu.add_cascade(label="Aide", menu=FicherAide)

root.mainloop()
