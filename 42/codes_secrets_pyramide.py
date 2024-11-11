
def est_premier(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def sphinx_aime(n):
    return est_premier(n) and est_premier(n + 2)

def code_hall(nombre_prefere):
    while not sphinx_aime(nombre_prefere):
        nombre_prefere += 1
    return nombre_prefere

def est_puissance2(n):
    return (n > 0) and (n & (n - 1)) == 0

def osiris_aime(n):
    return est_puissance2(n + 1) and n % 5 == 3

def code_tresor(nombre_prefere):
    while not osiris_aime(nombre_prefere):
        nombre_prefere += 1
    return nombre_prefere









        
        
if __name__=="__main__": # NE PAS SUPPRIMER CETTE LIGNE
    # Votre programme principal ne sera pas évalué.
    # Utilisez-le pour tester votre programme en faisant
    # les appels de votre choix.
    # Respectez bien ce niveau d'identation.
    print("Debut du prog. principal")
    # Vos tests ici
    print("Code secret du hall pour le nombre préféré 15 :", code_hall(15))
    print("Code secret de la salle du trésor pour le nombre préféré 20 :", code_tresor(20))
    # Fin de vos tests
    # Ci-dessous: programme qui simule votre entree dans la pyramide
    # Vous devez juste appuyer sur Entree lorsque l'on vous le demande.
    import pyramide
    pyramide.entre() # Vous pouvez commenter cette ligne si vous le voulez.
   

