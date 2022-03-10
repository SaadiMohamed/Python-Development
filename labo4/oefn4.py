givenNumber = "-1"
getallen = []

while givenNumber != "":
    givenNumber = (input("Geef een negatief of positief geheel getal in, als je wilt stoppen geef niets in: "))
    if (givenNumber.startswith("-") and givenNumber[1:].isdigit() or givenNumber.isdigit()):
        getallen.append(givenNumber)

NieuweLijst = []
negatief = []
positief = []
nullen =[]


for getal in getallen:
    if int(getal) < 0:
        negatief.append(getal)
    elif (int(getal) == 0):
        nullen.append(getal)
    else:
        positief.append(getal)

NieuweLijst = negatief + nullen + positief

print(NieuweLijst)
