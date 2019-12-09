from tkinter import *
import sqlite3
from tkinter import messagebox
import os

root = Tk()
# Interface
root.title("BDDD Users")
root.iconbitmap('user.ico')
root.geometry("280x350")
root.resizable(False, False)

# Variable
VarID = IntVar()
VarNom = StringVar()
VarPrenom = StringVar()
VarMotdepasse = StringVar()
VarCommentaire = StringVar()


# Fonctions
def Suprimerchamps():
    MonEntry0.delete(0, END)
    MonEntry1.delete(0, END)
    MonEntry2.delete(0, END)
    MonEntry3.delete(0, END)
    MonEntry4.delete("1.0", END)
    pass


def ConectionBDDD():
    if os.path.exists('Registre'):
        messagebox.showinfo("CONECTION", "Existe la BBDD, se va a hacer la conexion...")
    else:
        messagebox.showinfo("CONECTION", "No existe la BBDD, se va a crear...")
        MonConection = sqlite3.connect("Registre")
        MonCoursor = MonConection.cursor()
        MonCoursor.execute('''
                    CREATE TABLE REGISTROS (
                    ID INTEGER PRIMARY KEY AUTOINCREMENT,
                    Nom VARCHAR(25),
                    Prenom VARCHAR(25),
                    Motdepasse VARCHAR(20),
                    Commentaire VARCHAR(20))
                '''
                           )
        messagebox.showinfo("CONECTION", "BBDD, creada correctamente.")
    global MonConectionBD
    MonConectionBD = sqlite3.connect("Registre")
    global MonCursor
    MonCursor = MonConectionBD.cursor()
    messagebox.showinfo("CONECTION", "Se conecto a la BBDD")


def CreateBBDD():
    ListRegistre = [
        (MonEntry1.get(), MonEntry2.get(), MonEntry3.get(), MonEntry4.get(1.0, END))
    ]
    MonCursor.executemany("INSERT INTO REGISTROS VALUES(NULL, ?, ?, ?, ?)", ListRegistre)
    MonConectionBD.commit()


Activate = 0


def ReaderBBDD():
    MonEntry0['state'] = 'normal'
    global Activate
    MonEntry1.delete(0, END)
    MonEntry2.delete(0, END)
    MonEntry3.delete(0, END)
    MonEntry4.delete("1.0", END)
    if MonEntry0['state'] == 'normal':
        ChercherID = MonEntry0.get()
        MonCursor.execute("SELECT * FROM REGISTROS WHERE ID=" + ChercherID)
        ReaderBD = MonCursor.fetchall()
        print(Activate)
    if Activate == 1:
        if ReaderBD:
            for VarReader in ReaderBD:
                VarID.set(VarReader[0])
                VarNom.set(VarReader[1])
                VarPrenom.set(VarReader[2])
                VarMotdepasse.set(VarReader[3])
                MonEntry4.insert(INSERT, VarReader[4])
        else:
            messagebox.showerror("ERROR", "No se ha encontrado el registro.")
    if Activate == 0:
        messagebox.showinfo("BUSQUEDA", "Se a activado la busqueda, pon un ID y preciona READ")
        Activate += 1


def UpdateBBDD():
    MonCursor.execute(
        f"UPDATE REGISTROS SET Nom='{MonEntry1.get()}', Prenom='{MonEntry2.get()}', Motdepasse='{MonEntry3.get()}', Commentaire='{MonEntry4.get(1.0, END)}'  WHERE ID={MonEntry0.get()}")
    MonConectionBD.commit()
    messagebox.showinfo("ACTUALIZADO", "Se ha actualizado el registro con ID" + MonEntry0.get())


def DeleteBBDD():
    Seguro = messagebox.askquestion("ELIMINAR", "Estas seguro de quere eliminar este registro?")
    if Seguro == "yes":
        MonCursor.execute(f"DELETE FROM REGISTROS WHERE ID={MonEntry0.get()}")
        messagebox.showwarning("ELIMINAR", "Se ha eliminado el registro.")
        MonConectionBD.commit()
    else:
        messagebox.showinfo("ELIMINAR", "No se ha eliminado el registro.")
    Suprimerchamps()


