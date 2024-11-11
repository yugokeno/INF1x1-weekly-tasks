
def commence_par(lettre, mot):
    return mot[0] == lettre

def contient_voyelle(mot):
    voyelles = "aeiouy"
    return any(char in voyelles for char in mot)

def derniere_consonne(mot):
    voyelles = "aeiouy"
    for i in range(len(mot) - 1, -1, -1):
        if mot[i] not in voyelles:
            return i, mot[i]
    return None, None

def double_consonne(mot):
    voyelles = "aeiouy"
    for i in range(len(mot) - 1):
        if mot[i] == mot[i + 1] and mot[i] not in voyelles:
            return True, mot[i]
    return False, None

def envers(li):
    return li[::-1]

def palindrome(mot):
    return mot == mot[::-1]

def mot_autorise(mot, liste_interdite):
    return mot not in liste_interdite

if __name__=="__main__": # NE PAS SUPPRIMER CETTE LIGNE
    # Votre programme principal ne sera pas évalué.
    # Utilisez-le pour tester votre programme en faisant
    # les appels de votre choix.
    # Respectez bien ce niveau d'identation.
    print("Debut du prog. principal")
    print(commence_par('h', 'hello'))
    print(commence_par('e', 'roue'))
    print(contient_voyelle('hello')) 
    print(contient_voyelle('rhythm'))
    print(derniere_consonne('arrivee'))
    print(double_consonne('arrivee'))
    print(double_consonne('bonbon'))
    print(envers(['a', 'b', 'c', 'd']))
    print(palindrome('ici'))         
    print(palindrome('aller'))      
    print(mot_autorise('fric', ['sous', 'fric', 'thune', 'ble']))
    print(mot_autorise('argent', ['sous', 'fric', 'thune', 'ble']))
    mot="bonjour"
    test=list(mot)
    print(test)