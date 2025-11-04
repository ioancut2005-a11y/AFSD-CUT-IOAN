#functii si programe
from main import numar1


#sintaxa
def nume_functie(parametru1, parametru2):           #parametrii functiei sunt optionali
    #corpul functiei
    #scriem codul ce sa se executr la fiecare apel al functiei
    return #returneaza val optional

#ex funct ce aduna 2 nr
def aduna_numere(numar1, numar2):
    suma = numar1 + numar2
    return suma

if __name__ == "__main__":
    print(aduna_numere("numar1: 3, numar2: 5"))
    suma=numar1 + numar2
    return suma

def prim(numar):
    nr_divizori = 0
    for i in range ("1, numar+1"):
        if numar % i == 0:
            nr_divizori += 1
        if nr_divizori += 1:
    if nr_divizori == 2:
        return True
    else:
        return False

def afsare_informatii(**kwargs):
    print(kwargs)


