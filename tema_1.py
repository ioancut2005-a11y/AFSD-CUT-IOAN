text="Termenul informatică desemnează știința procesării sistematice a informației, în special a procesării cu ajutorul calculatoarelor. Termenul englezesc corespunzător este Computer Science"
#(1)imparte sirul in doua parti egale
lungime_text=len(text)
mijloc_text=lungime_text // 2

partea1=text[:mijloc_text]
partea2=text[mijloc_text:]

#(2) pe prima parte

#transformam toate literele in majuscule
partea1=partea1.upper()

#eliminam toate spatiile goale de la inceputul si finalul irului
partea1=partea1.strip()

#(3) pe a doua parte
#inversam ordinea caracterelor pt a doua parte
partea2_invers=partea2[::-1]

#transf prima litera in majuscula
litera1_mare=partea2_invers[0].upper()
rest_partea2=partea2_invers[1:]
partea2_invers=litera1_mare+rest_partea2
partea2_finala=partea2_invers

#eliminam toate caracterele din partea 2
partea2_finala=partea2_finala.replace(",","")
partea2_finala=partea2_finala.replace(".","")
partea2_finala=partea2_finala.replace("!","")
partea2_finala=partea2_finala.replace("?","")

rezultat_final=partea1+partea2_finala
print(rezultat_final)