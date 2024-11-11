
def liste_decroissante(n):
    return list(range(n, -1, -1))

def multiples(m, longueur):
    return [m * i for i in range(longueur)]

def pairs(longueur):
    return [2 * i for i in range(longueur)]

if __name__=="__main__": # NE PAS SUPPRIMER CETTE LIGNE
    # Votre programme principal ne sera pas évalué.
    # Utilisez-le pour tester votre programme en faisant
    # les appels de votre choix.
    # Respectez bien ce niveau d'identation.
    print("Debut du prog. principal")
