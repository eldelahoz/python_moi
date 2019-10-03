import pickle

with open("lista_nombres", "rb") as lista:
    lista_nombres = pickle.load(lista)

print(lista_nombres)
