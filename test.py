import math
input()
T=[int(s) for s in input().split()]
print(T and sorted(sorted(T, reverse=True), key=abs)[0] or 0)

"""n = int(input())  # the number of temperatures to analyse
if n == 0:
    print("0")
else:
    list_temps = []
    cont = 1
    Btemps = 5527
    for i in input().split():
        # t: a temperature expressed as an integer ranging from -273 to 5526
        list_temps.append(int(i))
        for temps in list_temps:
            if temps == 0:
                print(temps)
                break
            else:
                if abs(temps) < abs(int(Btemps)):
                    Btemps = temps
                if abs(temps) == abs(int(Btemps)):
                    if temps > Btemps:
                        Btemps = temps

            cont += 1
    print(Btemps)

"""
"""
n = int(input("Entrez le nombres de temperature à analise: "))
list_temperature = []
for i in input().split():
    list_temperature.append(i)

print(min(list_temperature))
print()
"""  # 1
"""n = int(input("Entrez le nombres de temperature à analise: "))
contador = 0
list_temperature = []
hoz = input("Entrez la liste de nombres: ")
x = str(hoz).split()
print(x)
print(min(x))
print("\n" + max(x))
"""
# 2
"""
    
if n == len(x):
    print(True)
else:
    print(f"Vous n'avez pas entre {n} nombres, ecrives une nouvelle fois les nombres:")
    x = str(hoz).split()

for i in input().split():
    # t: a temperature expressed as an integer ranging from -273 to 5526
    t = int(i)
"""
# 3
"""
n = int(input())
conteur = 0
zero_proche = []
for i in input().split():
    if 0 <= n < 1000:
        zero_proche.insert(conteur, int(i))

    conteur += 1

print(min((abs(x), x) for x in zero_proche)[1])

for x in zero_proche:
    print(min((abs(x)), x))

"""
