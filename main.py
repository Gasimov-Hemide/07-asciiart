#### Imports et définition des variables globales
"""
Retourne la liste de tuples encodant une chaîne de caractères passée en argument

Modules :
    artcode_i(s)
    artcode_r(s)
"""
# Mandatory for the recursive solution to work on large inputs
import sys
sys.setrecursionlimit(2000)


#### Fonctions secondaires


def artcode_i(s):
    """
    retourne la liste de tuples encodant une chaîne de caractères passée en argument selon
    un algorithme itératif

    Args:
        s (str): la chaîne de caractères à encoder

    Returns:
        list: la liste des tuples (caractère, nombre d'occurences)
    """

    # votre code ici

    if not s:
        return []

    c = [s[0]]
    o = [1]
    n = len(s)

    for k in range(1, n):
        if s[k] == s[k-1]:
            o[-1] += 1
        else:
            c.append(s[k])
            o.append(1)

    return list(zip(c, o))


def artcode_r(s):
    """
    retourne la liste de tuples encodant une chaîne de caractères passée en argument 
    selon un algorithme récursif

    Args:
        s (str): la chaîne de caractères à encoder

    Returns:
        list: la liste des tuples (caractère, nombre d'occurences)
    """

    # votre code ici

    # cas de base
    if not s:
        return []

    # recherche nombre de caractères identiques au premier
    premier_caractere = s[0]
    longueur_segment = 0

    for caractere in s:
        if caractere == premier_caractere:
            longueur_segment += 1
        else:
            break

    premier_tuple = (premier_caractere, longueur_segment)

    # appel récursif
    return [premier_tuple] + artcode_r(s[longueur_segment:])

#### Fonction principale


def main():
    """
    Fait appel aux fonctions artcode_i(s) et artcode_r(s) pour vérifier leur bon fonctionnement
    """
    print(artcode_i('MMMMaaacXolloMM'))
    print(artcode_r('MMMMaaacXolloMM'))

if __name__ == "__main__":
    main()
