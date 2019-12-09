from operator import itemgetter, attrgetter

prenoms = ["Jacques", "Laure", "André", "Victoire", "Albert", "Sophie"]
prenoms.sort()
print(prenoms)
prenoms2 = ["Jacques", "Laure", "André", "Victoire", "Albert", "Sophie"]
sorted(prenoms2)
# print(sorted(prenoms2))
print(prenoms2)
print(sorted([1, 8, -2, -3, 15, 9]))
print(sorted(["1", "8", "-3", "10", "9"]))
print("---------Trier avec des clés précises---------")
etudiants = [
    ("Clément", 14, 16),
    ("Charles", 12, 15),
    ("Oriane", 14, 18),
    ("Thomas", 11, 12),
    ("Damien", 12, 15),
]
print(sorted(etudiants))
doubler = lambda x: x * 2
print(doubler)
print(doubler(8))
print(sorted(etudiants, key=lambda colonnes: colonnes[2]), "\n")
print("--->Trier une liste d'objets")


class Etudiant:
    """Classe représentant un étudiant.

    On représente un étudiant par son prénom (attribut prenom), son âge
    (attribut age) et sa note moyenne (attribut moyenne, entre 0 et 20).

    Paramètres du constructeur :
        prenom -- le prénom de l'étudiant
        age -- l'âge de l'étudiant
        moyenne -- la moyenne de l'étudiant
    """

    def __init__(self, prenom, age, moyenne):
        self.prenom = prenom
        self.age = age
        self.moyenne = moyenne

    def __repr__(self):
        return f"<Étudiant {self.prenom} (âge={self.age}, moyenne={self.moyenne})"


etudiant = [
    Etudiant("Clément", 14, 16),
    Etudiant("Charles", 12, 15),
    Etudiant("Oriane", 14, 18),
    Etudiant("Thomas", 11, 12),
    Etudiant("Damien", 12, 15),
]

print(sorted(etudiant, key=lambda abc: abc.moyenne))

print("--->Trier dans l'ordre inverse")
print(sorted(etudiant, key=lambda etudian: etudian.age, reverse=True), "\n")

print("---------Plus rapide et plus efficace---------")
# Module operator
print(sorted(etudiants, key=itemgetter(2)))
print(sorted(etudiant, key=attrgetter("moyenne")))
print(sorted(etudiant, key=attrgetter("age", "moyenne")))
print("--->Chaînage de tris")


class LigneInventaire:
    """
    Classe représentant une ligne d'un inventaire de vente.

    Attributs attendus par le ocnstructeur:
        produit -- le nom du produit
        prix -- le prix unitaire du produit
        quantite -- la quantité vendue du produit.
    """

    def __init__(self, produit, prix, quantite):
        self.produit = produit
        self.prix = prix
        self.quantite = quantite

    def __repr__(self):
        return f"<Ligne d'inventaire {self.produit} ({self.prix}X{self.quantite}"


# Création de l'inventaire
inventaire = [
    LigneInventaire("pomme rouge", 1.2, 19),
    LigneInventaire("orange", 1.4, 24),
    LigneInventaire("bannane", 0.9, 21),
    LigneInventaire("poire", 1.2, 24)
]

print(sorted(inventaire, key=attrgetter("prix", "quantite")))

inventaire.sort(key=attrgetter("quantite"), reverse=True)
print(sorted(inventaire, key=attrgetter("prix")))