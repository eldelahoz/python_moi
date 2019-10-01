class Personne:
    """Classe representant une personne"""

    def __init__(self, nom, prenom, age):
        """Constructeur de notre classe"""
        self.nom = nom
        self.prenom = prenom
        self.age = age

    def __repr__(self):
        return "Nom: {} Premon: {} Age: {}".format(self.nom, self.prenom, self.age)

    def __str__(self):
        return "{} {} avec l'age de {} ans".format(self.nom, self.prenom, self.age)


# Andres = Personne("De la Hoz", "Andres", 21)

# chaine = str(Andres)
# print(Andres, "\n", type(Andres))
# print(chaine, type(chaine))


class Protege:
    """Classe possedant une methode particuliere d'acces a ses attributs :
    Si l'attribut n'est pas trouve, on affiche une alerte et renvoie None"""

    def __init__(self):
        """On cree quelques attributs par defaut"""
        self.a = 1
        self.b = 2
        self.c = 3

    def __getattr__(self, item):
        """Si Python ne trove pas l'attribut nomme nom, il appele cette methode.
        On affiche une alarte"""
        print("Alerte! Il n'y a pas d'attribut {} ici!".format(item))

    def __delattr__(self, item):
        """On ne peut supprimer d'attribut, on leve lexception
        AtributeError"""

        raise AttributeError("Vous ne pouvez supprimer aucun attribut de cette class"
                             )


"""    def __setattr__(self, key, value):
        Methode appelee quand on fait objet.nom_attr = val_attr.
        On se charge d'enregistre l'obet

        object.__setattr__(self, key, value)
        self.enregistrer()"""


# pro = Protege()
# print(pro.a, pro.c, pro.b)
# print(pro.e)
# print(pro)


class MaClasse:

    def __init__(self):
        self.nom = "Andres"

    def __getattr__(self, item):
        print("Alerte! Il n'y a pas d'attribut {} ici!".format(item))

    def __setattr__(self, nom_attr, val_attr):
        """Méthode appelée quand on fait objet.nom_attr = val_attr.
        On se charge d'enregistrer l'objet"""

        object.__setattr__(self, nom_attr, val_attr)
        self.enregistrer()

    def __delattr__(self, item):
        """On ne peut supprimer d'attribut, on leve l'exception
                AtributeError"""
        raise AttributeError("Vous ne pouvez supprimer aucun attribut de cette class")


objet = MaClasse()
getattr(object, "nom")

