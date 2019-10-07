from tkinter import *

root = Tk()
root.title("Salut!")
MonFrame = Frame(root, width=500, height=400)
MonFrame.pack()
MonImage = PhotoImage(file="one.png")
MonImage.resiz
# MonLabel = Label(MonFrame, text="Bonjours a tous", fg="red", font=("Comic Sans MS", 18)).place(x=100, y=200)
Label(MonFrame, image=MonImage).place(x=100, y=200)

root.mainloop()
