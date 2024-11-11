
def NextElem(elm, liste):
    if elm not in liste:
        return None
    index = liste.index(elm)
    return liste[(index + 1) % len(liste)]

def encode(texte, ordre):
    texte_encode = []
    for char in texte:
        if char in ordre:
            texte_encode.append(NextElem(char, ordre))
        else:
            texte_encode.append(char)
    return ''.join(texte_encode)

if __name__=="__main__": # NE PAS SUPPRIMER CETTE LIGNE
    # Votre programme principal ne sera pas évalué.
    # Utilisez-le pour tester votre programme en faisant
    # les appels de votre choix.
    # Respectez bien ce niveau d'identation.
    print("Debut du prog. principal")
    
    ordre1=list("abcdefghijklmnopqrstuvwxyz ,;:!?.")
    ordre2=list("az.erty,uiop:qsdfg!hjklm;wxcv?bn ")
    ordre_alpha = list("abcdefghijklmnopqrstuvwxyz.,!? ")
    texte = "bonjour, comment ca va?"
    texte_encode = encode(texte, ordre_alpha)
    print("Texte original :", texte)
    print("Texte chiffré :", texte_encode) 
