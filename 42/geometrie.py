    
import math

def coord_centre_cercle(x1, y1, x2, y2):
    x = (x1 + x2) / 2
    y = (y1 + y2) / 2
    return x, y

def coord_bas_losange(x1, y1, x2, y2):
    x = x2
    y = y1 - (y2 - y1)
    return x, y


def coordDEF():
    xA = float(input("Entrez l'abscisse de A (xA): "))
    yA = float(input("Entrez l'ordonnée de A (yA): "))
    xB = float(input("Entrez l'abscisse de B (xB): "))
    yB = float(input("Entrez l'ordonnée de B (yB): "))
    xC = float(input("Entrez l'abscisse de C (xC): "))
    yC = float(input("Entrez l'ordonnée de C (yC): ")) 
    
    xD = (xA + xB) / 2
    yD = (yA + yB) / 2
    E = coord_bas_losange(xA, yA, xB, yB)
    xF = (xC + E[0]) / 2
    yF = (yC + E[1]) / 2
    
    return xD, yD, E[0], E[1], xF, yF

def volume_sphere(r=1):
    return (4/3) * math.pi * r**3

def volume_cone(h, r=1):
    return (math.pi * r**2 * h) / 3

def volume_figure():
    r1 = float(input("Rayon de la sphère de gauche : "))
    r2 = float(input("Rayon de la sphère du milieu (même que le cône au-dessus) : "))
    r3 = float(input("Rayon de la sphère de droite : "))
    r_cone = float(input("Rayon du cône devant : "))
    h_cone = float(input("Hauteur du cône devant : "))
    h_cone_haut = float(input("Hauteur du cône au-dessus de la sphère : "))
    
    total_volume = (volume_sphere(r1) + volume_sphere(r2) + volume_sphere(r3) +
                    volume_cone(h_cone, r_cone) + volume_cone(h_cone_haut, r2))
    
    return total_volume

 

        
if __name__=="__main__": # NE PAS SUPPRIMER CETTE LIGNE 
    # Exemples d'utilisation des fonctions 2D
    print("Centre du cercle :", coord_centre_cercle(0, 0, 4, 4))
    print("Sommet inférieur du losange :", coord_bas_losange(2, 3, 4, 5))
    print("Coordonnées des points D, E, F :", coordDEF()) 
    print("Volume total de la figure :", volume_figure())
    # Votre programme principal ne sera pas évalué.
    # Utilisez-le pour tester votre programme en faisant
    # les appels de votre choix.
    # Respectez bien ce niveau d'identation.
    print("Debut du prog. principal")