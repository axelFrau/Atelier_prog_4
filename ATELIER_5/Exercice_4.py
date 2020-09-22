"""
Exercice 4 de l'atelier 5 : Choix aléatoire de plusieursélémentsdans une liste

file       = "Exercice_4.py"
author     = "Frau Axel"
credits    = ["Frau Axel"]
data       = 21/09/2020
version    = "1.0"
"""

import random


def extract_elements_list(l: list, nbr_of_elements: int) -> list:
    """ fonction qui récupère aléatoirement le nombre d'élément demandé en paramètre dans la liste 'l' """
    list_to_return = []
    rand_int = -1
    length = len(l)
    cpt = 0
    while cpt < nbr_of_elements:
        last_rand = rand_int
        rand_int = random.randint(0, length - 1)
        if rand_int != last_rand:  # Vérification que l'ont renvoi deux fois le même element
            list_to_return.append(l[rand_int])
            cpt += 1
        else:
            pass
    return list_to_return


print(extract_elements_list([1, "list", 2, (1, 2, 3)], 3))
