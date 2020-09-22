"""
Auteur : Marion calpena 
Date : 15/09/2020
Version : 1
Description : Codes de l'atelier 4 L3
"""
"""
Partie 1 - Exercice essentiel
"""
"""
Exercice 1 - Génération de listes dde nombres entiers aléatoires
"""
import random 
def gen_list_random_int(int_nbr,int_binf,int_bsup):
    list = []
    i = 0
    while i <= int_nbr:
        list.append(random.randint(int_binf,int_bsup))
        i = i + 1
    i = 0
    if list == []:
        while i <= 10:
            list[i] = random()
            i = i + 1
    return list 
# print(gen_list_random_int(9,15,20))
# print(gen_list_random_int(3,5,30))
# print(gen_list_random_int(18,100,200))

"""
Exercice 2 - Mélange des élément d'une liste 
"""
def mix_list(list_to_mix:list):
    list = []
    longueur = len(list_to_mix)
    indice = random.randint(0,longueur)
    for i in range(longueur):
        list[indice].append(list_to_mix[i])
    return list
a = [1,2,3,4,5,6,7,8,9]
b = [10,11,12,13,14,15,16,17,18,19] 
print(mix_list(a))
print(mix_list(b))