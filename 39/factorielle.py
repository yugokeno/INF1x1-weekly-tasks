def factorielle(n):
    if n < 0:
        print("La factorielle n'est pas définie pour les nombres négatifs.")
        return
    elif n == 0:
        print("La factorielle de 0 vaut 1 .")
        return 1
    else:
        result = 1
        for i in range(1, n + 1):
            result *= i
        print(f"La factorielle de {n} vaut {result} .")
        return result

try:
    n = int(input("n=? "))
    factorielle(n)
except ValueError:
    print("Veuillez entrer un entier valide.")