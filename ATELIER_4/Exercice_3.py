"""
Exercice Bilan de l'atelier 3 : Calculs, Comptage, Maximum, Fonction Entières, Structure itératives

file       = "Exercice_1.py"
author     = "Frau Axel"
credits    = ["Frau Axel"]
data       = 17/09/2020
version    = "1.0"
"""

def places_lettre(ch:str, mot:str) -> list :
    """ retourne la ou les places d'un caractère dans une chaine de caractère"""
    res = []
    for i in range(len(mot)):
        if mot[i] == ch :
            res.append(i)
    return res 
# print(places_lettre('b','bonbour'))
# print(places_lettre('a','bonbour'))
# print(places_lettre('m','bonbour'))

def outputStr(mot:str, l_pos:list) -> str :
    """Prend un mot et ajoute à 'str_output' aux emplacements indiqué dans 'l_pos' le '-' par la lettre dans le mot"""
    str_output = ''
    i = 0
    while i < len(mot):
        print(i)
        if i in l_pos :
            str_output += mot[i]
        else :
            str_output += '-'
        i += 1
    return str_output
    pass

# print(outputStr("Bonjour",[0]))

def build_list(filename: str) -> list :
    # cwd = os.getcwd()
    # files = os.listdir(cwd)  # Get all the files in that directory
    # print("Files in %r: %s" % (cwd, files))
    file = open("ATELIER_4/" + filename + ".txt","r")
    liste = []
    chaine = ''
    data = file.readlines()
    print(data)
    for i in data : 
        chaine += i
        chaine.split("\t")
        liste.append(chaine)
    print(liste)
    # print(content)
    file.close()
    return ["liste","liste","liste","liste","liste"]

import random 
import os
def rungame() :
    lst = build_list("littre_smaller")
    lst_len= len(lst)
    iRand = random.randint(1, lst_len)
    errors_list = ["|______","|/ \ ","| T ","| O ","|---] "]
    # "|---] "
    # "| O "
    # "| T "
    # "|/ \ "
    # "|______"
    word_to_guess = outputStr(lst[iRand], [])
    print('le mot est : {}'.format(lst[iRand]))
    print("Voici le mot à trouver : {}".format(word_to_guess))
    l_pos = []
    errors = 0
    error_to_display = []
    letters_entered = []
    while word_to_guess != lst[iRand] and errors != 5:
        user_letter = input('Entrer une lettre : ')
        if user_letter in letters_entered :
            letters_entered.append(user_letter)
        else :
            letter_pos = places_lettre(user_letter, lst[iRand])
            if letter_pos == [] :
                print("La lettre entrée ne se trouve pas dans le mot : {}".format(word_to_guess))
                errors += 1
            else :
                for i in letter_pos :
                    l_pos.append(i)
                word_to_guess = outputStr(lst[iRand], l_pos)
            print("Voici ce que vous avez jusque là : {} mot à trouver : {}".format(word_to_guess,lst[iRand] ))
            if errors == 0 :
                print("Encore 5 erreurs autorisées ! faites attention ;)")
            else :
                for i in range(errors,0,-1) :
                    print("{} erreurs : ".format(i),errors_list[i - 1])
                    # if error_count == 5 :
                    #     print("C'est PERDU !!!!!!! le mot était : {}".format(lst[iRand]))
    if errors != 5 :
        print("C'est gagné !!")
    else :
        print("Quel dommage ! Tu as fais trop d'erreurs ! le mot était : {}".format(lst[iRand]))

                # if(errors == 1) :
                #     print("1 erreur : ",errors_list[0])
                # if(errors == 2) :
                #     print("2 erreurs : ",errors_list[1])
                #     print("1 erreur : ",errors_list[0])
                # if(errors == 3) :
                #     print("3 erreurs : ",errors_list[2])
                #     print("2 erreurs : ",errors_list[1])
                #     print("1 erreurs : ",errors_list[0])
                # if(errors == 4) :
                #     print("4 erreurs : ",errors_list[3])
                #     print("3 erreurs : ",errors_list[2])
                #     print("2 erreurs : ",errors_list[1])
                #     print("1 erreur : ",errors_list[0])
                # if(errors == 5) :
                #     print("5 erreurs : ",errors_list[4])
                #     print("4 erreurs : ",errors_list[3])
                #     print("3 erreurs : ",errors_list[2])
                #     print("2 erreurs : ",errors_list[1])
                #     print("1 erreur : ",errors_list[0])

rungame()