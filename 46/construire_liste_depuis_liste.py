
def decale(l, d):
    return [x + d for x in l]

def intercale_zeros(l):
    result = []
    for x in l:
        result.extend([x, 0])
    return result

def supprime(l, elem):
    return [x for x in l if x != elem]

def insere_milieu(l, elem):
    mid = len(l) // 2
    if len(l) % 2 == 0:
        return l[:mid] + [elem] + l[mid:]
    else:
        return l[:mid] + [elem] + l[mid:mid+1] + [elem] + l[mid+1:]

def decoupe(l, seuil):
    lower_or_equal = [x for x in l if x <= seuil]
    greater = [x for x in l if x > seuil]
    return lower_or_equal, greater

if __name__=="__main__": # NE PAS SUPPRIMER CETTE LIGNE
    # Votre programme principal ne sera pas évalué.
    # Utilisez-le pour tester votre programme en faisant
    # les appels de votre choix.
    # Respectez bien ce niveau d'identation.
    print("Debut du prog. principal")
