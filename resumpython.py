def menu():
    opcio=0
    while opcio<1 or opcio >5:
        print("""
            Menú principal:
            1. Programació estructurada
            2. Programacio funcional
            3. Programacio orientada a objectes
            4. Accés a fitxers
            5. Sortir
        """)
        opcio = int(input("Selecciona una opció: "))
        if opcio <1 or opcio >5:
            print("Opció no vàlida!")
        else:
            return opcio
        
def programacio_estructurada():
    print("Has entrat a la programació estructurada")
def programacio_funcional():
    print("Has entrat a la programació funcional")
def programacio_oo():
    print("Has entrat a la programació orientada a objectes")
def acces_fitxers():
    print("Has entrat a l'accés a fitxers")
#Programa Principal
op=1
while op!=5:
    op=menu()
    match(op):
        case 1:
            programacio_estructurada()
        case 2:
            programacio_funcional()
        case 3:
            programacio_oo()
        case 4:
            acces_fitxers()
        case 5:
            print("Gràcies per utilitzar l'aplicació")
        case other:
            print("Error!")
menu()