def moyenne_ponderee(note1, note2, coeff1, coeff2):
    total_notes = (note1 * coeff1) + (note2 * coeff2)
    total_coeffs = coeff1 + coeff2
    moyenne = total_notes / total_coeffs
    return moyenne


        
if __name__=="__main__": # NE PAS SUPPRIMER CETTE LIGNE
    # Votre programme principal ne sera pas évalué.
    # Utilisez-le pour tester votre programme en faisant
    # les appels de votre choix.
    # Respectez bien ce niveau d'identation.
    print("Debut du prog. principal")