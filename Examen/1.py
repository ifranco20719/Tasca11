def menu():
    op = 0
    while op<1 or op>14:
        print("""
        Programa Principal
        1. Estructures condicionals, if
        2. Estructures condicionals, match
        3. Estructures iteratives, for e in b
        4. Estructures iteratives, for i in range(x)
        5. Estructures iteratives, for i,e in enumerate(a)
        6. Funció amb paràmetres
        7. Funció lambda
        8. Funció list comprehension
        9. Funció map
        10. Funció zip
        11. Funció filter
        12. Classes i objectes
        13. Fitxers
        14. Sortir
        """)
        op=int(input("Introdueix una opció: "))
        if op<1 or op>14:
            print("Opció no vàlida, torni a elegir una opció \n")
        else:
            return op

def ex1():
    a=int(input("Introdueix el primer nombre: "))
    b=int(input("Introdueix el segon nombre: "))
    if a>b:
        print("{} és major que {}".format(a,b))
    elif b>a:
        print("{} és major que {}".format(b,a))
    else:
        print("{} i {} són iguals".format(a,b))

def ex2():
    c=input("Introdueixi una vocal (a,e,i,o,u): ")
    match(c):
        case 'a':
            print("Has introduit la vocal a")
        case 'e':
            print("Has introduit la vocal e")
        case 'i':
            print("Has introduit la vocal i")
        case 'o':
            print("Has introduit la vocal o")
        case 'u':
            print("Has introduit la vocal u")


def ex3():
    a=[]
    b=[]
    for i in range(3):
        a.append(input("Introdueixi la paraula"))
    for e in a:
        b.append(len(e))
    print("Les longituds de la llita {} són {}".format(a,b))

def ex4():
    for i in range(1,10,2):
        print(i)

def ex5():
    a=[1, 2, 3, 4, 5]
    d={}
    for i,e in enumerate(a):
        d[i]=e
    print(d)

def ex6(l,c):
    b=[]
    for e in l:
        if c in e:
            b.append(e)
    print("De la llista {}, les següents {} contenen el caràcter {}".format(l,b,c))

def ex7():
    a=[3, 4, 6, 8, 9]
    b=list(map(lambda x: x+10, a))
    print(b)

def ex8():
    a=[3,4,6,8,9]
    b=[e**2 for e in a if e%2==1]
    print(b)

def ex9():
    a=["Piano", "Bateria", "Clarinet", "Saxo", "Cello"]
    b=list(map(lambda x: x[::-1],a))
    print(b)

def ex10():
    a=[1,2,3,4,5]
    b=[6,7,8,9,10]
    c=dict(map(lambda x: a[x], b))
    print(c)

def ex11():
    a= [1, 2, 3, 4, 5]
    b= list(filter(lambda x: x%2==1))
    print(b)

def ex12():
    class Ordinador():
        def __init__(self, tipus, pantalla):
            self.tipus=tipus
            self.pantalla=pantalla
        def getTipus(self):
            pass
        def getPantalla(self):
            pass

    class Portatil(Ordinador):
        def getTipus(self):
            print('Pantalla')
        def getPantalla(self):
            print('15"')

    class Tablet(Ordinador):
        def getTipus(self):
            print('Pantalla')
        def getPantalla(self):
            print('9"')

    class Servidor(Ordinador):
        def getTipus(self):
            print('Pantalla')
        def getPantalla(self):
            print('21"')

    class PC(Ordinador):
        def getTipus(self):
            print('PC')
        def getPantalla(self):
            print('27"')

    llista = [Portatil('Soc un portatil', '15"'), Tablet('Soc una tablet', '9"'), Servidor('Soc un servidor', '21"'), PC('Soc un PC', '27"')]

def ex13():
    with open("/home/cicles/AO/ex20.txt","w") as f:
        for i in range(10):
            f.write(i+"\n")
    with open("/home/cicles/AO/ex20.txt","r") as f:
        for i in f:
            print(i)

#Programa principal
op=1
while op!=14:
    op=menu()
    match(op):
        case 1:
            ex1()
        case 2:
            ex2()
        case 3:
            ex3()
        case 4:
            ex4()
        case 5:
            ex5()
        case 6:
            ex6()
        case 7:
            ex7()
        case 8:
            ex8()
        case 9:
            ex9()
        case 10:
            ex10()
        case 11:
            ex11()
        case 12:
            ex12()
        case 13:
            ex13()