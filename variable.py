
def convetionCmPouces():
    valuer_a_convertir = float(input("Entrez la valeur à convertir en pouce: "))
    ResultatConvertion = valuer_a_convertir*0.394
    print(f"{valuer_a_convertir} cm = {ResultatConvertion} pouces")
    
    choixContinuer = int(input("Continuer la conversion ? 1 'pour oui' ou 0 'pour non'"))
    if choixContinuer == 1:
        bouclerConversionCmPouces(choixContinuer)

def convetionPoucesCm():
    valuer_a_convertir = float(input("Entrez la valeur à convertir en cm: "))
    ResultatConvertion = valuer_a_convertir*2.54
    print(f"{valuer_a_convertir} pouces = {ResultatConvertion} cm")

    choixContinuer = int(input("Continuer la conversion ? 1 'pour oui' ou 0 'pour non'"))
    if choixContinuer == 1:
        bouclerConversionPoucesCm(choixContinuer)

def bouclerConversionPoucesCm(choix):
    while choix==1:
        valuer_a_convertir = float(input("Entrez la valeur à convertir en cm: "))
        ResultatConvertion = valuer_a_convertir*2.54
        print(f"{valuer_a_convertir} pouces = {ResultatConvertion} cm")
        
        choix = int(input("Continuer la conversion ? 1 'pour oui' ou 0 'pour non'"))

def bouclerConversionCmPouces(choix):
    while choix==1:
        valuer_a_convertir = float(input("Entrez la valeur à convertir en pouce: "))
        ResultatConvertion = valuer_a_convertir*0.394
        print(f"{valuer_a_convertir} cm = {ResultatConvertion} pouces")
        
        choix = int(input("Continuer la conversion ? 1 'pour oui' ou 0 'pour non'"))

def bouclerMenuPrincipale(continuer):
    while continuer:
            try:
                choix = int(input("""
            Souhaitez convertir des "Pouces vers cm" ou "cm vers Pouces"?
            Tapez:
            1 - Pour convertir des pouces vers cm
            2 - Pour convertir des cm vers pouces   

            Entrez votre choix:     
            """))
                match choix:
                    case 1: 
                        convetionPoucesCm()
                    case 2:
                        convetionCmPouces()
                    case _:
                        print("Vous avez saisi la mauvais choix veillez réessayer.")
            except ValueError:
                print("Seuls les chiffres sont autorisés. Veuillez réessayer.")
            
            choixContinuer = int(input("Retour au menu principal: 1 'oui' 0 'non': "))
            if choixContinuer == 0:
                continuer = False
                print("Fin du programme")