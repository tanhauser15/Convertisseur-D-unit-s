import variable

if __name__ == "__main__":
    
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
                variable.convetionPoucesCm()
            case 2:
                variable.convetionCmPouces()
            case _:
                print("Vous avez saisi la mauvais choix veillez réessayer.")
    except ValueError:
        print("Seuls les chiffres sont autorisés. Veuillez réessayer.")
    