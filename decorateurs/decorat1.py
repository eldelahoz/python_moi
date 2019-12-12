# Funciones que a su vez añaden funciones a otra funciones.
# Por eso se las denomina "decoradores", porque "decoran" a otras funciones. Les añaden funcionalidades.
# Estrctura de un decorador:
# - 3 Funciones (A, B, C), donde A recibe como parametro a B para devolver C.
# - Un decorador devuelve una funcion
def function_derocateur(function_parametre):
    def function_interne(*args, **kwargs):
        # Des acciones adicioneles qui decoran
        print("Le calcule viens de commence:")
        function_parametre(*args, **kwargs)
        # Des acciones adicionales qui decoran
        print("Le calcule est fini", "\n")

    return function_interne


@function_derocateur
def suma(nombre1, nombre2, nombre3):
    print(nombre1 + nombre2 + nombre3)


@function_derocateur
def resta(nombre1, nombre2):
    print(nombre1 - nombre2)


@function_derocateur
def potencia(base, exponente):
    print(pow(base, exponente))


suma(7, 5, 8)

resta(20, 5)

potencia(base=5, exponente=3)
