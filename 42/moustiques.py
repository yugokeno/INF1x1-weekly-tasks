
import math

def f(x):
    return math.floor(1.09 * x - 200)

def nb_moustiques(nb_debut, annee_voulue):
    population = nb_debut
    for _ in range(2017, annee_voulue):
        population = f(population)
    return population

def annee_atteindra(seuil, nb_debut):
    population = nb_debut
    annee = 2017
    while population < seuil:
        population = f(population)
        annee += 1
    return annee

def main():
    estimation_marc = int(input("Estimation de Marc (entre 8000 et 12000): "))
    estimation_alice = int(input("Estimation d'Alice (entre 8000 et 12000): "))
    
    annee_voulue = int(input("Entrez l'année souhaitée: "))
    
    population_marc = nb_moustiques(estimation_marc, annee_voulue)
    population_alice = nb_moustiques(estimation_alice, annee_voulue)
    
    print(f"Estimation de Marc pour l'année {annee_voulue}: {population_marc} moustiques")
    print(f"Estimation d'Alice pour l'année {annee_voulue}: {population_alice} moustiques")
    
    seuil = int(input("Entrez un seuil de moustiques: "))
    
    annee_marc = annee_atteindra(seuil, estimation_marc)
    annee_alice = annee_atteindra(seuil, estimation_alice)
    
    print(f"Marc atteindra le seuil de {seuil} moustiques en l'année {annee_marc}.")
    print(f"Alice atteindra le seuil de {seuil} moustiques en l'année {annee_alice}.")

if __name__=="__main__": # NE PAS SUPPRIMER CETTE LIGNE
    # Votre programme principal ne sera pas évalué.
    # Utilisez-le pour tester votre programme en faisant
    # les appels de votre choix.
    # Respectez bien ce niveau d'identation.
    print("Debut du prog. principal")
    main()