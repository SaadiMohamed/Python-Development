leeftijden = []
ingave = 0
while(ingave != ""):
    ingave = input("Geef alle leeftijden van de groep 1 per 1 in: ")
    if (ingave != ""):
        leeftijden.append(ingave)


aantalOnder3 = 0
aantalTussen3en12 = 0
aantal65Ouder = 0
aantalTussen12en65 = 0
totaalprijs = 0
for i in leeftijden:
    if(int(i) < 3):
        aantalOnder3 = aantalOnder3 + 1
    elif(int(i) < 12 and int(i) > 3 ):
        aantalTussen3en12 = aantalTussen3en12 + 1
        totaalprijs = totaalprijs + 15
    elif (int(i) > 65):
        aantal65Ouder = aantal65Ouder +1
        totaalprijs = totaalprijs + 20
    else:
        aantalTussen12en65 = aantalTussen12en65 +1
        totaalprijs = totaalprijs + 30

print(f"Jullie zijn met {len(leeftijden)} man totaal")
print(f"aantal onder de 3: {aantalOnder3}")
print(f"aantal tussen de 3 en 12: {aantalTussen3en12}")
print(f"aantal tussen de 12 en 65: {aantalTussen12en65}")
print(f"aantal ouder dan 65: {aantal65Ouder}")

print(f"Totaalprijs is : {round(totaalprijs,2)}")