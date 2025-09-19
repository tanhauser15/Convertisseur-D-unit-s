
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