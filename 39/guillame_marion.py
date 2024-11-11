lancer_gestion = input("Lancement de la gestion des comptes? ").strip().lower()

if lancer_gestion == "non":
    print("OK. A bientot.")
elif lancer_gestion == "oui":
    guillaume_solde = float(input("Solde du compte de Guillaume? "))
    marion_solde = float(input("Solde du compte de Marion? "))

    if guillaume_solde >= 0 and marion_solde >= 0:
        print("Tous les deux en positif!")

    elif guillaume_solde < 0 and marion_solde < 0:
        print("Tous les deux en négatif!")
        print("Impossible de rétablir la situation.")

    elif guillaume_solde >= 0 and marion_solde < 0:
        print("Marion est en négatif.")
        if guillaume_solde >= abs(marion_solde):
            nouveau_solde_guillaume = guillaume_solde + marion_solde
            print(f"Guillaume peut lui transférer {abs(marion_solde)} euros (il lui restera {nouveau_solde_guillaume} euros).")
        else:
            print("Impossible de rétablir la situation.")

    elif guillaume_solde < 0 and marion_solde >= 0:
        print("Guillaume est en négatif.")
        if marion_solde >= abs(guillaume_solde):
            nouveau_solde_marion = marion_solde + guillaume_solde
            print(f"Marion peut lui transférer {abs(guillaume_solde)} euros (il lui restera {nouveau_solde_marion} euros).")
        else:
            print("Impossible de rétablir la situation.")