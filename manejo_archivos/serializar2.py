import pickle


class Vehiculos():
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.enmarcha = False
        self.acelera = False
        self.frena = False

    def __str__(self):
        return "Marca:", self.marca, "\nModelo:", self.modelo, "\nEnmarcha:", self.enmarcha, "\nAcelerar:",self.acelera, "\nFrenar:", self.frena

    def arrancar(self):
        self.enmarcha = True

    def acelerar(self):
        self.acelera = True

    def frenar(self):
        self.frena = True

    def estado(self):
        print("Marca:", self.marca, "\nModelo:", self.modelo, "\nEnmarcha:", self.enmarcha, "\nAcelerar:",
              self.acelera, "\nFrenar:", self.frena)


class Furgoneta(Vehiculos):

    def carga(self, cargar):
        self.cargado = cargar
        if self.cargado:
            return "La furgoneta esta cargada"
        else:
            return "La furgoneta no esta cargada"


class Moto(Vehiculos):
    hcaballito = ""

    def caballito(self):
        self.hcaballito = "Voy haciendo el caballito"

    def estado(self):
        print("Marca:", self.marca, "\nModelo:", self.modelo, "\nEnmarcha:", self.enmarcha, "\nAcelerar:",
              self.acelera, "\nFrenar:", self.frena, "\n", self.hcaballito)


class VElectricos(Vehiculos):
    def __init__(self, marca, modelo):
        super().__init__(marca, modelo)
        self.autonomia = 100

    def cargarEnergia(self):
        self.cargando = True
        if self.cargando:
            self.autonomia = 100
            return "Vehiculo cargado"


coche1 = Vehiculos("Mazda", "MX2")
coche2 = Vehiculos("Mazda", "MX5")
coche3 = Vehiculos("Renault", "Megane")

coches = [coche1, coche2, coche3]
# Enregistre
with open("losCoches", "wb") as losCoches:
    losCoches = pickle.dump(coches, losCoches)

