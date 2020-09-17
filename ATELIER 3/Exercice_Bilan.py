"""
Exercice Bilan de l'atelier 3 : Calculs, Comptage, Maximum, Fonction Entières, Structure itératives

file       = "Exercice_1.py"
author     = "Frau Axel"
credits    = ["Frau Axel"]
data       = 17/09/2020
version    = "1.0"
"""

def fill_list (b_inf:int,b_sup:int,max_len:int) -> list :
    """ Permet de rentrer des nombres dans une listes tant que le chiffre est compris entre b_inf et b_sup avec un nombre max de nombre qui a pour valeur max_len
    J'ai du séparer le fonctionnement de la fonction en deux pour verifier si l'appel fait à un instant T est un test ou une utilisation d'un utilisateur en vérifiant si la liste
    envoyé est vide"""
    i = 0
    empty_list = False
    res = []
    while i < max_len and not empty_list :
        try :
            entered_nb = int(input('Veuillez rentrer le nombre numéro {} : '.format(i+1)))
            if(b_inf > entered_nb or b_sup < entered_nb ) :
                empty_list = True #Stop la boucle quand une valeur en dehors des bornes est rentrée
            else :
                res.append(entered_nb) #On stock dans la liste le nombre entrée
                i += 1 #On incrémente le compteur i de 1
        except ValueError:  # C'est ici la gestion du cas où un autre caractère est rentrer qui ne serrais pas un chiffre ou un nombre.
            print("Il y eu une erreur recommencer s'il vous plait")
            pass
    return res


# Tests :             #1         #2      #3        #4         #5        #6       #7
# Bornes rentré = [0,10,9], [0,10,9],[0,10,9], [0,10,9], [0,10,9], [0,10,9], [0,20,9]
# Nombre à rentrer = [],[-1, 1 ,39,89],[1, 2,11],[1,2,3,4,5,6,7,8,9], [10000, 1,2,3,4,5,6,7,8], [1,2,-1], [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
# Resultat attendu = [], [], [1, 2], [1,2,3,4,5,6,7,8,9], [1,2], [1,2,3,4,5,6,7,8,9]


# def test_unitaire():
#     """ Cette fonciton nous permet de tester les différents cas possibles pour la fonction fill_list(), en faisant des appels successifs avec des paramètres différent
#     """
    
#     success = True
#     for i in range (0, len(bornes_test)) :
#         print(i)
#         b_inf = bornes_test[i][0]
#         b_sup = bornes_test[i][1]
#         max_len = bornes_test[i][2]
#         if fill_list(b_inf, b_sup, max_len, nb_test[i]) == res[i]:
#             print(">",end="")
#         else : 
#             print("X",end="")
#             success = False
    
#     if success == True :
#         print(" TEST IS SUCCESSFUL")
#     else :
#         print(" TEST FAILED")

# test_unitaire()
print(fill_list(0,10,9))