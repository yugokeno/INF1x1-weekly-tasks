def est_premier(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

try:
    n = int(input("Nombre : "))
    if est_premier(n):
        print(f"{n} est premier.")
    else:
        print(f"{n} n'est pas premier.")
except ValueError:
    print("Veuillez entrer un entier valide.")
