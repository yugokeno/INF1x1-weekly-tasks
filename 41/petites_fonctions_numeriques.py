def f(x):
    return 4 * x ** 2 - x + 5

def coteAB(coteAC, hypotenuse):
    return (hypotenuse ** 2 - coteAC ** 2) ** 0.5

def conversion_feet_m(feet):
    return feet * 0.3048

def distance_manh(xA, yA, xB, yB):
    return abs(xA - xB) + abs(yA - yB)