# -*-coding:Utf-8 -*

"""Ce fichier contient le code principal du jeu.

Exécutez-le avec Python pour lancer le jeu.

"""
import os
import tkinter.messagebox as tm
from tkinter import *

from labyrinthe import *
from carte import *

# On charge les cartes existantes
cartes = []
for nom_fichier in os.listdir("cartes"):
    if nom_fichier.endswith(".txt"):
        chemin = os.path.join("cartes", nom_fichier)
        nom_carte = nom_fichier[:-3].lower()
        cartes.append(nom_carte)
        with open(chemin, "r") as fichier:
            contenu = fichier.read()
            # Création d'une carte, à compléter

# On affiche les cartes existantes
list_cartes = ""
for i, carte in enumerate(cartes):
    list_cartes += f"{i + 1} - {carte}\n"


# Function mouvement
def mouvement(a_jouer, labyrinthe_c, nick, visualiser, mouvement_entre):
    if len(a_jouer) > 1:
        if a_jouer[0] == "e":
            labyrinthe_c.e(int(a_jouer[1:]))
            labyrinthe_c.Enregistre(nick)
        if a_jouer[0] == "o":
            labyrinthe_c.o(int(a_jouer[1:]))
            labyrinthe_c.Enregistre(nick)
        if a_jouer[0] == "s":
            labyrinthe_c.s(int(a_jouer[1:]))
            labyrinthe_c.Enregistre(nick)
        if a_jouer[0] == "n":
            labyrinthe_c.n(int(a_jouer[1:]))
            labyrinthe_c.Enregistre(nick)
    if a_jouer.lower() == "e":
        labyrinthe_c.e()
        labyrinthe_c.Enregistre(nick)
    elif a_jouer.lower() == "o":
        labyrinthe_c.o()
        labyrinthe_c.Enregistre(nick)
    elif a_jouer.lower() == "s":
        labyrinthe_c.s()
        labyrinthe_c.Enregistre(nick)
    elif a_jouer.lower() == "n":
        labyrinthe_c.n()
        labyrinthe_c.Enregistre(nick)
    if a_jouer == "q":
        sieur = tm.askquestion("Sortir", "Vous voulez sortir vraiment?")
        if sieur:
            exit()

    visualiser.config(state=NORMAL)
    visualiser.delete('1.0', END)
    visualiser.insert(INSERT, labyrinthe_c)
    visualiser.config(state=DISABLED)
    mouvement_entre.delete(0, 'end')


# Nouveux joueur
# Pour vérifier si le nombre que vous êtes entré est dans la liste
def nouveux_jouer(vm_master, LesCartes, JouerEntry, JouerBouton, JouerExit):
    try:
        if cartes[int(JouerEntry.get()) - 1]:
            nouveux_labyrinthe = labyrinthes(f"cartes/test.txt")
            Reg_carte = Text(vm_master)
            Reg_carte.insert(INSERT, nouveux_labyrinthe)
            Reg_carte.config(state=DISABLED, height=nouveux_labyrinthe.valeur_deplacement,
                             width=nouveux_labyrinthe.valeur_deplacement)
            Reg_carte.config(padx=10)
            Reg_carte.grid(row=2, columnspan=2)

            EcrireMouvement = Label(vm_master, text="Écrire le mouvement")
            EcrireMouvement.grid(row=3, columnspan=2, pady=5)
            EntryMouvement = Entry(vm_master)
            EntryMouvement.grid(row=4, columnspan=2, pady=5)

            EntreButon = Button(vm_master, text="Entre", width=5,
                                command=lambda: mouvement(EntryMouvement.get(), nouveux_labyrinthe,
                                                          Contenu.entry_nick.get(),
                                                          Reg_carte, EntryMouvement))
            EntreButon.grid(row=5, column=0, pady=5)
            ExitButon = Button(vm_master, text="Exit", command=lambda: exit(), width=5)
            ExitButon.grid(row=5, column=1, pady=5)
            LesCartes.destroy()
            JouerEntry.destroy()
            JouerBouton.destroy()
            JouerExit.destroy()

    except IndexError:
        print(f"Le nombre {JouerEntry.get()} ne correspond pas à aucun labyrinthes.")
        tm.showerror("ERROR CARTE", f"Le nombre {JouerEntry.get()} ne correspond pas à aucun labyrinthes.")


# Modifier cartes
def modifier_cartes(n_cart, plan_modifie, vm_carte):
    with open(f"cartes/{n_cart}.txt", "w") as edit_carte:
        edit_carte.write(plan_modifie)
    tm.showinfo("Modifier", "La carte a été modifiée, pour la visualiser il faut redémarre le jeu")
    vm_carte.destroy()


# Vérifier cartes existent
def verifier_cartes(n_cart, plan, nom_entry, button_enregistre, vm_carte):
    if n_cart + "." in cartes:
        editer = tm.askyesno("Editeur de cartes",
                             f"Desole mais il existe une carte avec le nom {n_cart} vous voulez la modifiez?")
        if editer:
            plan.delete('1.0', END)

            with open(f"cartes/{n_cart}.txt", "r") as edit_carte:
                ma_carte_a_editer = edit_carte.read()
            plan.insert(INSERT, ma_carte_a_editer)
            button_enregistre.config(text="Modifier",
                                     command=lambda: modifier_cartes(n_cart, plan.get('1.0', END), vm_carte))
        else:
            tm.showwarning("Editeur de cartes", "Désole mais vous ne pouvez pas enregistre une carte avec le même nom")
    else:
        Nouvelle_carte = Carte(n_cart, plan.get('1.0', END))
        Nouvelle_carte.Regist_carte()
        tm.showinfo("Registre", "Carte enregistre avec succès, pour la visualiser il faut redémarre le jeu")
        nom_entry.delete(0, 'end')
        plan.delete('1.0', END)


