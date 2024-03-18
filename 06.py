def coincideixen(llista):
    l=[]
    for i,e in enumerate(llista):
        if e == i:
            l.append(e)
    print("Els elements de la llista \n{} \n que coincideixen en la seva posició són \n {}".format(llista,l))
l=[3,7,2,3,4,5,6,7,8,9,10,1]
coincideixen(l)