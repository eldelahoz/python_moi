import pickle


class Personne:

    def __init__(self, nombre, genero, edad):
        self.nombre = nombre
        self.genero = genero
        self.edad = edad
        print("Une personne c'est à enregistre:", self.nombre)

    def __str__(self):
        return "Nombre: {}, Genero: {} Edad: {}".format(self.nombre, self.genero, self.edad)





class ListPersonnes:
    personnes = []

    def __init__(self):
        with open("FicherExterne", "ab+") as PersonnesEnregistre:
            PersonnesEnregistre.seek(0)
            try:
                self.personnes = pickle.load(PersonnesEnregistre)
                print("Se cargaron {} personas del FicherExterne".format(len(self.personnes)))
            except:
                print("El fichero esta vacio")

    def AppPersonnes(self, p):
        self.personnes.append(p)
        self.EnregistrePersonnesFicher()

    def printPersonnes(self):
        for hoz in self.personnes:
            print(hoz)

    def EnregistrePersonnesFicher(self):
        with open("FicherExterne", "wb") as FicherPourEnregistre:
            pickle.dump(self.personnes, FicherPourEnregistre)
        print("Ficher Enregistre...")

    def VoirFicherExterne(self):
        print("La informacion del fichero externo es la siguiente:")
        for hoz in self.personnes:
            print(hoz)


MonListe = ListPersonnes()
pers = Personne("Sandra", "Femenino", 29)
MonListe.AppPersonnes(pers)
MonListe.VoirFicherExterne()
