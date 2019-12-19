import os

cartes = []
for i in os.listdir("."):
    if i.endswith(".txt"):
        cartes.append(i)

for x, value in enumerate(cartes):
    print(f"{x + 1} et {value[:-3]}")

# a_jouer = int(input("Quel carte tu veux?: "))
a_jouer = 1


class Carte:

    def __init__(self, ficher):
        self.labyrinthe = []
        with open(ficher, "r") as cartes:
            ma_carte_on = cartes.read()

        print(ma_carte_on)
        for a in ma_carte_on:
            self.labyrinthe.append(a)
        # print(labyrinthe)
        # labyrinthe[labyrinthe.index("X")] = " "
        # labyrinthe[52] = "X"
        # test = ""
        # for a in labyrinthe:
        #     test += a
        # print(test)

    def s(self, nombre):
        test = ""
        if self.labyrinthe[self.labyrinthe.index("X") + 11] == ".":
            print("Vous pouvez vous deplace")
            self.labyrinthe[self.labyrinthe.index("X") + 11] = "X"
            self.labyrinthe[self.labyrinthe.index("X")] = " "
        else:
            print(self.labyrinthe[self.labyrinthe.index("X") + 11])
            pass
        for a in self.labyrinthe:
            test += a
        print(test)


try:
    if cartes[a_jouer - 1]:
        print("La carte existe")
    labyrinthe_c = Carte(cartes[a_jouer - 1])

except IndexError:
    print(f"Le nombre {a_jouer} ne correspond pas à aucun labyrinthes.")

print("------Deuxime-------\n")
labyrinthe_c.s()
