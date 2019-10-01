class TableauNoir():
    mensagge_ecrit = ""
    veux_efface = ""

    def __init__(self):
        self.surface = ""

    def ecrire(self, menssage_ecrit):
        self.mensagge_ecrit = menssage_ecrit
        if self.surface != "":
            self.surface += "\n"
        self.surface += self.mensagge_ecrit

    def efface(self):
        self.veux_efface = input("Vous voulez effacer le tableau?(oui/non):")

        if self.veux_efface.lower() == "oui":
            self.surface = ""
            print("Surface efface")
        else:
            print("Surface non efface")

    def lire(self):
        print(self.surface)


MonTableau = TableauNoir()
MonTableau.ecrire("Je vais ecrit n'importe quoi")
MonTableau.ecrire("Mon deuxime ligne")
MonTableau.lire()
MonTableau.efface()
MonTableau.lire()

print(MonTableau.__dict__)
