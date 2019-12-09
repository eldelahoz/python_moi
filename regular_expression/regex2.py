import re

list_prenom = [
    'Ana',
    'Pedro',
    'Maria',
    'Rosa',
    'Sandra',
    'Celia'
]

for element in list_prenom:
    if re.findall('[o-t]', element):
        print(element)

print("\n")
list_ville = [
    'Ma.1',
    'Se1',
    'Ma2',
    'Ba1',
    'Ma:3',
    'Va1',
    'Va2',
    'Ma4',
    'MaA',
    'Ma.5',
    'MaB',
    'Ma:C'
]

for element in list_ville:
    if re.findall('Ma[0-3A-B]', element):
        print(element)
