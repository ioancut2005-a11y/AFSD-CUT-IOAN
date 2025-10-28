lista_de_numere= [10, 20, 30, 40, 50]
print(lista_de_numere[1])

lista1= [1, 2, 3]
lista2= [4, 5, 6]
print(lista1 + lista2)
print(lista1 * 3)

#functii utile
#len(lista)
lista=[100, 20, 30, 40]
print(max(lista))
print(min(lista))
print(sum(lista))

#adaugam elem in lista
# append(lista)

lista3=[1, 2, 3]
lista3.append(10)
print(lista3)
#sau cu .insert
lista3.insert(1, 77)
print(lista3)

#stergere lista
# .pop()
# .remove(cifra pe care vrem sa o eliminam)

#sortam liste
# cu sort()
lista_1 =[5,3,5,6]
print(lista_1)
lista_1.sort()
print(lista_1)

# sorted ca sa nu ne modif lista initiala

#cautarea elem in lista
#index(element)
listaa=[5,3,5,6]
index_element=lista.index(3)
print(index_element)

#count numaram elementele
print(listaa.count(2))

#afisam elem pare
lista_2 = [101, 204, 300, 404]
print("Elemente pare:")
for element in lista_2:
    if element  %2 == 0:
         print(element)

