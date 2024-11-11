def lundi(mot):
    return f"{mot} {mot}"

def mardi(mot):
    if len(mot) % 2 == 0:
        return '-'.join([mot] * 6)
    else:
        return ','.join([mot] * 3)

def mercredi(mot):
    return "impair" if len(mot) % 2 != 0 else mot

def jeudi(mot):
    repetitions = len(mot) % 3
    return mot * repetitions

def vendredi(mot):
    return mot

def transforme(mot, num_jour):
    if num_jour == 1:
        return lundi(mot)
    elif num_jour == 2:
        return mardi(mot)
    elif num_jour == 3:
        return mercredi(mot)
    elif num_jour == 4:
        return jeudi(mot)
    elif num_jour == 5:
        return vendredi(mot)
    else:
        return "Pas de transformation les week-ends !"
        
if __name__=="__main__": # NE PAS SUPPRIMER CETTE LIGNE
    # Votre programme principal ne sera pas évalué.
    # Utilisez-le pour tester votre programme en faisant
    # les appels de votre choix.
    # Respectez bien ce niveau d'identation.
    print("Debut du prog. principal")
    print("Lundi :", transforme("bonjour", 1))
    print("Mardi (mot pair) :", transforme("test", 2))
    print("Mardi (mot impair) :", transforme("python", 2))
    print("Mercredi :", transforme("code", 3))
    print("Jeudi :", transforme("comment", 4))
    print("Vendredi :", transforme("journal", 5))
    print("Samedi :", transforme("weekend", 6))