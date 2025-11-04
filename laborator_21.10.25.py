#structura decizionala if elif else



#if conditie   returneaza True sau False


#elif poate aparea de mai multe ori sau niciodata


#else poaate o data sau deloc





#comparam daca m1 este mai mare sau egal cu n2





numar1=7


numar2=8


if(numar1>numar2):


    print("Numarul 1 este mai mare decat numarul 2")


elif(numar1<numar2):


    print("Numar 1 mai mic deacr nr 2")


else:


    print("egale")





#verificam daca un nr este par sau impar


numar=11


if(numar%2==0):


    print("NUMAR PAR")


else:


    print("NUMAR IMPAR")


print("---------")


#verif daca un sir de caractere este gol sau nu gol


sir=""


if len(sir)==0:


    print("SIRUL ESTE GOL")


else:


    print("SIRUL NU ESTE GOL")





#verif daca sirul de caractere are @


#in este un operatpr ce verif daca un elem se afla intr o colectie


#"@" in sir


sir="testemail"


if "@" in sir:


    print("SIRUR CONTINE @")


else:


    print("SIRUL NU CONTINE @")





#VERIF DACA SIRUL E PALINDROM


#SE CITESTE LA FEL DE LA INCEPUT SPRE SFARSIT SI DE LA SF SPRE INCEPUT


sir="radar"


if sir==sir[::-1]:


    print("sirul este palindrom")


else:


    print("sirul nu este palindrom")





#numaram daca apare litera a sau A de numar par de ori intr un sir


sir="Azi este o zi frumoasa"


numar_caractere_a=sir.count("a")


numar_caractere_A=sir.count("A")





if numar_caractere_a + numar_caractere_A % 2==0:


    print("litera a apare de nr pari de ori")


else:


    print("litera a apare de nr impar de ori")


#structuri repetitive for si while


#range(start, stop, pas) genereaza o secv de numere


#start de unde incepem inclusiv


#stop unde ne oprim exclusiv


#pas cu cat crestem


for i in range(10):


    print (i,end="")





#for merge pe sir de caractere


sir="HELLO WORLD"


#2 moduri


#metoda 1 parcurgerea directa


for caracter in sir:


    print(caracter)


    print("*")


#metoda 2


#caracter=sir[0]


#caracter=sir[1]


#...


#caracter=sir[len(sir)-1]


#0,1,2,...,len(sir)-1=range(len(sir))


for i in range(len(sir)):


    print(i,sir[i])     #i este pozitia, sir[i] e valoarea de la pozitia i