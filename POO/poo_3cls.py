class Compteur:
    """Cette classe possède un attribut de classe qui s'incrémente à chaque
    fois que l'on crée un objet de ce type"""

    objets_crees = 0  # Le compteur vaut 0 au départ

    def __init__(self):
        """À chaque fois qu'on crée un objet, on incrémente le compteur"""
        Compteur.objets_crees += 1


a = Compteur()
print(Compteur.objets_crees)
b = Compteur
print(Compteur.objets_crees)


class Compteur2:
    """Cette classe possède un attribut de classe qui s'incrémente à chaque
    fois que l'on crée un objet de ce type"""

    objets_crees = 0  # Le compteur vaut 0 au départ

    def __init__(self):
        """À chaque fois qu'on crée un objet, on incrémente le compteur"""
        Compteur2.objets_crees += 1

    def combien(cls):
        """Méthode de classe affichant combien d'objets ont été créés"""
        print("Jusqu'à présent, {} objets ont été créés.".format(
            cls.objets_crees))

    combien = classmethod(combien)


Compteur2.combien()
c = Compteur2()
d = Compteur2()
c.combien()


class Test:
    """Une classe de test tout simplement"""

    def afficher():
        """Fonction chargée d'afficher quelque chose"""
        print("On affiche la même chose.")
        print("peu importe les données de l'objet ou de la classe.")

    afficher = staticmethod(afficher)


class Test2():

    def __init__(self):
        self.mon_atribute = "ok"


t = Test()
Test.afficher()
voir = Test2()
voir.__dict__["mon_atribute"] = "pas ok"

print(voir.mon_atribute)