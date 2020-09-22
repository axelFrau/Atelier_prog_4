"""
Exercice 3 de l'atelier 5 : Choix aléatoire d'un élément dans une liste

file       = "Exercice_3.py"
author     = "Frau Axel"
credits    = ["Frau Axel"]
data       = 21/09/2020
version    = "1.0"
"""

import random


def choose_element_list(l: list):
    """ fonction qui choisit aléatoirement un élément de la liste 'l' et le return"""
    length = len(l)
    rand_int = random.randint(0, length - 1)
    element = l[rand_int]
    return element


print(choose_element_list(['liste', 1, 2]))