def TestBBDD():
    MonCursor.execute(f"SELECT * FROM REGISTROS WHERE ID={MonEntry0.get()}")
    ReaderBD = MonCursor.fetchall()
    print(ReaderBD)
    if ReaderBD:
        print("El registro esta.")
    else:
        print("No se encuentra el registro")
    pass


# Menu
BarMenu = Menu(root)
BBDDMenu = Menu(BarMenu, tearoff=0)

BBDDMenu.add_command(label="Connecter", command=ConectionBDDD)
BBDDMenu.add_separator()
BBDDMenu.add_command(label="Sortir", command=root.quit)

BarMenu.add_cascade(label="BBDD", menu=BBDDMenu)

SuprimerMenu = Menu(BarMenu, tearoff=0)
SuprimerMenu.add_command(label="Suprimer champs", command=Suprimerchamps)

BarMenu.add_cascade(label="Suprimer", menu=SuprimerMenu)

CRUDMenu = Menu(BarMenu, tearoff=0)
CRUDMenu.add_command(label="Create", command=CreateBBDD)
CRUDMenu.add_command(label="Read", command=ReaderBBDD)
CRUDMenu.add_command(label="Update", command=UpdateBBDD)
CRUDMenu.add_command(label="Delete", command=DeleteBBDD)

BarMenu.add_cascade(label="CRUD", menu=CRUDMenu)

TestMenu = Menu(BarMenu, tearoff=0)
TestMenu.add_command(label="Test", command=TestBBDD)

BarMenu.add_cascade(label="Test", menu=TestMenu)

# Frame
MonFrame = Frame(root)
MonFrame.pack()
MonFrame2 = Frame(root)
MonFrame2.pack()

# Label
MonLabel0 = Label(MonFrame, text="ID")
MonLabel0.grid(column=1, row=1)
MonLabel1 = Label(MonFrame, text="Nom")
MonLabel1.grid(column=1, row=2)
MonLabel2 = Label(MonFrame, text="Pre Nom")
MonLabel2.grid(column=1, row=3)
MonLabel3 = Label(MonFrame, text="Mot de Passe")
MonLabel3.grid(column=1, row=4)
MonLabel4 = Label(MonFrame, text="Commentaire")
MonLabel4.grid(column=1, row=5)


# Entry
def is_valid_char(char):
    return char in "0123456789"


validatecommand = root.register(is_valid_char)
MonEntry0 = Entry(MonFrame, width=15, textvariable=VarID, validate="key", validatecommand=(validatecommand, "%S"),
                  state=DISABLED)
MonEntry0.grid(column=2, row=1, padx=3, pady=8)
MonEntry1 = Entry(MonFrame, width=15, textvariable=VarNom)
MonEntry1.grid(column=2, row=2, padx=3, pady=8)
MonEntry2 = Entry(MonFrame, width=15, textvariable=VarPrenom)
MonEntry2.grid(column=2, row=3, padx=3, pady=8)
MonEntry3 = Entry(MonFrame, width=15, textvariable=VarMotdepasse)
MonEntry3.grid(column=2, row=4, padx=3, pady=8)
MonEntry4 = Text(MonFrame, width=15, height=6)
MonEntry4.grid(column=2, row=5, padx=3, pady=8)
scrollVert = Scrollbar(MonFrame, command=MonEntry4.yview)
scrollVert.grid(column=3, row=5, sticky="nsew")
MonEntry4.config(yscrollcommand=scrollVert.set)

# Button

MonButton0 = Button(MonFrame2, text="Create", command=CreateBBDD)
MonButton0.grid(column=1, row=1, padx=4, pady=8)
MonButton1 = Button(MonFrame2, text="Reader", command=ReaderBBDD)
MonButton1.grid(column=2, row=1, padx=4, pady=8)
MonButton2 = Button(MonFrame2, text="Update", command=UpdateBBDD)
MonButton2.grid(column=3, row=1, padx=4, pady=8)
MonButton3 = Button(MonFrame2, text="Delete", command=DeleteBBDD)
MonButton3.grid(column=4, row=1, padx=4, pady=8)

root.config(menu=BarMenu)
root.mainloop()
