def factorielle(n):
    if n == 0 or n == 1:
        return 1
    resultat = 1
    for i in range(2, n + 1):
        resultat *= i
    return resultat

def coeff_binomial(n, k):
    if k > n:
        return 0
    return factorielle(n) // (factorielle(k) * factorielle(n - k))

def triangle_pascal(nb_lignes):
    for n in range(nb_lignes):
        ligne = []
        for k in range(n + 1):
            ligne.append(coeff_binomial(n, k))
        print(" ".join(map(str, ligne)))

# Exemples d'utilisation       # Affiche le triangle de Pascal avec 6 lignes


        
        
if __name__=="__main__": # NE PAS SUPPRIMER CETTE LIGNE 
    print(factorielle(5))        # Renvoie 120
    print(coeff_binomial(5, 2))  # Renvoie 10
    triangle_pascal(6)    
    # Votre programme principal ne sera pas évalué.
    # Utilisez-le pour tester votre programme en faisant
    # les appels de votre choix.
    # Respectez bien ce niveau d'identation.
    print("Debut du prog. principal")