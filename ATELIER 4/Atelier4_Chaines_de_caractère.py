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

def outputStr(mot : str)->str:
    result = []
    longueur = len(mot)
    print(longueur)
    a  = "_"
    i = 0 
    while i <= longueur:
        i = i + 1
        result.extend(a)
    return result
# print(outputStr('bonjour'))
# print(outputStr('bon'))
# print(outputStr('maman'))
import random
def runGame():
    """"""
    C5 = "|-----]"
    C4 = "|  o"
    C3 = "|  T"
    C2 = "| / \ "
    C1 = "|______"
    iSizeDict = len(dSetWords)
    iRand = random.randint(1, iSizeDict)
    print(dSetWords[iRand])
    game_str = outputStr(dSetWords[iRand].values)
    print(game_str)
    i = 1
    while i <= 5:
        cUserChar = input("entrer une lettre: ")
        if cUserChar in dSetWords[iRand]:
            print("il vous reste " + 5-i +"coups")

dSetWords = {
    1:("paris",5),
    2:("londre",6),
    3:("madrid",6),
    4:("new-york",8),
    5:("berlin",6)
}
runGame()