# -*-coding:Utf-8 -*

"""Ce fichier contient le code principal du jeu.

Exécutez-le avec Python pour lancer le jeu.

"""

import os

from carte import *
from labyrinthe import *

# On charge les cartes existantes
cartes = []
conteur = 0
for nom_fichier in os.listdir("cartes"):
    if nom_fichier.endswith(".txt"):
        chemin = os.path.join("cartes", nom_fichier)
        nom_carte = nom_fichier[:-3].lower()
        cartes.append(nom_carte)
        with open(chemin, "r") as fichier:
            contenu = fichier.read()
            # Création d'une carte, à compléter

# On affiche les cartes existantes
print("Labyrinthes existants :")
for i, carte in enumerate(cartes):
    print(f"  {i + 1} - {carte}")

# Si il y a une partie sauvegardée, on l'affiche, à compléter

# ... Complétez le programme ...
a_jouer = input("Entrez un numéro de labyrinthe pour commencer à jouer: ")
# a_jouer = 1


def verifie_labyrinthes():
    try:
        if cartes[int(a_jouer) - 1] in cartes:
            return True
        else:
            return False
    except IndexError:
        print(f"Le nombre {a_jouer} ne correspond pas à aucun labyrinthes.")


if verifie_labyrinthes():
    print("Le labyrinthe existe")
    route = os.path.join("cartes", cartes[int(a_jouer) - 1] + "txt")
    with open(route, "r") as TestOuver:
        labyrinthe_on = TestOuver.read()
    # print(labyrinthe_on)
    grille = {}
    portes = {}
    nouveux = ""
    for nombre, value in enumerate(labyrinthe_on):
        if value == "O":
            grille[nombre] = value
        nouveux += value
    labyrinthe_on = Labyrinthe("X", labyrinthe_on, None)
print(labyrinthe_on)
# print(type(labyrinthe_on))
# mouvement = input(">")
#
# if mouvement.lower() == "s":
#     ou_roboc = labyrinthe_on.find("X")
#     print(labyrinthe_on)
os.system("pause")
