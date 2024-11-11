def previsions_annuelles(annee):
    adherents = 100
    croissance = 1.08
    for _ in range(2017, annee):
        adherents = round(adherents * croissance)
    return adherents

def previsions_details(annee):
    adherents = 100
    croissance = 1.08
    adherents_par_annee = []
    for an in range(2017, annee + 1):
        adherents_par_annee.append((an, adherents))
        adherents = round(adherents * croissance)
    return adherents_par_annee

def adhesions_cumulees(annee):
    details = previsions_details(annee)
    return sum(adherents for _, adherents in details)

def annee_pour_m_adherents(nombre_vise):
    annee = 2017
    adherents = 100
    croissance = 1.08
    while adherents < nombre_vise:
        adherents = round(adherents * croissance)
        annee += 1
    return annee

def menu(): 
    incorrect = False
    while True:
        if not incorrect:
            print("Menu, veuillez choisir :")
            print("1. Prévisions adhérents à l'année N (resumé)")
            print("2. Prévisions adhérents à l'année N (détails)")
            print("3. Adhésions cumulées à l'année N")
            print("4. Année à laquelle on obtiendra M adhérents")
            print("Q. Quitter")
        
        choix = input().strip()
        
        if choix == '1': 
            incorrect = False
            annee = int(input("Choisissez une année : ").strip())
            adherents = previsions_annuelles(annee)
            print(f"En {annee} il y aura {adherents} adherents.\n")
        
        elif choix == '2': 
            incorrect = False
            annee = int(input("Choisissez une année : ").strip())
            details = previsions_details(annee)
            for an, adherents in details:
                if an == 2017:
                    print(f"En {an} il y a {adherents} adherents.")
                else:
                    print(f"En {an} il y aura {adherents} adherents.")
            print()
        
        elif choix == '3': 
            incorrect = False
            annee = int(input("Choisissez une année : ").strip())
            cumul = adhesions_cumulees(annee)
            print(f"De 2017 à {annee} il y aura {cumul} adhésions cumulées.\n")
        
        elif choix == '4': 
            incorrect = False
            nombre_vise = int(input("Entrez le nombre d'adherents voulus : ").strip())
            annee = annee_pour_m_adherents(nombre_vise)
            print(f"On atteindra {nombre_vise} adherents en {annee}.\n")
        
        elif choix == 'Q': 
            incorrect = False
            print("Au revoir.")
            break
        
        else:
            incorrect = True
            print("Choix invalide, recommencez :", end='')

menu()