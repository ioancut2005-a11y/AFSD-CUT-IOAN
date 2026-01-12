tabla=[
    [".", ".", "."],
    [".", ".", "."],
    [".", ".", "."]
]
def arata_tabla():
    print("\n  0 1 2")
    for i in range(3):
        print(f"{i} ", end="")
        for j in range(3):
            print(tabla[i][j], end=" ")
        print()
def verifica_jocul():
    #verificam liniile
    for i in range(3):
        if tabla[i][0] == tabla[i][1]==tabla[i][2] and tabla[i][0] != ".":
            return tabla[i][0]  #x sau 0
    #verificam coloanele
    for j in range(3):
        if tabla[0][j] == tabla[1][j]==tabla[2][j] and tabla[0][j] != ".":
            return tabla[0][j]
    #verificam diagonalele
    if tabla[0][0] == tabla[1][1] and tabla[2][2] and tabla[0][0] != ".":
        return tabla[0][0]
    if tabla[0][0]==tabla[1][1]==tabla[2][2] and tabla[0][0] != ".":
        return tabla[0][0]
    if tabla[0][2] == tabla[1][1] and tabla[2][0] and tabla[0][2] != ".":
        return tabla[0][2]
    #verificam daca mai sunt locuri libere
    liber=False
    for i in range(3):
        for j in range(3):
            if tabla[i][j]==".":
                liber=True
    if not liber:
        return "EGAL"
    return "CONTINUA"
print("~~~ JOC X SI O ~~~")
print("Folositi o,1 sau 2 pentru linie si coloana")
jucator="X"
joc_activ=True
while joc_activ:
    arata_tabla()
    print(f"\n Randul jucatorului {jucator}")
    linie_input=input("Linia(0, 1, 2):")
    coloana_input=input("Coloana(0, 1, 2):")
    if not linie_input.isdigit() or not coloana_input.isdigit():
        print("Trebuie sa introduci numere")
        continue
    linie=int(linie_input)
    coloana=int(coloana_input)

    if linie <0 or linie >2 or coloana <0 or coloana >2:
        print("Numerele trebuie sa fie 0 1 sau 2")
        continue

    if tabla[linie][coloana] != ".":
        print("Pozitia este deja ocupata")
        continue

    tabla[linie][coloana] = jucator

    rezultat=verifica_jocul()

    if rezultat == "X":
        arata_tabla()
        print("f\n Jucatorul X a castigat")
        joc_activ=False
    elif rezultat == "0":
        arata_tabla()
        print("f\n Jucatorul 0 a castigat")
        joc_activ=False
    elif rezultat == "EGAL":
        arata_tabla()
        print("f\n Egalitate")
        joc_activ=False

    if jucator=="X":
        jucator="0"
    else:
        jucator="X"
print("\n Joc terminat!!!")