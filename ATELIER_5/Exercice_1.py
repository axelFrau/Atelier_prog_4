"""
Exercice 1 de l'atelier 5 : Génération de listes de nombres entiers aléatoires

file       = "Exercice_1.py"
author     = "Frau Axel"
credits    = ["Frau Axel"]
data       = 21/09/2020
version    = "1.0"
"""
import random


def gen_list_random_int(int_binf=0, int_bsup=10) -> list:
    """ Renvoi un liste de 10 nombres compris en la borne max et la borne min si aucune bornes n'est spécifié alors
    renvois 10 nombres entre 0 et 10 """
    int_nbr = []
    if int_binf == 0 and int_bsup == 10:  # Si il n'y a pas de paramètres on fixe la longueur de la liste final à 10
        longueur = 10
    else:  # Sinon on demande une longueur de liste aléatoire qui est au max égale à la différence de la borne
        # supérieur et la borne inférieur
        diff = int_bsup - int_binf
        longueur = random.randint(0, diff)
    for i in range(longueur):
        # print (longueur)
        rand_int = random.randint(int_binf, int_bsup)
        int_nbr.append(rand_int)
    return int_nbr

# print(gen_list_random_int())
# print("###############")
# print(gen_list_random_int(0,20))
