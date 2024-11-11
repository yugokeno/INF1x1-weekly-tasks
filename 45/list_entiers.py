def LireListeEntiers():
    liste_entiers = []
    while True:
        try:
            nombre = int(input("Element?"))
            if nombre < 0:
                break
            liste_entiers.append(nombre)
        except ValueError:
            print("Please enter a valid integer.")
    return liste_entiers

def LireListeReelsBornes(bmin=0, bmax=100):
    liste_reels = []
    while True:
        try:
            nombre = float(input("Element?"))
            if nombre < bmin or nombre > bmax:
                break
            liste_reels.append(nombre)
        except ValueError:
            print("Please enter a valid real number.")
    return liste_reels

def MMSListe(liste):
    if not liste:
        return None, None, 0
    minimum = liste[0]
    maximum = liste[0]
    somme = 0
    for nombre in liste:
        if nombre < minimum:
            minimum = nombre
        if nombre > maximum:
            maximum = nombre
        somme += nombre
    return minimum, maximum, somme
        
if __name__=="__main__": # NE PAS SUPPRIMER CETTE LIGNE 
        # Main program
    # Reading and displaying the list of integers
    liste_entiers = LireListeEntiers()
    print(liste_entiers)
    
    # Reading the list of reals within bounds and calculating minimum, maximum, and sum
    liste_reels = LireListeReelsBornes()
    min_val, max_val, somme_val = MMSListe(liste_reels)
    print((min_val, max_val, somme_val))