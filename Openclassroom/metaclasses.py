# Retour sur le processus d'instanciation
class Personne:
    """Classe définissant une personne.

    Elle possède comme attributs:
    nom -- le nom de la personne
    prenom -- son prénom
    age -- son âge
    lieu_residence -- son lie de résidence

    Le nom et le prénom doivent être passés au constructeur.
    """

    # Utilization la méthode __new__
    def __new__(cls, nom, prenom, *args, **kwargs):
        print(f"Appel de la méthode __new__ de la classe {cls}")
        instance = super(Personne, cls).__new__(cls, *args, **kwargs)
        return instance

    def __init__(self, nom, prenom, *args, **kwargs):
        """Constructeur de notre personne."""
        super(Personne, self).__init__(*args, **kwargs)
        print("Appel de la méthode __init__")
        self.nom = nom
        self.prenom = prenom
        self.age = 23
        self.lieu_residence = "Sabaneta"


A = Personne("DelaHoz", "Andres")

# Créer une classe dynamiquement
print(type(5))
print(type("une chaine"))
print(type([1, 2, 3]))
print(type(int))
print(type(str))
print(type(list))

# Créer une classe dynamiquement

B = type("Persone", (), {})
print(B)
C = B
print(dir(C))


def creer_personne(personne, nom, prenom):
    """La fonction qui jouera la rôle de constructeur pour notre classe Personne.

    Elle prend en paramètre, outre la personne:
    nom -- son nom
    prenom -- son prenom
    """
    personne.nom = nom
    personne.prenom = prenom
    personne.age = 22
    personne.lieu_residence = "Sabaneta"


def presenter_personne(personne):
    """Foction présente la personne"""
    print(f"Persone {personne.nom} {personne.prenom} il a une age de {personne.age}")


methodes = {
    "__init__": creer_personne,
    "presenter": presenter_personne
}

Personne2 = type("Personne", (), methodes)
john = Personne2("Doe", "John")
print(john.nom)
print(john.prenom)
print(john.age)
john.presenter()


# Définition d'une métaclasse

class MaMetaClasse(type):
    """Example d'une métaclasse"""

    def __new__(metacls, nom, bases, dict):
        """Création de notre classe."""
        print(f"On crée la classe {nom}")
        return type.__new__(metacls, nom, bases, dict)


class MaClasse(metaclass=MaMetaClasse):
    pass


# Les métaclasses en action

# Biblio_Widgets = {
#     "Widget": Widget,
#     "Bouton": Bouton,
#     "CaseACocher": CaseACoher,
#     "Menu": Menu,
#     "Cadre": Cadre
# }

trace_classes = {}


class MetaWidget(type):
    """Notre métaclasse pour nos Widgets.

    Elle hérite de type, puisque c'est une métaclasse.
    Elle va écrire dans le dictionnaire trace_classes à chaque fois
    qu'une classe sera crée, utilisant cette métaclasse naturellement."""

    def __init__(cls, nom, bases, dict):
        """Constructeur de notre métaclasse, appelé quand on crée une classe."""
        type.__init__(cls, nom, bases, dict)
        trace_classes[nom] = cls


class Widget(metaclass=MetaWidget):
    """Classe mère de tous nos widgets."""
    pass


print(trace_classes)


class Bouton(Widget):
    """Une classe définissant le widget bouton."""
    pass


print(trace_classes)

# En résumé
#
#     Le processus d'instanciation d'un objet est assuré par deux méthodes,__new__et__init__.
#
#     __new__est chargée de la création de l'objet et prend en premier paramètre sa classe.
#
#     __init__est chargée de l'initialisation des attributs de l'objet et prend en premier paramètre l'objet précédemment créé par__new__.
#
#     Les classes étant des objets, elles sont toutes modelées sur une classe appelée métaclasse.
#
#     À moins d'être explicitement modifiée, la métaclasse de toutes les classes esttype.
#
#     On peut utilisertypepour créer des classes dynamiquement.
#
#     On peut faire hériter une classe detypepour créer une nouvelle métaclasse.
#
#     Dans le corps d'une classe, pour spécifier sa métaclasse, on exploite la syntaxe suivante :class MaClasse(metaclass=NomDeLaMetaClasse):.