# -*-coding:Utf-8 -*

"""Ce module contient la classe Labyrinthe."""
import tkinter.messagebox as tm


class labyrinthes:
    """

    """

    def __init__(self, ficher):
        self.labyrinthe = []
        self.obstacle = []
        self.valeur_deplacement = 0
        self.position_porte = 0
        with open(ficher, "r") as cartes:
            self.ma_carte_on = cartes.read()

        self.valeur_deplacement = self.ma_carte_on.splitlines()
        self.valeur_deplacement = len(self.valeur_deplacement[0]) + 1
        for a in self.ma_carte_on:
            if a == "O":
                self.obstacle.append(a)
            self.labyrinthe.append(a)

    def __repr__(self):
        viste_labyrinthe = ""
        for a in self.labyrinthe:
            viste_labyrinthe += a
        return viste_labyrinthe

    def e(self, nombre=1):
        for a in range(0, nombre):
            viste_labyrinthe = ""
            position = self.labyrinthe.index("X")
            # On gagne
            if self.labyrinthe[position + 1] == "U":
                self.labyrinthe[position + 1] = "X"
                self.labyrinthe[position] = " "
                for b in self.labyrinthe:
                    viste_labyrinthe += b

                tm.showinfo("GAGNE", "Vous avez gagne...")
                exit()

            if self.labyrinthe[position + 1] == ".":
                self.position_porte = position + 1
                self.labyrinthe[position + 1] = "X"
                self.labyrinthe[position] = " "

            if self.labyrinthe[position + 1] in self.obstacle:
                tm.showwarning("DEPLACEMENT", "Désole mais vous ne pouvez pas vous déplacer par là")
                break

            if self.labyrinthe[position + 1] == " ":
                self.labyrinthe[position + 1] = "X"
                self.labyrinthe[position] = " "
                if self.position_porte != 0:
                    self.labyrinthe[self.position_porte] = "."
                    self.position_porte = 0

            for b in self.labyrinthe:
                viste_labyrinthe += b

        return self.labyrinthe

    def o(self, nombre=1):
        for a in range(0, nombre):
            viste_labyrinthe = ""
            position = self.labyrinthe.index("X")
            # On gagne
            if self.labyrinthe[position - 1] == "U":
                self.labyrinthe[position - 1] = "X"
                self.labyrinthe[position] = " "
                for b in self.labyrinthe:
                    viste_labyrinthe += b

                tm.showinfo("GAGNE", "Vous avez gagne...")
                exit()

            if self.labyrinthe[position - 1] == ".":
                self.position_porte = position - 1
                self.labyrinthe[position - 1] = "X"

            if self.labyrinthe[position - 1] in self.obstacle:
                tm.showwarning("DEPLACEMENT", "Désole mais vous ne pouvez pas vous déplacer par là")
                break

            if self.labyrinthe[position - 1] == " ":
                self.labyrinthe[position - 1] = "X"
                self.labyrinthe[position] = " "
                if self.position_porte != 0:
                    self.labyrinthe[self.position_porte] = "."
                    self.position_porte = 0

            for b in self.labyrinthe:
                viste_labyrinthe += b

        return self.labyrinthe

    def s(self, nombre=1):
        for a in range(0, nombre):
            viste_labyrinthe = ""
            position = self.labyrinthe.index("X")
            # On gagne
            if self.labyrinthe[position + self.valeur_deplacement] == "U":
                self.labyrinthe[position + self.valeur_deplacement] = "X"
                self.labyrinthe[position] = " "
                for b in self.labyrinthe:
                    viste_labyrinthe += b

                tm.showinfo("GAGNE", "Vous avez gagne...")
                exit()
            if self.labyrinthe[position + self.valeur_deplacement] == ".":
                self.position_porte = position + self.valeur_deplacement
                self.labyrinthe[position + self.valeur_deplacement] = "X"
                self.labyrinthe[position] = " "

            if self.labyrinthe[position + self.valeur_deplacement] in self.obstacle:
                tm.showwarning("DEPLACEMENT", "Désole mais vous ne pouvez pas vous déplacer par là")
                break
            if self.labyrinthe[position + self.valeur_deplacement] == " ":
                self.labyrinthe[position + self.valeur_deplacement] = "X"
                self.labyrinthe[position] = " "
                if self.position_porte != 0:
                    self.labyrinthe[self.position_porte] = "."
                    self.position_porte = 0

            for b in self.labyrinthe:
                viste_labyrinthe += b

        return self.labyrinthe

    def n(self, nombre=1):
        for a in range(0, nombre):
            viste_labyrinthe = ""
            position = self.labyrinthe.index("X")
            # On gagne
            if self.labyrinthe[position - self.valeur_deplacement] == "U":
                self.labyrinthe[position - self.valeur_deplacement] = "X"
                self.labyrinthe[position] = " "
                for b in self.labyrinthe:
                    viste_labyrinthe += b

                tm.showinfo("GAGNE", "Vous avez gagne...")
                exit()

            if self.labyrinthe[position - self.valeur_deplacement] == ".":
                self.position_porte = position - self.valeur_deplacement
                self.labyrinthe[position - self.valeur_deplacement] = "X"
                self.labyrinthe[position] = " "

            if self.labyrinthe[position - self.valeur_deplacement] in self.obstacle:
                tm.showwarning("DEPLACEMENT", "Désole mais vous ne pouvez pas vous déplacer par là")
                break

            if self.labyrinthe[position - self.valeur_deplacement] == " ":
                self.labyrinthe[position - self.valeur_deplacement] = "X"
                self.labyrinthe[position] = " "
                if self.position_porte != 0:
                    self.labyrinthe[self.position_porte] = "."
                    self.position_porte = 0

            for b in self.labyrinthe:
                viste_labyrinthe += b

        return self.labyrinthe

    def Enregistre(self, nick_name):
        labyrinthe_enregistrement = ""
        for a in self.labyrinthe:
            labyrinthe_enregistrement += a
        with open(f"score/{nick_name}.txt", "w") as carte_ouverte:
            carte_ouverte.write(labyrinthe_enregistrement)
# Creation et edition by DelaHoz
