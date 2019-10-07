from tkinter import *

raiz = Tk()

raiz.title("Mon premiere interface")
raiz.geometry("850x450")
raiz.config(bg="black", relief="sunken", bd="20", cursor="gumby")
# raiz.resizable(0, False)
monFrame = Frame()
monFrame.pack(fill="both", expand="True")
monFrame.config(bg="#ff7e62", width="650", height="350", relief="groove", cursor="pirate")
raiz.mainloop()