# Createur des cartes
def createur_carte():
    vm_createur_carte = Toplevel()
    vm_createur_carte.title("Créateur de cartes")
    vm_createur_carte.iconbitmap('img/ico.ico')

    N_carteLabel = Label(vm_createur_carte, text="Nom de carte")
    N_carteLabel.config(font="Arial 14 bold")
    N_carteLabel.grid(row=0)

    N_carteEntry = Entry(vm_createur_carte)
    N_carteEntry.grid(row=0, column=1)

    EditCarte_Label = Label(vm_createur_carte, text="Éditeur:")
    EditCarte_Label.config(font="Arial 12 bold")
    EditCarte_Label.grid(row=1, columnspan=2)

    EditCarte_Text = Text(vm_createur_carte)
    EditCarte_Text.grid(row=2, columnspan=2, padx=20)

    EnregisButton = Button(vm_createur_carte, text="Enregistre",
                           command=lambda: verifier_cartes(N_carteEntry.get(), EditCarte_Text, N_carteEntry,
                                                           EnregisButton, vm_createur_carte))
    EnregisButton.grid(row=3, columnspan=1, pady=10)

    CancelButton = Button(vm_createur_carte, text="Cancel", command=lambda: vm_createur_carte.destroy())
    CancelButton.grid(row=3, column=1, pady=10)


# Interface
def deuxime_wm():
    root.withdraw()
    vm_deuxime = Toplevel()
    vm_deuxime.title("Labyrinthe")
    vm_deuxime.iconbitmap('img/ico.ico')

    Nickname_Label1 = Label(vm_deuxime, text=f"Bienvenu: {Contenu.entry_nick.get()}")
    Nickname_Label1.configure(font="Arial 14 bold")
    Nickname_Label1.grid(row=0, columnspan=2)

    # Si il y a une partie sauvegardée, on l'affiche, à compléter
    enregistre = []

    for nick_enregistre in os.listdir("score"):
        if nick_enregistre.endswith(".txt"):
            nick_nom = nick_enregistre[:-4]
            enregistre.append(nick_nom)
    if Contenu.entry_nick.get() in enregistre:
        continue_partie = tm.askquestion("PARTIE ENREGISTRÉE",
                                         "Vous avez une partie enregistrée, vous voulez continue?(Oui/Non) ")
        if continue_partie == "yes":
            labyrinthe_c = labyrinthes(f"score/{Contenu.entry_nick.get()}.txt")

            Reg_carte = Text(vm_deuxime)
            Reg_carte.insert(INSERT, labyrinthe_c)
            Reg_carte.config(state=DISABLED, height=labyrinthe_c.valeur_deplacement,
                             width=labyrinthe_c.valeur_deplacement)
            Reg_carte.config(padx=10)
            Reg_carte.grid(row=2, columnspan=2)

            EcrireMouvement = Label(vm_deuxime, text="Écrire le mouvement")
            EcrireMouvement.grid(row=3, columnspan=2, pady=5)
            EntryMouvement = Entry(vm_deuxime)
            EntryMouvement.grid(row=4, columnspan=2, pady=5)

            EntreButon = Button(vm_deuxime, text="Entre", width=5,
                                command=lambda: mouvement(EntryMouvement.get(), labyrinthe_c, Contenu.entry_nick.get(),
                                                          Reg_carte, EntryMouvement))
            EntreButon.grid(row=5, column=0, pady=5)
            ExitButon = Button(vm_deuxime, text="Exit", command=lambda: exit(), width=5)
            ExitButon.grid(row=5, column=1, pady=5)

    else:
        # On demande la carte à joue
        LesCartes = Label(vm_deuxime, text=f"Les cartes que tu poura jouait sont\n {list_cartes}")
        LesCartes.configure(font="Arial 12 bold")
        LesCartes.grid(row=1, columnspan=2)

        JouerEntry = Entry(vm_deuxime)
        JouerEntry.grid(row=2, pady=5, columnspan=2)

        JouerBouton = Button(vm_deuxime, text="Jouer", width=5,
                             command=lambda: nouveux_jouer(vm_deuxime, LesCartes, JouerEntry, JouerBouton, JouerExit))
        JouerBouton.grid(row=3, pady=5, column=0)

        JouerExit = Button(vm_deuxime, text="Exit", command=lambda: exit(), width=5)
        JouerExit.grid(row=3, pady=5, column=1)

    vm_deuxime.resizable(height=False, width=False)
    vm_deuxime.bind('<Escape>', lambda esc: vm_deuxime.destroy())


def ferme_vm():
    root.destroy()


def verificateur_nick(nick):
    if nick != "":

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

        # Créateur des cartes
        self.button_cartes = Button(self, text="Créer une carte", command=lambda: createur_carte())
        self.button_cartes.grid(row=2, pady=5, columnspan=2)

        self.pack()


root = Tk()
root.title("Labyrinthe")
root.iconbitmap('img/ico.ico')

Contenu = GUI_Lab(root)
root.geometry("350x110")
root.resizable(height=False, width=False)
root.bind('<Escape>', lambda esc: root.destroy())
# Mensagge de bienvenu
tm.showinfo("BIENVENU", "-BIENVENU DANS LE JEUX DE LABYRINTHE\n Pour commencé saisissez vous nick")
root.mainloop()
# Creation et edition by DelaHoz
