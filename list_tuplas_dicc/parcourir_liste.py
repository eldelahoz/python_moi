ma_liste = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
i = 0  # Notre indice pour la boucle while
while i < len(ma_liste):
    print(ma_liste[i])
    i += 1

print("Espace", "\n")
for cernaine_variable in ma_liste:
    print(cernaine_variable)

print("Espace", "\n")

# La fonctionenumerate
for i, elt in enumerate(ma_liste):
    print("À l'indice {} se trouve {}.".format(i, elt))

print("Espace", "\n")
# Un autre example
autre_liste = [
    [1, 'a'],
    [4, 'd'],
    [7, 'g'],
    [26, 'z'],
]  # J'ai étalé la liste sur plusieurs lignes
for nb, lettre in autre_liste:
    print("La lettre {} est la {}e de l'alphabet.".format(lettre, nb))
print("Espace", "\n")

# Des chaînes aux list_tuplas_dicc
ma_chaine = "Bonjour à tous"
ma_chaine = ma_chaine.split(" ")
print(ma_chaine)

# Des list_tuplas_dicc aux chaînes
ma_liste_aux_chaines = " ".join(ma_chaine)
print(ma_liste_aux_chaines)


# Une application pratique
def afficher_flottant(flottant):
    """Fonction prenant en paramètre un flottant et renvoyant une chaîne de caractères représentant la troncature de ce nombre. La partie flottante doit avoir une longueur maximum de 3 caractères.

    De plus, on va remplacer le point décimal par la virgule"""

    if type(flottant) is not float:
        raise TypeError("Le paramètre attendu doit être un flottant")
    flottant = str(flottant)
    partie_entiere, partie_flottante = flottant.split(".")
    # La partie entière n'est pas à modifier
    # Seule la partie flottante doit être tronquée
    return ",".join([partie_entiere, partie_flottante[:3]])


print(afficher_flottant(1.555555))


# compteur de voyelles
def get_vowels_numbers(word):
    # créer un compteur de voyelles
    nb_vowels = 0

    # pour chaque lettre du mot vous verifiez s'il s'agit d'un voyelle
    for letter in word:
        if letter in ['a', 'e', 'i', 'o', 'u', 'y']:
            # on ajoute un au compteur
            nb_vowels += 1

    # à la fin de la fonction, vous allez renvoyer le compteur
    return nb_vowels


word = input("Entrer un mot")
vowels_count = get_vowels_numbers(word)
print("Il y a", vowels_count, "voyelles dans le mot", word)
