from functools import reduce
def Passar_a_numero(llista):
    a = list(map(lambda x: str(x),llista))
    b = reduce(lambda x,y:x+y,a)
    print("La llista {} és el número {}".format(llista,b))
#P.Principal
C = [3,5,7,9,1]
Passar_a_numero(C)