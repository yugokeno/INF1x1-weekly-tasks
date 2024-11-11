def maximum(a, b):
    return a if a > b else b

def maximum3(a, b, c):
    return maximum(maximum(a, b), c)

def maximum3_input():
    a = float(input("Entrez le premier nombre : "))
    b = float(input("Entrez le deuxième nombre : "))
    c = float(input("Entrez le troisième nombre : "))
    
    return maximum3(a, b, c)

if __name__=="__main__": # NE PAS SUPPRIMER CETTE LIGNE
    # Votre programme principal ne sera pas évalué.
    # Utilisez-le pour tester votre programme en faisant
    # les appels de votre choix.
    # Respectez bien ce niveau d'identation.
    print("Debut du prog. principal")
    result = maximum3_input()
    print(f"Le plus grand des trois nombres est : {result}")
