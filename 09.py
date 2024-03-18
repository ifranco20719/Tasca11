def pot(p):
    r = [x**p for x in range (1,10)]
    print("Les potències elevades a {} dels 10 primers números és {}".format(p,r))
p=int(input("Introdueixi un número al qual voleu elevar la resta: "))
pot(p)