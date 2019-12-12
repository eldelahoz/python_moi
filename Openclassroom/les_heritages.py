class Persone:

    def __init__(self, nom):
        self.nom = nom
        self.prenom = "DelaHoz"

    def __str__(self):
        return f"{self.prenom} {self.nom}"


class AgentSpecial(Persone):

    def __init__(self, nom, matricule):
        Persone.__init__(self, nom)
        self.matricule = matricule

    def __str__(self):
        return f"Agent {self.nom}, matricule {self.matricule}"

    # Petite précision
    def __setattr__(self, key, value):
        """Méthode appelée quand on fait objet.attribut = valeur"""
        print(f"Attention, on modifie l'attribut {key}")
        object.__setattr__(self, key, value)


agent = AgentSpecial("Andres", 1515155)
print(agent)
print(agent.nom)
print(agent.prenom, "\n")
# agent.nom = "David"

print("---->Deux fonctions très pratiques")
# issubclass et isinstance
print(issubclass(AgentSpecial, Persone))  # AgentSpecial hérite de Personne
print(issubclass(AgentSpecial, object))
print(issubclass(Persone, object))
print(issubclass(Persone, AgentSpecial))  # Personne n'hérite pas d'AgentSpecial

# isistance
print(isinstance(agent, AgentSpecial))  # Agent est une instance d'AgentSpecial
print(isinstance(agent, Persone), "\n")  # Agent est une instance de Personne

print("-------------L'héritage multiple-----------")


class ObjetPourSAsseoir:
    def __init__(self, nom):
        self.nom = nom

    def Sasseoir(self):
        print("Vous vous êtes assis")


class ObjetPourDormir:
    def __init__(self, nom):
        self.nom = nom

    def Dormir(self):
        print('S\'est endormi')


class MaClasseHeritee(ObjetPourSAsseoir, ObjetPourDormir):
    def __init__(self, nom):
        object.__init__(self)
        self.nom = nom


Fauteuil = ObjetPourSAsseoir("Fauteil")
Fauteuil.Sasseoir()
Lit = ObjetPourDormir("Lit")
Lit.Dormir()
Canape = MaClasseHeritee("Canape")
Canape.Sasseoir()
print("\n")
print("-------------Retour sur les exceptions-----------")


class MonException(Exception):
    """Exception levée dans un certain contexte... qui reste à définir"""

    def __init__(self, message):
        """On se contente de stocker la message d'erreur"""
        self.message = message

    def __str__(self):
        """On renvoie le message"""
        return self.message


raise MonException("OUPS... j'ai tout cassé")
