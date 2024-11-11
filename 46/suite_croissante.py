
def est_croissante(l):
    return all(l[i] <= l[i + 1] for i in range(len(l) - 1))

def est_decroissante(l):
    return all(l[i] >= l[i + 1] for i in range(len(l) - 1))

def est_en_desordre(l):
    return not (est_croissante(l) or est_decroissante(l))
        
if __name__=="__main__": # NE PAS SUPPRIMER CETTE LIGNE
    # Votre programme principal ne sera pas évalué.
    # Utilisez-le pour tester votre programme en faisant
    # les appels de votre choix.
    # Respectez bien ce niveau d'identation.
    print("Debut du prog. principal")
