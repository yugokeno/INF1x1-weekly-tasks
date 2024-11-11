def calculer_carre():
    while True:
        nombre = float(input("Nombre: "))
        
        carre = nombre ** 2
        print(f"Le carre de ce nombre est {carre}")
        
        recommencer = input("Voulez-vous recommencer? ").lower()
        
        if recommencer == "non":
            print("Au revoir")
            break

calculer_carre()