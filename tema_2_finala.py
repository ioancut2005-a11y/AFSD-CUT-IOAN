#DATE INITIALE
elevi = ["Ana", "Bogdan", "Carmen", "Darius", "Elena"]
note  = [9,       7,        10,       4,        8]

elev_nou        = "Felix"
nota_elev_nou   = 6
elev_de_sters   = "Darius"

interogari_nume = ["Ana", "Mara", "Elena", "stop"]

absente = [1, 0, 2, 3, 0]
#FIECARE ELEV ARE O NOTA PE ACEEASI POZITIE

#PARTEA A
#A1 LISTEAZA ELEVII CU NOTELE LOR
print("A1")
for i in range(len(elevi)):
    print(f"{elevi[i]} are nota {note[i]}")
print("--------------")
print("A2")
#A2 NOTA MAXIMA SI MINIMA
nota_maxima = max(note)
nota_minima = min(note)

print(f"Nota maxima: {nota_maxima}, elev:", end="")
for i in range(len(note)):
    if note[i] == nota_maxima:
        print(elevi[i], end="")
print()
print(f"Nota minima: {nota_minima}, elev:", end="")
print()
print("---------------")
print("A3")
#A3 MEDIA CLASEI
media_clasei = sum(note)/len(note)
print(f"Media clasei: {media_clasei:.2f}")
print("---------------")
print("A4")
#A4 PROMOVATI
print("Elevii promovati:")
for i in range(len(note)):
    if note[i] >= 5:
        print(elevi[i])
print("---------------")
#PARTEA B
#B5 NOTE CU 1P IN PLUS
print("B5")
for i in range(len(note)):
    note[i] = min(note[i] + 1, 10)
print("Note dupa marire:", note)
print("---------------")

#B6 ADD ELEVUL FELIX
print("B6")
elevi.append(elev_nou)
note.append(nota_elev_nou)
print("elevi", elevi)
print("note", note)
print("---------------")

#B7 STERGERE ELEV DARIUS
print("B7")
if elev_de_sters in elevi:
    poz = elevi.index(elev_de_sters)
    elevi.pop(poz)
    note.pop(poz)
    print(f"{elev_de_sters} este eliminat din lista")
else:
    print(f"{elev_de_sters} nu este in lista")
print("Elevi:", elevi)
print("Note:", note)
print("---------------")

#B8 AFISEAZA LISTA NOUA
print("B8")
for i in range(len(elevi)):
    print(f"{elevi[i]} are nota {note[i]}")
print("---------------")

#C9 CAUTARI NUME WHILE
print("C9")
i = 0
while i < len(interogari_nume) and (interogari_nume[i]) != "stop":
    nume = interogari_nume[i]
    if nume in elevi:
        poz = elevi.index(nume)
        print(f"{nume} are nota {note[poz]}")
    else:
        print(f"{nume} nu exista")
    i += 1
print("---------------")
#PROMOVATI SI RESPINSI
print("C10")
print("Total elevi promovati si respinsi:")
promovati = 0
respinsi = 0
for n in note:
    if n >= 5:
        promovati += 1
    else:
        respinsi += 1
print(f"Promovati: {promovati}")
print(f"Respinsi: {respinsi}")
print("---------------")
#MEDIA PROMOVATI
print("C11")
note_promovati= [n for n in note if n >= 5]
if len(note_promovati) > 0:
    media_promovati = sum(note_promovati) / len(note_promovati)
    print(f"Media promovati: {media_promovati:.2f}")
else:
    print("No promovati")