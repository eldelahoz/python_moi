import os
import pickle
from donnes import *


def utilise_les_donnes():
    if os.path.exists(score):
        print("Si existe")

    else:
        print("Il n'y a pas de score registre")


def joeur_enregistre(joeur, liste_score):
    if joeur in liste_score:
        print("Tu est enregistre sur le jeux {}, et ton score est {}".format(joeur, liste_score[joeur]))
    else:
        print("Tu n'est pas enregistre sur le jeux")
        liste_score.update({joeur: 0})
        print("Tu vien d'etre enregistre {} tu as: {} points".format(joeur, liste_score[joeur]))


def cacher_mot(mot_cacher, mot_joeur):
    while len(mot_cacher) < len(mot_joeur):
        for nombre, lettre in enumerate(mot_joeur):
            mot_cacher.insert(nombre, "*")


def une_sole_lettre(lettre):
    while len(lettre) > 1 or len(lettre) == 0:
        print("Desole mais vous deviez ecrit qu'une lettre".center(60))
        lettre = input("Il faut ecrire une lettre pour commence a jouer: ")
