import re

chaine = "On vas a apprendre l'expresionnes racionelles"

chaine2 = 'Vamos a aprender expresiones regulares en Python. Python es un lenguaje de programacion'

textcherche = 'Python'

print(len(re.findall(textcherche, chaine2)))

text = "apprendre"

if re.search(text, chaine) is not None:
    print("Je trouve le texte")
else:
    print("Je ne pas trouve le texte")
