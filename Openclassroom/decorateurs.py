import time


# def mon_decorateur(fonction):
#     """Premier example de décorateur"""
#     print(f"Notre décorateur est appelé avec en paramètre la foction {fonction}")
#     return fonction
#
#
# @mon_decorateur
# def salut():
#     """Fonction modifiée par notre décorateur"""
#     print("Salut !")
#
#
# # Exemple équivalent, sans décorateur
# def fonction():
#     fonction = mon_decorateur(fonction)


def mon_deuxime_decorateur(fonction):
    """Notre décorateur: il va afficher un message avant l'appel de la
    fonction définie"""

    def foction_modifie():
        """Foction que l'on va renvoyer. Il s'agit en fait d'une version
        un peu modifiée de notre foction originellement définie. On se
        contente d'afficher un avertissement avant d'exécuter notre foction
        originellement définie"""

        print(f"Attention ! On appelle {fonction}")
        return fonction()

    return foction_modifie


@mon_deuxime_decorateur
def deuxime_salut():
    print("Deuxime salut!")


def obsolete(fonction):
    """Décorateur levant une exception pour noter que la fonction est obsolète"""

    def fonction_obsolete():
        raise RuntimeError(f"La foction {fonction} est obsolète!")

    return fonction_obsolete


deuxime_salut()

print(deuxime_salut, "\n")


# @obsolete
# def essais():
#     print("Je vais teste cette fonction")
# essais()

# def controler_temps(nb_secs):
#     """Contrôle le temps mis par une foction pour s'exécuter.
#     Si le temps d'exécutions est supériur à nb_secs, on affiche une alerte"""
#
#     def decorateur(fonction_a_executer):
#         """Notre décorateur. C'est lui qui est appelé directament LORS
#         DE LA DEFINITION de notre fonction (foction_a_executer)"""
#
#         def fonction_modifiee():
#             """Foction renvoyée par notre décorateur. Elle se carge
#             de calculer le temps mis par la fonction à s'exécuter"""
#
#             tps_avant = time.time()
#             valeur_renvoyee = fonction_a_executer()
#             tps_apres = time.time()
#             tps_execution = tps_apres - tps_avant
#             if tps_execution >= nb_secs:
#                 print(f"La foction {fonction_a_executer} a mis {round(tps_execution, 2)}")
#             return valeur_renvoyee
#
#         return fonction_modifiee
#
#     return decorateur
#
#
# @controler_temps(4)
# def attendre():
#     input("Appuyer sur enter...")
#
#
# attendre()


def controleur_temps_2(nb_sec):
    def decorateur(fonction_a_executer):
        def foction_modifiee(*parametres_non_nommes, **parametres_nommes):
            tps_avant = time.time()
            ret = fonction_a_executer(*parametres_non_nommes, **parametres_nommes)
            tps_apres = time.time()
            tps_execution = tps_apres - tps_avant
            if tps_execution >= nb_sec:
                print(f"La fonction {fonction_a_executer} a mis {round(tps_execution, 2)} pour s'exécuter")
            return ret

        return foction_modifiee

    return decorateur


@controleur_temps_2(3)
def attendre2(a, b):
    input(f"Apuuyer sur enter2...{a} + {b}")


# attendre2(10, 20)

print("\n")


# Des décorateurs s'appliquant aux définitions de classes
def decorateur_classe(classe):
    print(f"Définition de la classe {classe}")


@decorateur_classe
class Test:
    pass


print("\n")


def singleton(classe_definie):
    instance = {}

    def get_instance():
        if classe_definie not in instance:
            instance[classe_definie] = classe_definie()
        return instance[classe_definie]

    return get_instance


@singleton
class Test2:
    pass


a = Test2()
b = Test2()
print(a is b)


# Contrôler les types passés à notre fonction

def controler_type(type_un, type_deux):
    def decorateur(fonction_a_executer):
        def fonction_modifie(typeUn, typeDeux):
            rest = fonction_a_executer(typeUn, typeDeux)
            if type(typeUn) == type_un and type(typeDeux) == type_deux:
                print(f"C'est bien como type {type_un} et le deuxime type {type_deux}")
            else:
                raise TypeError(f"Vous avez tape mal le type {repr(type_un)}")
            return rest

        return fonction_modifie

    return decorateur


@controler_type(float, float)
def intervalle(base_inf, base_sup):
    print(base_inf + base_sup)


# intervalle(25, 3.5)


def controler_types2(*a_args, **a_kwargs):
    """On attend en paramètres du décorateur les types souhaités. On accepte
    une liste de paramètres indéterminés, étant donné que notre fonction
    définie pourra être appelée avec un nombre variable de paramètres et que
    chacun doit être contrôlé"""

    def decorateur(fonction_a_executer):
        """Notre décorateur. Il doit renvoyer fonction_modifiee"""

        def fonction_modifiee(*args, **kwargs):
            """Notre fonction modifiée. Elle se charge de contrôler
            les types qu'on lui passe en paramètres"""

            # La liste des paramètres attendus (a_args) doit être de même
            # Longueur que celle reçue (args)
            if len(a_args) != len(args):
                raise TypeError("le nombre d'arguments attendu n'est pas égal au nombre reçu")
            # On parcourt la liste des arguments reçus et non nommés
            for i, arg in enumerate(args):
                if a_args[i] is not type(args[i]):
                    raise TypeError("l'argument {0} n'est pas du type {1}".format(i, a_args[i]))

            # On parcourt à présent la liste des paramètres reçus et nommés
            for cle in kwargs:
                if cle not in a_kwargs:
                    raise TypeError("l'argument {0} n'a aucun type précisé".format(repr(cle)))
                if a_kwargs[cle] is not type(kwargs[cle]):
                    raise TypeError("l'argument {0} n'est pas de type {1}".format(repr(cle), a_kwargs[cle]))
            return fonction_a_executer(*args, **kwargs)

        return fonction_modifiee

    return decorateur


@controler_types2(int, float, hola=str)
def testtype(base, altura, text):
    print(f"La base {base}, la altura {altura}, {text}")


testtype(10, 2.5, hola="Je suis")
