from tkinter import *

root = Tk()
root.title("Mon Calculatrice")
MonFrame = Frame(root, width=500, height=500)
MonFrame.pack()

NombreEcran = StringVar()

# <editor-fold desc="Ecran">
Ecran = Entry(MonFrame, textvariable=NombreEcran)
Ecran.grid(row=0, column=1, padx=10, pady=10, columnspan=4)
Ecran.config(bg="black", fg="#03f943", justify="right")


# </editor-fold>
def NombrePul(nombre):
    NombreEcran.set(NombreEcran.get() + nombre)


# <editor-fold desc="File1">
Button7 = Button(MonFrame, text="7", width=3, command=lambda: NombrePul("7"))
Button7.grid(row=2, column=1)
Button8 = Button(MonFrame, text="8", width=3, command=lambda: NombrePul("8"))
Button8.grid(row=2, column=2)
Button9 = Button(MonFrame, text="9", width=3, command=lambda: NombrePul("9"))
Button9.grid(row=2, column=3)
ButtonDiv = Button(MonFrame, text="/", width=3)
ButtonDiv.grid(row=2, column=4)
# </editor-fold>

# <editor-fold desc="File2">
Button4 = Button(MonFrame, text="4", width=3, command=lambda: NombrePul("4"))
Button4.grid(row=3, column=1)
Button5 = Button(MonFrame, text="5", width=3, command=lambda: NombrePul("5"))
Button5.grid(row=3, column=2)
Button6 = Button(MonFrame, text="6", width=3, command=lambda: NombrePul("6"))
Button6.grid(row=3, column=3)
ButtonMul = Button(MonFrame, text="X", width=3)
ButtonMul.grid(row=3, column=4)
# </editor-fold>

# <editor-fold desc="File3">
Button1 = Button(MonFrame, text="1", width=3, command=lambda: NombrePul("1"))
Button1.grid(row=4, column=1)
Button2 = Button(MonFrame, text="2", width=3, command=lambda: NombrePul("2"))
Button2.grid(row=4, column=2)
Button3 = Button(MonFrame, text="3", width=3, command=lambda: NombrePul("3"))
Button3.grid(row=4, column=3)
ButtonRest = Button(MonFrame, text="-", width=3)
ButtonRest.grid(row=4, column=4)
# </editor-fold>

# <editor-fold desc="File4">
Button0 = Button(MonFrame, text="0", width=3, command=lambda: NombrePul("0"))
Button0.grid(row=5, column=1)
ButtonComa = Button(MonFrame, text=",", width=3, command=lambda: NombrePul(","))
ButtonComa.grid(row=5, column=2)
ButtonIgual = Button(MonFrame, text="=", width=3)
ButtonIgual.grid(row=5, column=3)
ButtonSuma = Button(MonFrame, text="+", width=3)
ButtonSuma.grid(row=5, column=4)
# </editor-fold>

root.mainloop()
