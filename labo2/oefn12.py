
getallen = []

getal = int(input("Geef een geheel getal in of geef 0 in om te stoppen: "))
if(getal == 0):
    print("Je mag niet starten met een 0")
else:
    getallen.append(getal)
    while(getal != 0):
        getal = int(input("Geef een geheel getal in of geef 0 in om te stoppen: "))
        if (getal == 0):
            break
        else:
            getallen.append(getal)

som = 0
for i in getallen:
    som = som + i

gemiddelde = som / len(getallen)
print(gemiddelde)
        
    

