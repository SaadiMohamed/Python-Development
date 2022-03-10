def verminderLijst(getal, lijst):
    if (getal * 2) >= len(lijst):
        print("DIT KAN NIET JE GETAL IS TE GROOT VOOR JE LIJST")
    else:
        lijst.sort()
        for i in range(0,getal,1):
            del lijst[0]
            del lijst[-1]
        return lijst


givenNumber = -1
getallen = []

while givenNumber != 0:
    givenNumber = int(input("Geef een geheel getal in, als je wilt stoppen geef het getal 0 in: "))
    if givenNumber != 0:
        getallen.append(givenNumber)

verwijderenGetal = int(input("Geef een geheel getal in om de kleinste en grootste n waardes te verwijderen: "))

print(verminderLijst(verwijderenGetal,getallen))