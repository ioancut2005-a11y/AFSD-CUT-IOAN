lista=[1,4,7,3,5,6]
def bubble_sort(lista):
    interschimbare=False
    i=0
    while i<len(lista) -1:
        #i poz curenta
        #i+1 poz urm
        if lista[i] > lista [i+1]:
            interschimbare = True
            lista[i],lista[i+1]=lista[i+1],lista[i]
            i+=1
        print(lista)
        return lista

