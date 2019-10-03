import pickle
from serializar2 import *

with open("losCoches", "rb") as losCoches:
    coches = pickle.load(losCoches)

for hoz in coches:
    print(hoz.estado())
