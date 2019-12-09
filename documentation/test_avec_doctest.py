import doctest


def email_corectement(email):
    """
    La funcion Comprueba Mail
    Evalua un mail recibido en busca de la @ si tiene
    una @ es correcto, si tiene mas de una @ es incorrecto
    Si la @ esta al final es incorrecto

    >>> email_corectement('andres@delahoz.es')
    True

    >>> email_corectement('juancursos.es@')
    False

    >>> email_corectement('andres@@@hoz.es')
    False

    >>> email_corectement('andresdelahoz.es')
    False
    """
    arroba = email.count('@')
    if arroba != 1 or email.rfind('@') == (len(email) - 1) or email.find('@') == 0:
        return False
    else:
        return True


doctest.testmod()
