# Découvrez la portée des variables et les références
a = 5  # Pour example on definit une variable normale


def voir_a():
    print("La variable a = {}".format(a))  # On peut voir qu'on peut faire appelle à la variable dans un def


voir_a()  # Si on fait appelle à la variables définies va nous montrer la valeur de la variable

# La portée de nos variables

var = 1


def set_var(nouvelle_variable):
    try:
        print("Avant l'affectation, notre variable var vaut {}".format(var))
    except NameError:
        print("La variable var n'existe pas encore.")
    var = nouvelle_variable
    print("Après l'affectation, notre variable var vaut {}".format(var))


set_var("Hola")


# Une fonction modifiant des objets
def ajouter(liste, valeur_a_ajouter):
    liste.append(valeur_a_ajouter)


ma_liste = ['a', 'e', 'i']
ajouter(ma_liste, 'o')
print(ma_liste)

# Et les références, dans tout cela?

mliste = [1, 2, 3]
mliste2 = mliste
mliste2.append(4)  # Si on modifie l'objet depuis une des deux variable, le changement sera visible depuis les deux
# variables, et comment on a utilise le methode append c'est une modification de l'objet
print(mliste2)
print(mliste, "\n")

# Pour modifier une liste sans toucher à l'autre il faut ajoute le methode list, pour copier le contenu de la liste
mliste = [1, 2, 3]
mliste2 = list(mliste)
mliste2.append(4)
print("On ajoute la methode list", mliste2, "\n")
print(mliste)

# On va faire la meme chose me avec le dictionnaire
mon_dic = {"Mon primier": 1, "Mon deuxieme": 2, "Mon troxieme": 3}
mon_dic2 = mon_dic
mon_dic2.update({"Mon quatrieme": 4})
print(mon_dic2)
print(mon_dic)

# Les variables globales
i = 4


def appell_i():
    global i
    i += 1


print(i, "\n")
appell_i()
print(i)

