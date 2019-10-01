class Persone():

    def __init__(self, nom, prenom, age):
        self.nom = nom
        self.prenom = prenom
        self.age = age
        self._lieu_residence = "Colombie"

    def _get_lieu_residence(self):
        print("On a accedes a la residence")
        return self._lieu_residence

    def _set_lieu_residence(self):
        print("{} viens de c'est change de maison a {}".format(self.prenom, self._lieu_residence))

    pro_residence = property(_get_lieu_residence)


Andres = Persone("DelaHoz", "Andres", 21)

print(Andres._get_lieu_residence())

Andres._lieu_residence = "Paris"

print(Andres._get_lieu_residence())
print(Andres)
