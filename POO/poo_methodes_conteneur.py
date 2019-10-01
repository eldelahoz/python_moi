class ZDict:
    def __init__(self):
        self._dictionnaire = {}

    def __getitem__(self, item):
        return self._dictionnaire[item]

    def __setitem__(self, key, value):
        self._dictionnaire[key] = value

    def __repr__(self):
        return "Tout le dictionnaire: {}".format(self._dictionnaire)


MonDic = ZDict()
MonDic.__setitem__(1, "Salut")
print(MonDic.__getitem__(1))
print(MonDic)

ma_liste = [1, 2, 3, 4, 5]
print(8 in ma_liste)
print(ma_liste.__contains__(8))
print(ma_liste.__len__())
print("\n")


class Duree:

    def __init__(self, min=0, sec=0):
        self.min = min
        self.sec = sec

    def __str__(self):
        return "{0:02}:{1:02}".format(self.min, self.sec)

    def __add__(self, objet_a_ajouter):
        """L'objet a ajouter est un entier, le nombre de secondes"""
        nouvelle_durre = Duree()
        # On va copier self dans l'objet cree por avoir la meme duree
        nouvelle_durre.min = self.min
        nouvelle_durre.sec = self.sec
        # On ajoute la durée
        nouvelle_durre.sec += objet_a_ajouter
        # Si le nombre de secondes >= 60
        if nouvelle_durre.sec >= 60:
            nouvelle_durre.min += nouvelle_durre.sec // 60
            nouvelle_durre.sec = nouvelle_durre.sec % 60
        # On renvoie la nouvelle durée
        return nouvelle_durre

    def __radd__(self, objet_a_ajouter):
        """Cette méthode est appelée si on écrit 4 + objet et que
        le premier objet (4 dans cet exemple) ne sait pas comment ajouter
        le second. On se contente de rediriger sur __add__ puisque,
        ici, cela revient au même : l'opération doit avoir le même résultat,
        posée dans un sens ou dans l'autre"""

        return self + objet_a_ajouter

    def __iadd__(self, objet_a_ajouter):
        self.sec = objet_a_ajouter

        if self.sec >= 0:
            self.min += self.sec // 60
            self.sec = self.sec % 60

        return self


d1 = Duree(3, 5)
print(d1)
d1.__add__(4)
print(d1.__add__(60))
d2 = 4 + d1
print(d2)
d3 = Duree(5)
d3 += 70
print(d3)
