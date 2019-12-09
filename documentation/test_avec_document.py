import doctest


def air_de_triangle(base, hauteur):
    """
    Calcula el area de un triangulo dado
    :param base: La base del triangulo
    :param hauteur: La altura
    :return: Te regresa el valor del area
    >>> air_de_triangle(3, 6)
    'El area del triangulo es: 9.0'
    >>> air_de_triangle(2, 4)
    'El area del triangulo es: 4.0'
    >>> air_de_triangle(5, 10)
    'El area del triangulo es: 25.0'
    """
    return "El area del triangulo es: " + str((base * hauteur) / 2)


print(air_de_triangle(5, 10))
