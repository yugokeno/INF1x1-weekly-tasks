
import math

def valeur_abs(x):
    return x if x >= 0 else -x

def signe_different(x, y):
    if x == 0 or y == 0:
        return False
    return (x > 0 > y) or (x < 0 < y)

def f(x):
    return 3 * x ** 2 + 2 * x + 3

def nb_racines(a, b, c):
    delta = b ** 2 - 4 * a * c
    
    if delta < 0:
        return 0
    elif delta == 0:
        return 1
    else:
        return 2

# Programme principal
if __name__=='__main__': # NE PAS SUPPRIMER CETTE LIGNE
    # Votre programme principal ne sera pas évalué.
    # Utilisez-le pour tester votre programme en faisant
    # les appels de votre choix.
    # Respectez bien ce niveau d'identation.
    print("Debut du prog. principal")
    print(f"Valeur absolue de -5 : {valeur_abs(-5)}")
    print(f"Signe différent entre 5 et -3 : {signe_different(5, -3)}")
    print(f"Valeur de f(2) : {f(2)}")
    print(f"Nombre de racines pour le polynôme 1x² + 4x + 4 : {nb_racines(1, 4, 4)}")

