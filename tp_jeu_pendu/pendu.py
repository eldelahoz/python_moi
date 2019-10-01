import random
import pickle
from donnes import *
from fonctions import *


"""with open('score', 'rb') as ficher:
    mon_score = pickle.Unpickler(ficher)
    contenu = mon_score.load()
    print(contenu["Andres"])
"""

# Mot aleatoira
mot_aleatoira = liste_mot[random.randrange(len(liste_mot))]
# Mot a voir
mot_revele = []
# Historiele de lettre
lettres_joue = []

print("Bienvenu a joue de pendu".center(40))

nom_joeur = input("Ecribe son nom: ")

# Le ficher est open
mon_score_r = open('score', 'rb')
mon_score = pickle.Unpickler(mon_score_r)
contenu = mon_score.load()
mon_score_r.close()
# Pour voir si le joeur il a deja jeux avant (Il est une fonctions dans le ficher fonctions.py)
joeur_enregistre(nom_joeur, contenu)

# C'est pour inserte de * dans la liste a revele
cacher_mot(mot_revele, mot_aleatoira)

# Commence de jeux
lettre_joue = input("Alor {} il faut que tu ecrit une lettre pour commence a jouer: ".format(nom_joeur))
contador = 0

# Les points de vie et un plus pour voir si la letre et bonne
while 1 < chance:
    # C'est mon while pour faire que le code detecte si le jouer a ecrit plus de 1 lettres au aucune
    une_sole_lettre(lettre_joue)
    """while len(lettre_joue) > 1 or len(lettre_joue) == 0:
        print("Desole mais vous deviez ecrit qu'une lettre".center(60))
        lettre_joue = input("Alor {} ecrit une lettre pour commence a jouer: ".format(nom_joeur))"""
    # C'est pour voir si le joeur a repete la lettre
    if lettre_joue in lettres_joue:
        print("Vous avez deja jouer c'etai lettre {}.".format(lettre_joue))
        lettre_joue = input("Ecrit autre lettre differente: ")
        lettres_joue.append(lettre_joue)
    elif lettre_joue not in mot_aleatoira:
        chance -= 1
        print("Vous vainez de perdre un point -1, point totale {}".format(chance))
        lettres_joue.append(lettre_joue)
        lettre_joue = input("Ecrit autre lettre: ")
    else:
        for nombre, lettre in enumerate(mot_aleatoira):
            if lettre in lettre_joue:
                print("Vous avez reussi {}".format(lettre))
                lettres_joue.append(lettre_joue)
                mot_revele.pop(nombre)
                mot_revele.insert(nombre, lettre)
        mot_revele_str = "".join(mot_revele)
        print(mot_revele_str)
        if mot_revele_str == mot_aleatoira:
            print("Vous avez gagne")
            contenu[nom_joeur] += chance
            print("{} tu nombre de points son: {}".format(nom_joeur, contenu[nom_joeur]))
            mon_score_w = open('score', 'wb')
            enregistre_score = pickle.Pickler(mon_score_w)
            enregistre_score.dump(contenu)
            mon_score_w.close()
            break
        lettre_joue = input("Ecrit une autre lettre {}: ".format(nom_joeur))
        contador += 1
        if contador > 3:
            sortir = input("Vous voulez continue a jouer?(oui/non):")
            if sortir.lower() == "non":
                break

"""for nombre, lettre in enumerate(mot_aleatoira):
        if lettre in lettre_joue:
            print("Vous avez reussi {}".format(lettre))
            mot_revele.pop(nombre)
            mot_revele.insert(nombre, lettre)
    mot_revele_str = "".join(mot_revele)
    print(mot_revele_str)
    if mot_revele_str == mot_aleatoira:
        print("Vous avez gagne")
        break
    lettre_joue = input("Ecrit une autre lettre {}: ".format(nom_joeur))
    contador += 1
    if contador > 3:
        sortir = input("Vous voulez continue a jouer?(oui/non):")
        if sortir.lower() == "non":
            break"""
"""mot_revele.insert(nombre, lettre)
print(mot_revele)"""
