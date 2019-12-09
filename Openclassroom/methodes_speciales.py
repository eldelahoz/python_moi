import pickle


class ZDict:
    def __init__(self):
        self.__dictionnaire = {}

    def __repr__(self):
        return f"Les valeur sur la liste son {self.__dictionnaire}"

    def __getitem__(self, item):
        return self.__dictionnaire[item]

    def __setitem__(self, key, value):
        self.__dictionnaire[key] = value

    def __delitem__(self, key):
        del self.__dictionnaire[key]

    def __contains__(self, item):
        if item in self.__dictionnaire:
            return True
        else:
            return False

    def __len__(self):
        return len(self.__dictionnaire)


Listex = ZDict()
Listex.__dictionnaire = {1, 2, 3, 4}
conteur = 1
for i in range(5):
    Listex.__setitem__(i, conteur)
    conteur += 1
print(Listex.__getitem__(2))
print(Listex)
Listex.__delitem__(4)
print(Listex.__contains__(10))
print(Listex.__len__())

print("---------------Méthodes mathématiques")


class Duree:
    def __init__(self, min=0, sec=0):
        self.min = min
        self.sec = sec

    def __repr__(self):
        return f"{self.min:02}:{self.sec:02}"

    def __add__(self, other):
        nouvelle_duree = Duree()
        nouvelle_duree.min = self.min
        nouvelle_duree.sec = self.sec
        nouvelle_duree.sec += other

        if nouvelle_duree.sec >= 60:
            nouvelle_duree.min += nouvelle_duree.sec // 60
            nouvelle_duree.sec = nouvelle_duree.sec % 60
        self.min = nouvelle_duree.min
        self.sec = nouvelle_duree.sec
        print(f"Sont ajoutés {other} secondes")

    def __radd__(self, other):
        return self + other

    def __iadd__(self, other):
        self.sec += other
        if self.sec >= 60:
            self.min += self.sec // 60
            self.sec = self.sec % 60
        return self

    def __eq__(self, other):
        if self.min == other.min and self.sec == other.sec:
            return True
        else:
            return False

    def __gt__(self, other):
        if (self.min + self.sec) > (other.min + other.sec):
            return True
        else:
            return False


D1 = Duree(12, 8)
print(D1)
# D2 = D1 + 54
D1 + 42
print(D1)
50 + D1
D2 = Duree(8, 5)
D2 += 128
print(D2)
D3 = Duree(10, 3)
D4 = Duree(10, 3)
print(f"Le temps de {D3}")
print(D3.__gt__(D4))

print("----------------Méthodes spéciales utiles à pickle-------------")


class Temp:
    """Classe contenant plusieurs attributs, dont un temporaire"""

    def __init__(self):
        """Constructeur de notre objet"""
        self.attribut_1 = "une valeur"
        self.attribut_2 = "une autre valeur"
        self.attribut_temporaire = 5

    def __repr__(self):
        return f"Attribute 1: {self.attribut_1} Attribute 2: {self.attribut_2} Attibute temporaire: {self.attribut_temporaire}"

    def __getstate__(self):
        """Renvoie le dictionnaire d'attributs à sérialiser"""
        dict_attr = self.__dict__
        dict_attr["attribut_temporaire"] = 0
        return dict_attr

    def __setstate__(self, state):
        state["attribut_1"] = "deu valeur"
        self.__dict__ = state


A = Temp()

# print(A.__getstate__())
Liste_pour_enregistre = A.__getstate__()


def EnregistreFicher(Attribut):
    with open("test", "ab") as EnregistreHoz:
        pickle.dump(Attribut, EnregistreHoz)


def VoirFicher(nom):
    with open(nom, "rb") as EnregistreVoir:
        Liste = pickle.load(EnregistreVoir)
        return Liste


# EnregistreFicher(Liste_pour_enregistre)

ListaR = dict(VoirFicher("test"))
B = Temp()
B.__setstate__(ListaR)
print(B)
