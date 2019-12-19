# -*-coding:Utf-8 -*

"""Ce module contient la classe Labyrinthe."""


class Labyrinthe:
    """Classe représentant un labyrinthe."""

    def __init__(self, robot, grille, obstacles):
        self.robot = robot
        self.grille = grille
        # ...

    def __repr__(self):
        labyrinthe = ""
        for i, value in enumerate(self.grille):
            print(f"{i} et {value}")
            pass
        return f"{self.grille}"
    


