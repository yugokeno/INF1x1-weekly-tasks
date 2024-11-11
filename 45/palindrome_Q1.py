
def est_palindrome(mot):
    return mot == mot[::-1]

if __name__=="__main__": # NE PAS SUPPRIMER CETTE LIGNE
    # Votre programme principal ne sera pas évalué.
    # Utilisez-le pour tester votre programme en faisant
    # les appels de votre choix.
    # Respectez bien ce niveau d'identation.
    print("Debut du prog. principal")
    print(est_palindrome("kayak"))
    print(est_palindrome("elle"))
    print(est_palindrome("bonjour"))
 