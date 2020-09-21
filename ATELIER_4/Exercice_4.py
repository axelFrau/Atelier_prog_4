"""
Exercice 4 de l'atelier 4 : Aide Scrabble

file       = "Exercice_4.py"
author     = "Frau Axel"
credits    = ["Frau Axel"]
data       = 17/09/2020
version    = "1.0"
"""

def mot_correspond(mot:str, motif:str)->bool :
    """Fonction qui renvoi un booléen en fonction de si le motif donnée et la chaine de caractère mot donnée correspondent ou non"""
    if len(mot) == len(motif) :
        for i in range(len(mot)) :
            if mot[i] != motif[i] and motif[i] != "." :
                res = False
        else :
            res = True 
    else :
        res = False
    return res
# print(mot_correspond("tarte","t..t."))
# print(mot_correspond("cheval","c..v..l"))

def presente(mot:str, lettre:str)->bool or int :
    """ Cette fonction renvoi l'indice de l'emplacement de la lettre donnée en paramètre dans la chaine de caractère 'mot' sinon elle renvoie -1 """
    res = -1
    lenght = len(mot)
    for i in range(lenght) :
        if mot[i] == lettre :
            res = i
    return res
# print(presente("virgule","u"))
# print(presente("virgule","z"))
# print(presente("","u"))


def mot_possible(mot:str, chaine:str)->bool :
    """ Fonction qui evalue en fonction de la chaine de lettres donnée si le mot donné en paramètre est possible d'être écrit ou non"""
    compteur = 0
    for e in mot :
        if presente(chaine, e) != -1 :
            compteur += 1
    if compteur == len(mot):
        res = True
    else : 
        res = False
    return res

print(mot_possible('lapin', 'aklipnd'))
