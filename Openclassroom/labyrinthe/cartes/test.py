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
        self.obstacle = []
        with open(ficher, "r") as cartes:
            self.ma_carte_on = cartes.read()
        for a in self.ma_carte_on:
            if a == "O":
                self.obstacle.append(a)
            self.labyrinthe.append(a)
        # print(labyrinthe)
        # labyrinthe[labyrinthe.index("X")] = " "
        # labyrinthe[52] = "X"
        # test = ""
        # for a in labyrinthe:
        #     test += a
        # print(test)

    def __repr__(self):
        return self.ma_carte_on

    def Enregistre(self, value):
        with open("partie_test.txt", "w") as carte_ouverte:
            carte_ouverte.write(value)

    def e(self, nombre=1):
        for a in range(0, nombre):
            viste_labyrinthe = ""
            position = self.labyrinthe.index("X")
            if self.labyrinthe[position + 1] in self.obstacle:
                print("Désole mais vous ne pouvez pas vous déplacer par là")
                break
            else:
                self.labyrinthe[position + 1] = "X"
                self.labyrinthe[position] = " "
            # print(self.labyrinthe[position + 1] in self.obstacle)
            for a in self.labyrinthe:
                viste_labyrinthe += a

            print(viste_labyrinthe, "\n")
        return self.labyrinthe

    def o(self):
        viste_labyrinthe = ""
        position = self.labyrinthe.index("X")
        if self.labyrinthe[position - 1] in self.obstacle:
            print("Désole mais vous ne pouvez pas vous déplacer par là")
        else:
            self.labyrinthe[position - 1] = "X"
            self.labyrinthe[position] = " "
        for a in self.labyrinthe:
            viste_labyrinthe += a
        print(viste_labyrinthe)
        return self.labyrinthe


jouer = False
# Pour vérifier si le nombre que vous êtes entré est dans la liste
try:
    if cartes[a_jouer - 1]:
        print("La carte existe")

        jouer = True

except IndexError:
    print(f"Le nombre {a_jouer} ne correspond pas à aucun labyrinthes.")

if jouer:
    labyrinthe_c = Carte(cartes[a_jouer - 1])
    print(labyrinthe_c)


def function_mouvement(mouvement):
    if len(mouvement) > 1:
        if mouvement[1] > "0":
            return "labyrinthe_c." + mouvement + "(" + mouvement[1] + ")"


function_mouvement(input("Saissisez"))
# while jouer:
#
#     b_jouer = input("Saissisez: ")
#     if len(b_jouer) > 1:
#         print(len(b_jouer))
#         if b_jouer[1] > "0":
#             labyrinthe_c.e(int(b_jouer[1]))
#
#     if b_jouer.lower() == "q":
#         jouer = False
#     elif b_jouer.lower() == "e":
#         labyrinthe_c.e()
#     elif b_jouer.lower() == "o":
#         labyrinthe_c.o()

print("------Deuxime-------\n")
