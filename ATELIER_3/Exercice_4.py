"""
Exercice 4 de l'atelier 3 : fonctions - histogramme
file       = "Exercice_4.py"
author     = "Frau Axel & Jean-François Giammari"
credits    = ["Frau Axel","Jean-François Giammari"]
version    = "1.0"
"""

from Exercice_1 import val_max
import matplotlib.pyplot as plt


def histo(F_list: list, display_console: bool = False, display_gui: bool = False) -> list:
    """
    Transform if a list representing a function in a  histogram
    Keyword argument:
    F_list -- List of number
    display
    return a histogram list
    """
    MAXVALEUR = len(F_list)
    H_list = []
    for i in range(MAXVALEUR):
        H_list.append(F_list.count(i))

    if display_console:
        afficheHisto(H_list)

    if display_gui:
        afficheHistoGUI(H_list)
    return H_list


def afficheHisto(H_list: list):
    """
    Display on console an histogram
    Keyword argument:
    H_list -- List of number to display (histogram)
    """
    print("\n\nHISTOGRAMME :")
    MAX0CC = val_max(H_list)
    length = len(H_list)
    for i in range(MAX0CC, 0, -1):
        for e in H_list:
            if e > 0 and e >= i:
                print("  # ", end="")
            else:
                print("    ", end="")
        print("")

    for i in range(length):
        print("|---", end="")
    print("|")

    for i in range(length):
        print("  " + str(i) + " ", end="")


def afficheHistoGUI(H_list: list):
    """
    Display on console an histogram
    Keyword argument:
    H_list -- List of number to display (histogram)
    """

    plt.hist(H_list,align="mid", facecolor='blue', alpha=0.7,histtype="bar")
    plt.axis([0, len(H_list), 0, val_max((H_list))])
    plt.grid(True)
    plt.show()


def est_injective(F_list: list) -> bool:
    """
    Define if a list representing a function is injective
    Keyword argument:
    F_list -- List of number
    return true if is injective
    """
    H_list = histo(F_list)
    length = len(H_list)

    is_injective = True
    i = 0
    while i < length and is_injective:
        if H_list[i] > 1:
            is_injective = False
        i += 1

    return is_injective


def est_surjective(F_list: list) -> bool:
    """
       Define if a list representing a function is surjective
    Keyword argument:
    F_list -- List of number
    return true if is surjective
    """
    H_list = histo(F_list)
    length = len(H_list)

    is_surjective = True
    i = 0
    while i < length and is_surjective:
        if H_list[i] < 1:
            is_surjective = False
        i += 1

    return is_surjective


def est_bijective(F_list: list) -> bool:
    """
       Define if a list representing a function is bijective
    Keyword argument:
    F_list -- List of number
    return true if is bijective
    """
    is_bijective = False
    if est_surjective(F_list) and est_injective((F_list)):
        is_bijective = True
    return is_bijective


def test_exercice4():
    """
    Test for exercice 4
    """
    print("\nTest pour histo [0, 1, 1, 0, 1, 2, 2, 0] :", histo([6, 5, 6, 8, 4, 2, 1, 5], True, True))
    print("\nTest pour Injective True :", est_injective([3, 0, 6, 7, 4, 2, 1, 5]))
    print("\nTest pour Injective False :", est_injective([6, 5, 6, 7, 4, 2, 1, 5]))
    print("\nTest pour Surjective True :", est_surjective([3, 0, 6, 7, 4, 2, 1, 5]))
    print("\nTest pour Surjective False :", est_surjective([6, 5, 6, 7, 4, 2, 1, 5]))
    print("\nTest pour Bijective True :", est_bijective([3, 0, 6, 7, 4, 2, 1, 5]))
    print("\nTest pour Bijective False :", est_bijective([6, 5, 6, 7, 4, 2, 1, 5]))


test_exercice4()
