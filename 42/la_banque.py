
def capital(nb_annees, capital_debut):
    for _ in range(nb_annees):
        capital_debut = capital_debut * 1.05 - 11
    return capital_debut


def gagne_argent(nb_annees, capital_debut):
    return capital(nb_annees, capital_debut) >= capital_debut


def capital_debut_min(nb_annees):
    capital_debut = 0
    while True:
        capital_final = capital(nb_annees, capital_debut)
        if capital_final >= capital_debut:
            return capital_debut
        capital_debut += 1


if __name__ == "__main__":
    nb_annees = 7
    capital_initial = 220

    print("Capital après", nb_annees, "années :", capital(nb_annees, capital_initial))

    print("Gagne de l'argent :", gagne_argent(nb_annees, capital_initial))

    print("Capital de début minimum pour", nb_annees, "années :", capital_debut_min(nb_annees)) 
    print("Debut du prog. principal")