import os
import pickle
from donnes import *


def utilise_les_donnes():
    if os.path.exists(nom_de_ficher_score):
        print("Si existe")

    else:
        print("Il n'y a pas de score registre")


utilise_les_donnes()
