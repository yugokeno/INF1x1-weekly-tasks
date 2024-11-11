def sommeDivPropre(n):
    if n <= 1:
        return 0
    somme = 0
    for i in range(1, n):
        if n % i == 0:
            somme += i
    return somme

def estParfait(n):
    return sommeDivPropre(n) == n

def parfaits_entre(binf=2, bsup=100):
    print(f"Nombres parfaits de [{binf},{bsup}]")
    parfaits = [n for n in range(binf, bsup + 1) if estParfait(n)]
    print(" ".join(map(str, parfaits)))


 


        
        
if __name__=="__main__": # NE PAS SUPPRIMER CETTE LIGNE
    # Votre programme principal ne sera pas évalué.
    # Utilisez-le pour tester votre programme en faisant
    # les appels de votre choix.
    # Respectez bien ce niveau d'identation.
    print("Debut du prog. principal")
