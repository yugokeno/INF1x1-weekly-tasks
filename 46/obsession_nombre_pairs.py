
def somme_pairs(liste):
    return sum(x for x in liste if x % 2 == 0)

def nb_elem_pairs(liste):
    return sum(1 for x in liste if x % 2 == 0)

def max_pair(liste):
    return max(x for x in liste if x % 2 == 0)

def min_pair(liste):
    pairs = [x for x in liste if x % 2 == 0]
    return min(pairs) if pairs else None

def indice_de(entier, liste):
    for i, x in enumerate(liste):
        if x == entier:
            return i
    return None

def trouve_premier_pair(liste):
    for x in liste:
        if x % 2 == 0:
            return x
    return None

def extrait_pairs(l1):
    return [x for x in l1 if x % 2 == 0]

if __name__ == "__main__":
  print("Début du prog. principal")
