import random
from donnes import *
from fonctions import *

print("Bienvenu a joue de pendu".center(40))
nom_joeur = input("Ecribe son nom: ")
lettre_joue = input("Alor {} il faut que tu ecrit une lettre pour commence a jouer: ".format(nom_joeur))
while len(lettre_joue) > 1:
    print("Desole mais vous deviez ecrit qu'une lettre".center(60))
    lettre_joue = input("Si vous plait ecrivez qu'une lettre: ")

mot_aleatoira = liste_mot[random.randrange(len(liste_mot))]
print(mot_aleatoira)
while letre in mot_aleatoira:
    print(letre)