
def est_premier(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def plus_grand_diviseur_premier(n):
    diviseur = None
    for i in range(2, n + 1):
        if n % i == 0 and est_premier(i):
            diviseur = i
    return diviseur


def pgcd(a, b):
    while b:
        a, b = b, a % b
    return a


def ppcm(a, b):
    return abs(a * b) // pgcd(a, b)


def irreductible(numerateur, denominateur):
    return pgcd(numerateur, denominateur) == 1

if __name__=="__main__": # NE PAS SUPPRIMER CETTE LIGNE
    # Votre programme principal ne sera pas évalué.
    # Utilisez-le pour tester votre programme en faisant
    # les appels de votre choix.
    # Respectez bien ce niveau d'identation.
    print("Debut du prog. principal")
    n = 28
    print("Plus grand diviseur premier de", n, ":", plus_grand_diviseur_premier(n))

    a, b = 12, 18
    print("PGCD de", a, "et", b, ":", pgcd(a, b))
    print("PPCM de", a, "et", b, ":", ppcm(a, b))

    numerateur, denominateur = 3, 4
    print("La fraction", numerateur, "/", denominateur, "est irréductible :", irreductible(numerateur, denominateur))