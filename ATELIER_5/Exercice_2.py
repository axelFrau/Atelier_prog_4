"""
Exercice 2 de l'atelier 5 : Mélange des éléments d’une liste

file       = "Exercice_2.py"
author     = "Frau Axel"
credits    = ["Frau Axel"]
data       = 21/09/2020
version    = "1.0"
"""

import random


def mix_list(l: list):
    """ Fonction qui prend en paramètre une liste ordonée et renvoi la même liste mais dans le désordre"""
    l_bis = []
    l_bis = l[:] # Comme la liste l est mutable on append dans une nouvelle liste chacune de ses valeurs.
    length = len(l_bis)
    for i in range(length):  # J'intervertis chaque valeur avec un autre aléatoire a chaque tour
        tempo = l_bis[i]
        rand_int = random.randint(0, length - 1)
        l_bis[i] = l_bis[rand_int]
        l_bis[rand_int] = tempo
    if l_bis == l:  # Dans le cas où de façon aléatoire elle serais revenue a son point de départ on relance la fonction
        mix_list(l)
    else:
        return l_bis  # sinon on return la liste mélangée


print(mix_list([1, 2, 3, 4, 5, 6, 7]))
