"""
Auteur : Marion calpena 
Date : 15/09/2020
Version : 1
Description : Codes de l'atelier 4 L3
"""
"""
Exercice 1 Manipulmation simples 
"""
def full_name(str_arg:str)->str:
    valeur = str_arg.split() #transforme en liste en enlevant les espace 
    print(valeur)
    valeur = valeur[0].upper() + " " + valeur[1].capitalize() #met en majuscule le premier mot, ajoute un espace, 
    #et met en majuscule la lettre du deuxieme mot 
    return valeur #retourne la valeur 
str_variable2test = "bisgambiglia paul"
#print(full_name(str_variable2test))

def is_mail(str_arg:str) -> (int, int):
    result = []
    if len(str_arg) > 64 or str_arg.startswith(".") or \
            str_arg.endswith(".") or str_arg.find("..") > -1:
        result.append((0, 1))
    if not '@' in str_arg: #erreur ici 
        result.append((0, 2))
    mail = str_arg.split('@')
    if len(mail[1]) < 3 or mail[1] == '' or '/' in mail[1] or '@' in mail[1] or '\\' in mail[1]:
        result.append((0, 3))
    if not '.' in mail[1]:
        result.append((0, 4))
    if len(result) == 0:
        result.append((1, 0))
    return result
str_variable1test = "bisgambiglia_paul@univ-corse.fr"
str_variable2test = "bisgambiglia_pauluniv-corse.fr"
str_variable3test = "bisgambiglia_paul@univ-corsePOINTfr"
str_variable4test = "@univ-corse.fr"
# print(is_mail(str_variable1test))
# print(is_mail(str_variable2test))
# print(is_mail(str_variable3test))
# print(is_mail(str_variable4test))

""" 
Exercice 2 mots croisé 
"""
def mots_Nlettre(L:list, n)->list:
    """une fonction qui prend une liste de mots (L) en argument et
    qui renvoie la liste des mots contenant exactement n lettres"""
    lst= []
    mot = 0
    for i in range(len(L)):
        mot = L[i]  
        cpt = 0
        for e in mot:
            cpt += 1
        if cpt == n:
            lst.append(mot)
    return lst
#print(mots_Nlettres(["mot", "mots"], 3))
#print(mots_Nlettres(["mot", "mer", "lol"], 3))
#print(mots_Nlettres([], 3))

def commence_par(mot, prefixe)->bool:
    """fonction commence_par(mot, prefixe) qui renvoie True si 
    l'argument mot commence par prefixe et False sinon"""
    return mot[:len(prefixe)] == prefixe
#print(commence_par("joli", "jol"))
#print(commence_par("envie", "jol"))

def finit_par(mot, suffixe)->bool:
    """fonction qui renvoie True si l'argument mot se termine par 
    suffixe et False sinon"""
    return mot[(len(mot)-len(suffixe)):len(mot)] == suffixe
#print(fini_par("joli", "oli"))
#print(fini_par("envie", "oli"))

def finissent_par(L:list, suffixe)->list:
    """fonction qui renvoie la liste des mots présents dans la liste L qui se terminent par suffixe"""
    list_return = []
    for e in L :
        if finit_par(e, suffixe) :
            list_return.append(e)
    return list_return
#print(finissent_par(["mot", "parcours", "ame", "mort"], "t"))

def commencent_par(L, prefixe):
    """fonction qui renvoie la liste des mots présents dans la liste L qui commencent par prefixe"""
    list_return = []
    for e in L :
        if commence_par(e, prefixe) :
            list_return.append(e)
    return list_return
#print(commencer_par(["mot","mots","legume","manguste","banane"],"m"))

def liste_mots(L:list, prefixe:str, suffixe:str, n:int)->list:
    """fonction liste_mots (L, prefixe, suffixe, n) qui renvoie la liste 
    des mots présents dans L qui commencent par prefixe, se terminent 
    par suffixe et contiennent exactement n lettres"""
    return commencent_par(finissent_par(mots_Nlettre(L, n),suffixe), prefixe)
#print(liste_mots(["mot","lol","mort","ok"],"m","t","2"))

def dictionnaire(fichier):
    """fonction qui admet en paramètre une chaine de caractères 
    représentant un nom de fichier de texte et renvoie la liste 
    des mots présents dans ce dictionnaire."""
    f=open(fichier,"r")
    c=f.readline()
    print("** Contenu du fichier **")
    while c!="" :
        print(c)
        c=f.readline()
    print("** fin **")
    f.close()
#print(dictionnaire("littre.txt"))

def dictionnaire2(fichier) :
    f=open(fichier,"r")
    c=f.readlines()
    f.close()
    return c
#dictionnaire2("littre.txt") 

"""
Exercice 3 Jeu du pendu 
"""
def placesLettres(char:str, mot:str)->list:
    Valeur = []
    if char in mot :
        for i in range(len(mot)):
            Valeur =+ 1
    else:
        Valeur = []
    return Valeur 
