ma_liste = [1, 2, 3, 4, 5]
for element in ma_liste:
    print(element)
    if element == 4:
        break

ma_chaine = "test"
iterateur_de_ma_list = iter(ma_liste)
iterateur_de_ma_chaine = iter(ma_chaine)
print(iterateur_de_ma_chaine)
print(next(iterateur_de_ma_chaine))
print(iterateur_de_ma_list)
try:
    print(next(iterateur_de_ma_list))
    print(next(iterateur_de_ma_list))
    print(next(iterateur_de_ma_list))
    print(next(iterateur_de_ma_list))
except StopIteration:
    print("Il n'y a pas d'autre valeur")

print("--------Créons nos itérateurs--------")


class RevStr(str):
    """Classe reprenant les méthodes et attributs des chaînes construites
    depuis 'str'. On se contente de définir une méthode de parcours différente:
    au lieu de parcourir la chaîne de la première à la dernière lettre, on la
    parcourt de la dernière à la première

    Les autres méthodes, y compris le constructeur, n'ont pas besoin d'être redéfinies"""

    def __iter__(self):
        """Cette méthode renvoi un itérateur parcourant la chaîne dans le sens
        inverse de celui de 'str'"""
        return ItRevStr(self)


class ItRevStr:
    """Un itérateur permettand de parcourir una chaîne de la dernière lettre
    à la première. On stocke dans des attributs la position courante et la chaîne
    à parcourir"""

    def __init__(self, chaine_a_parcourir):
        """On se positionne à la fin de la chaîne"""
        self.chaine_a_parcourir = chaine_a_parcourir
        self.position = len(chaine_a_parcourir)

    def __next__(self):
        """Cette méthode doit renvoyer l'élement suivant dans le parcours,
        ou lever l'execption 'StopIteration' si le parcours est fini"""

        if self.position == 0:
            raise StopIteration
        self.position -= 1
        return self.chaine_a_parcourir[self.position]


ma_chaine2 = RevStr("Bonjour")
print(ma_chaine2)
for letter in ma_chaine2:
    print(letter)

print("--------Les générateurs--------")


def mon_generateur():
    """Notre premier générateur. Il va simplement renvoyer 1,2 et 3"""
    yield 1
    yield 2
    yield 3


print(mon_generateur())
for nombre in mon_generateur():
    print(nombre)

print("Separateur ------")


def intervalle(a, b):
    """Géérateur parcourant la série des entiers entre borne_inf et borne_sup"""
    a += 1
    while a < b:
        yield a
        a += 1


for nombre2 in intervalle(5, 10):
    print(nombre2)

print("Interrompre la boucle")
generateur = intervalle(5, 20)
for nombre3 in generateur:
    print(nombre3)
    if nombre3 > 17:
        generateur.close()

print("Separateur ------¬\nEnvoyer des données à notre générateur")


def intervalle2(borne_inf, borne_sup):
    """Générateur parcourant la série des entiers entre borne_inf et borne_sup
    Notre générateur doit pouvoir "sauter" une cernaine plage de nombres
    en foction d'une valeur qu'on lui donne pendant le parcours. La
    valeur qu'on lui passe est la nouvelle valeur de borne_inf.

    Note: borne_inf doit être inférieure à borne_sup"""

    borne_inf += 1
    while borne_inf < borne_sup:
        valeur_recue = (yield borne_inf)
        if valeur_recue is not None:
            borne_inf = valeur_recue
        borne_inf += 1


generateur2 = intervalle2(5, 25)
for element in generateur2:
    if element == 15:
        generateur2.send(20)
    print(element, end=", ")
