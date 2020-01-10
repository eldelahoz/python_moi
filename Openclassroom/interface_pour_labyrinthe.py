from tkinter import *
import tkinter.messagebox as tm


def deuxime_wm():
    root.withdraw()
    vm_deuxime = Toplevel()
    vm_deuxime.title("Labyrinthe")
    vm_deuxime.iconbitmap('img/ico.ico')
    Nickname_Label1 = Label(vm_deuxime, text=f"Bienvenu: {Contenu.entry_nick.get()}")
    Nickname_Label1.configure(font="Arial 14 bold")
    Nickname_Label1.pack()
    vm_deuxime.resizable(height=False, width=False)
    vm_deuxime.bind('<Escape>', lambda esc: vm_deuxime.destroy())


def ferme_vm():
    root.destroy()


def verificateur_nick(nick):
    if nick != "":
        print("C'est bien")
        deuxime_wm()
    else:
        tm.showerror("NICK ERROR", "Il n'y a pas de Nick ecrit")


class GUI_Lab(Frame):

    def __init__(self, master):
        super(GUI_Lab, self).__init__(master)

        self.label_nick = Label(self, text="Nick:", font="Arial 14 bold")
        self.entry_nick = Entry(self)
        self.button_ok = Button(self, text="Ok", width=10, command=lambda: verificateur_nick(self.entry_nick.get()))
        self.button_cancel = Button(self, text="Cancel", width=10, command=exit)

        self.label_nick.grid(row=0, sticky=E, pady=10, padx=10)
        self.entry_nick.grid(row=0, column=1)
        self.button_ok.grid(row=1, sticky=W)
        self.button_cancel.grid(row=1, column=1)

        self.pack()


root = Tk()
root.title("Labyrinthe")
root.iconbitmap('img/ico.ico')

Contenu = GUI_Lab(root)
root.geometry("350x80")
root.resizable(height=False, width=False)
root.bind('<Escape>', lambda esc: root.destroy())
root.mainloop()
# class LoginFrame(Frame):
#
#     def __init__(self, master):
#         super().__init__(master)
#
#         self.label_username = Label(self, text="Username")
#         self.label_password = Label(self, text="Password")
#
#         self.entry_username = Entry(self)
#         self.entry_password = Entry(self, show="*")
#
#         self.label_username.grid(row=0, sticky=E)
#         self.label_password.grid(row=1, sticky=E)
#         self.entry_username.grid(row=0, column=1)
#         self.entry_password.grid(row=1, column=1)
#
#         self.checkbox = Checkbutton(self, text="Keep me logged in")
#         self.checkbox.grid(columnspan=2)
#
#         self.logbtn = Button(self, text="Login", command=self._login_btn_clicked)
#         self.logbtn.grid(columnspan=2)
#
#         self.pack()
#
#     def _login_btn_clicked(self):
#         # print("Clicked")
#         username = self.entry_username.get()
#         password = self.entry_password.get()
#
#         # print(username, password)
#
#         if username == "john" and password == "password":
#             tm.showinfo("Login info", "Welcome John")
#         else:
#             tm.showerror("Login error", "Incorrect username")
#
#
# root = Tk()
# lf = LoginFrame(root)
# root.mainloop()
