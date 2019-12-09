# Esta funcion verifica que los elementos de una secuencia cumple una condicion, devolviendo un itereador con los
# elementos que cumplen dicha condicion
"""def numero_par(num):
    if num % 2 == 0:
        return True"""
"""
nombres = [17, 24, 7, 39, 8, 51, 92]

print(list(filter(lambda nombre_par: nombre_par % 2 == 0, nombres)))"""


class Employe:
    def __init__(self, nom, charge, salaire):
        self.nom = nom
        self.charge = charge
        self.salaire = salaire

    def __str__(self):
        return f"Le nom: {self.nom}, Le charge {self.charge}, Le Salaire: {self.salaire}"


ListEmploye = [
    Employe("Juan", "Directeur", 75000),
    Employe("Ana", "Presidenta", 85000),
    Employe("Antonio", "Administrativo", 25000),
    Employe("Sara", "Secretaria", 27000),
    Employe("Mario", "Botones", 21000),
]

salarios_altos = filter(lambda employe: employe.salaire > 50000, ListEmploye)

for EmployeSalaire in salarios_altos:
    print(EmployeSalaire)
