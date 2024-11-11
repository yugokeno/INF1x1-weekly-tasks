import math

def depasse(A):
    n = 1
    while math.factorial(n) < A:
        n += 1
    return n

if __name__=="__main__": # NE PAS SUPPRIMER CETTE LIGNE
    # Votre programme principal ne sera pas évalué.
    # Utilisez-le pour tester votre programme en faisant
    # les appels de votre choix.
    # Respectez bien ce niveau d'identation.
    print(depasse(120))  # Output: 5
    print(depasse(20))   
    print("Debut du prog. principal")