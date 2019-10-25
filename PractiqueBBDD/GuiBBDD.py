from tkinter import *

root = Tk()
# Interface
root.title("BDDD Users")
root.iconbitmap('user.ico')
root.geometry("280x300")
root.resizable(False, False)

# Frame
MonFrame = Frame(root, width=500, height=500, bg='red', cursor='circle')
MonFrame.pack()

# Label
MonLabel0 = Label(MonFrame, text="ID", bg='red')
MonLabel0.grid(column=1, row=1)
MonLabel1 = Label(MonFrame, text="Nom", bg='red')
MonLabel1.grid(column=1, row=2)

# Entry

MonEntry0 = Entry(MonFrame, width=10)
MonEntry0.grid(column=2, row=1, padx=2, pady=2)

root.mainloop()
