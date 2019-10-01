class Persona():

    def __init__(self, nombre, edad, lugar_residencia):
        self.nombre = nombre
        self.edad = edad
        self.lugar_residencia = lugar_residencia

    def descripcion(self):
        print("Nombre: {0} \nEdad: {1} \nLugar Residencia: {2}".format(self.nombre, self.edad, self.lugar_residencia))


class Empleado(Persona):

    def __init__(self, salario, antiguedad, nombre_empleado, edad_empleado, resiendia_empleado):
        super().__init__(nombre_empleado, edad_empleado, resiendia_empleado)
        self.salario = salario
        self.antiguedad = antiguedad

    def descripcion(self):
        super().descripcion()
        print("Salario: {} \nAntiguedad: {}".format(self.salario, self.antiguedad))


Andres = Persona("Andres", 21, "Colombia")

Andres.descripcion()

print(isinstance(Andres, Empleado))