# print(placesLettres('b','bonjour'))
# print(placesLettres('a','bonjour'))
# print(placesLettres('m','maman'))

def outputStr(mot : str, lpos:list)->str:
    """Prend un mot et ajoute à 'str_output' aux emplacements indiqué dans 'l_pos' le '-' par la lettre dans le mot"""
    str_output = ''
    i = 0
    while i < len(mot) :
        if i in lpos :
            str_output += mot[i]
        else :
            str_output += '-'
        i += 1
    return str_output
# print(outputStr('bonjour'))
# print(outputStr('bon'))
# print(outputStr('maman'))
import random
def runGame():
    lst =["parisa","londres","madrid","berlin","new-york"]
    lst_len= len(lst)
    # iRand = random.randint(1, lst_len)
    iRand = 1
    errors_list = ["|______","|/ \ ","| T ","| O ","|---] "]
    # "|---] "
    # "| O "
    # "| T "
    # "|/ \ "
    # "|______"
    word_to_guess = outputStr(lst[iRand], [])
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
            print("Voici ce que vous avez jusque là : {}".format(word_to_guess))
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
"""
Exercice 4 - Aide scrabble
"""
def mot_correspond(mot:str, motif:str)->bool :
    """fonction qui renvoie True ou False suivant que la chaine 
    de caractère mot correspond, ou pas, à la chaine de caractères 
    motif donnée"""
    if len(mot) == len(motif) :
        for i in range(len(mot)) :
            if mot[i] != motif[i] and motif[i] != "." :
                return False
        return True
    else :
        return False
#mot_correspondant("tante","t..t.")
#mot_correspondant("cheval","c..v..l")
#mot_correspondant("cheval","c..v.l")

def presente(lettre:str, mot:str)->bool :
    for e in mot :
        if e == lettre :
            return True
    return False
#print(present("virgule","u"))
#print(present("virgule","y"))
#print(present("","u"))

def presente_while(lettre:str, mot:str)->bool :
    test = -1
    i = 0
    while i < len(mot) and test == -1 :
        if mot[i] == lettre :
            test = i
        i += 1
    return test

def presente_2(lettre:str, mot:str)->int : #faire un while
    for i in range(len(mot)) :
        if mot[i] == lettre :
            return i
    return -1

def presences(lettre:str, mot:str)->list :
    list_return = []
    for i in range(len(mot)) :
        if mot[i] == lettre :
            list_return.append(i)
    return list_return

def mot_possible(mot:str, chaine:str)->bool :
    for e in mot :
        if not presente(e, chaine) :
            return False
        else :
            chaine = (chaine[:(chaine.index(e))]) + (chaine[chaine.index(e)+1:])
    return True

def mot_possible_2(mot:str, chaine:str)->bool :
    for e in mot :
        i = presente_2(e, chaine)
        if i == -1 :
            return False
        else :
            chaine = (chaine[:i]) + (chaine[i+1:])
    return True

def mot_possible_3(mot:str, chaine:str)->bool :
    for e in mot :
        index = presences(e, chaine)
        if index == [] :
            return False
        elif len(index) == 1 :
            chaine = (chaine[:index[0]]) + (chaine[index[0]+1:len(chaine)])
        else :
            for i in range(len(index)) :
                chaine = (chaine[:index[i]]) + (chaine[index[i]+1:])
    return True
"""
Exercice 5 - Vérification d'expressions arithmétiques
"""
def ouvrante(char:str)->bool :
    chars = ["(", "[", "{"]
    for e in chars :
        if e == char :
            return True
    return False


def fermante(char:str)->bool :
    chars = [")", "]", "}"]
    for e in chars :
        if e == char :
            return True
    return False

def renverse(char:str)->str :
    open_chars = ["(", "[", "{"]
    close_chars = [")", "]", "}"]
    if fermante(char) :
        for i in range(len(close_chars)) :
            if char == close_chars[i] :
                return open_chars[i]
    elif ouvrante(char) :
        for i in range(len(open_chars)) :
            if char == open_chars[i] :
                return close_chars[i]
    else :
        return char

def operateur(char:str)->bool :
    if char == '*' or char == '+' :
        return True
    else :
        return False

def nombre(char:str)->bool :
    return char.isdigit()

def caractere_valide(char:str)->bool :
    if (ouvrante(char) or fermante(char) or
        operateur(char) or nombre(char) or char == ' ') :
            return True
    else :
        return False

def verif_parentheses(expression:str)->bool :
    P = []
    for e in expression :
        if caractere_valide(e) :
            if ouvrante(e) or fermante(e) :
                P.append(e)
        else :
            return False
    for _ in range(len(P)//2) :
        if P[0] == renverse(P[-1]) :
            P.pop(0)
            P.pop(-1)
    if P == [] :
        return True
    else :
        return False

##print(renverse('['))
##print(nombre('5'))
##print(nombre('f'))
# print(verif_parentheses("(()()"))