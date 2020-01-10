# -*-coding:Utf-8 -*

"""Ce module contient la classe Carte."""


class Carte:
    """Objet de transition entre un fichier et un labyrinthe."""

    def __init__(self, nom, chaine):
        self.nom = nom
        self.labyrinthe = chaine

    def __repr__(self):
        return f"<Carte {self.nom}>\n{self.labyrinthe}"

    def Regist_carte(self):
        labyrinthe_enregistrement = ""
        for a in self.labyrinthe:
            labyrinthe_enregistrement += a
        with open(f"cartes/{self.nom}.txt", "w") as carte_ouverte:
            carte_ouverte.write(labyrinthe_enregistrement)
# Creation et edition by DelaHoz
