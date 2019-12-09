# Funciones anonimas
"""def Area_triangulo(base, altura):
    return (base * altura) / 2


print(Area_triangulo(5, 7))
"""
Area_triangulo = lambda base, altura: (base * altura) / 2

print(Area_triangulo(5, 7))

# -------Elevado al cubo
Al_cubo = lambda nombre: pow(nombre, 3)

print(Al_cubo(13))

# -------Destacar valor
destacar_valor = lambda comision: f"¡{comision}! €"

comision_ana = 15585

print(destacar_valor(comision_ana))