import doctest
import math


def RaizCuadrada(list_nombre):
    """
    La funcion devuelve una lista con la raiz cuadrada de los elementos numericos
    pasados por parametros en otra lista

    >>> lista=[]
    >>> for i in [4, 9, 16]:
    ...    lista.append(i)
    >>> RaizCuadrada(lista)
    [2.0, 3.0, 4.0]

    >>> lista=[]
    >>> for i in [4, -9, 16]:
    ...    lista.append(i)
    >>> RaizCuadrada(lista)
    Traceback (most recent call last):
        ...
    ValueError: math domain error
    """
    return [math.sqrt(n) for n in list_nombre]


# print(RaizCuadrada([9, 16, 25, 36]))
doctest.testmod()