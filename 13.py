class Animal():
    def __init__(self, atribut, edat):
        self.atribut=atribut
        self.edat=edat
    def xerrar():
        pass
    def mourem():
        pass
    def quisoc():
        print("Sóc un animal")

class Cavall(Animal):
    def xerrar():
        print("Íiiiii")
    def mourem():
        print("Em moc a trot")
    def quisoc():
        print("Sóc un cavall")
class Dofi(Animal):
    def xerrar ():
        print("IchIchIch")
    def mourem ():
        print("Em moc nadant")
    def quisoc ():
        print("Soc un dofi")

class Abella(Animal):
    def xerrar ():
        print("Sssss")
    def mourem ():
        print("Em moc volant")
    def quisoc ():
        print("Sóc una abella")

class Huma(Animal):
    def xerrar ():
        print("Hola!")
    def mourem ():
        print("Em moc caminant")
    def quisoc ():
        print("Sóc un Humà")

class Centaure(Animal):
    def xerrar ():
        print("Hola!")
    def mourem ():
        print("Em moc a trot")
    def quisoc ():
        print("Sóc un centaure")

class Fiet(Huma):
    def __init__(self, nom, atribut, edat, llpares):
        self.nom=nom
        self.atribut=atribut
        self.edat=edat
        self.pares=llpares


class xou():
    def xerrar(self):
        print("Xou")
    def mourem(self):
        print("Em moc fent xou")
    def quisoc (self):
        print("Sóc un xou")

a = [Cavall("Marró","4"),Dofi("Gris","10"),Abella("Negre i groga","0,5"), Huma("Sibila","Cristià"), Centaure("Fiona","Marrón","18"),Fiet("Jordi","Moreno","9",["Fiona","Marc"]),xou()]
for e in a:
    e.xerrar()
    e.mourem()
    e.quiosc()