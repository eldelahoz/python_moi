# Aplica una funcion a cada elemento de una lista iterable (lista, tuplas, etc) devolviendo una lista con los resultados
class Employe:
    def __init__(self, nom, charge, salaire):
        self.nom = nom
        self.charge = charge
        self.salaire = salaire

    def __str__(self):
        return f"Le nom: {self.nom}, Le charge {self.charge}, Le Salaire: {self.salaire} €"


ListEmploye = [
    Employe("Juan", "Directeur", 6700),
    Employe("Ana", "Presidenta", 7500),
    Employe("Antonio", "Administrativo", 2100),
    Employe("Sara", "Secretaria", 2150),
    Employe("Mario", "Botones", 1800),
]


def calculo_comision(empleado):
    if empleado.salaire <= 3000:
        empleado.salaire = empleado.salaire * 1.03
    return empleado


listaEmpleadoComision = map(calculo_comision, ListEmploye)

for empleado in listaEmpleadoComision:
    print(empleado)
