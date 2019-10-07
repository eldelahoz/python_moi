from tkinter import *

root = Tk()
MonPrenom = StringVar()
MonFrame = Frame(root, width=500, height=400)
MonFrame.pack()
PrenomLabel = Label(MonFrame, text="Prenom:")
PrenomLabel.grid(row=0, column=0)
Prenom = Entry(MonFrame, textvariable=MonPrenom)
Prenom.grid(row=0, column=1)


def prenom():
    MonPrenom.set("Andres")


Button_envoie = Button(root, text="Envoie", command=prenom).pack()

root.mainloop()
