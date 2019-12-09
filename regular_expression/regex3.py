import re

nom1 = "Jara López"

nom2 = "Antonio Gómez"

nom3 = "Lara López"

if re.match(".ara", nom1, re.I):
    print("Hemos encontrado el nombre")
else:
    print("No lo hemos encontrado")

if re.search("López", nom1):
    print("Hemos encontrado un Lopez")
else:
    print("No hemos encontrado un Lopez")

print("\n")
codig1 = "ajsdlaskdjaslkdasjldaskldas71dasdasdasdasdas"

codig2 = "dasdasdasdafsdfasdfasdlfjkasd"

codig3 = "fasdfjlkasdfkadlsfljakdfadf"

if re.search("71", codig1):
    print("Hemos encontrado el 71")
else:
    print("No hemos encontrado el 71")

chaine1 = "Jara Lopez"

chaine2 = "5644564165"

chaine3 = "a54654655"

if re.match("\d", chaine2):
    print("Hemos encontrado el numero")
else:
    print("No hemos encuntrado el numero")