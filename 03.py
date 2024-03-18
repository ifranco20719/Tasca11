def filtrar(llista,c):
    f = list(filter(lambda x : x[0]==c.lower() or x[0]==c.upper(), llista))
    print("De la llista {}, les paraules que comencen per {} són {}".format(llista,c,f))
#PP
llista = ["Josep", "Joana", "Jordi", "Maria", "Marc", "Pepe", "Paula"]
c = "j"
filtrar(llista,c)