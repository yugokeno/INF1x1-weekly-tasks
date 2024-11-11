
def somme(n):
    if(n < 0): return 0
    return n * (n + 1) // 2

def somme_impairs(n): 
    if(n < 0): return 0
    return n * n

def somme_carres(n): 
    if(n < 0): return 0
    return n * (n + 1) * (2 * n + 1) // 6

if __name__=="__main__": # NE PAS SUPPRIMER CETTE LIGNE
    # Votre programme principal ne sera pas évalué.
    # Utilisez-le pour tester votre programme en faisant
    # les appels de votre choix.
    # Respectez bien ce niveau d'identation.
    print("Debut du prog. principal")
    n = 5
    print("Somme des", n, "premiers entiers :", somme(n))
    print("Somme des", n, "premiers entiers impairs :", somme_impairs(n))
    print("Somme des", n, "premiers carrés :", somme_carres(n)) 
