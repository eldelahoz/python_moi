from tkinter import *

root = Tk()
root.title("CheckButton")

Plage = IntVar()
Montagne = IntVar()
Tourisme_rural = IntVar()


def Options():
    OptionsChoisi = ""
    if Plage.get() == 1:
        OptionsChoisi += " Plage"
    if Montagne.get() == 1:
        OptionsChoisi += " Montagne"
    if Tourisme_rural.get() == 1:
        OptionsChoisi += " Tourisme Rural"

    TextFin.config(text=OptionsChoisi)


Photo = PhotoImage(file="avion.png")
Label(root, image=Photo).pack()

MonFrame = Frame(root)
MonFrame.pack()

Label(MonFrame, text="Choisissez votre destination:", width=50).pack()
Checkbutton(MonFrame, text="Plage", variable=Plage, onvalue=1, offvalue=0, command=lambda: Options()).pack()
Checkbutton(MonFrame, text="Montagne", variable=Montagne, onvalue=1, offvalue=0, command=lambda: Options()).pack()
Checkbutton(MonFrame, text="Tourisme rural", variable=Tourisme_rural, onvalue=1, offvalue=0, command=lambda: Options()).pack()
TextFin = Label(MonFrame)
TextFin.pack()
root.mainloop()
