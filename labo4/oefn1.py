givenNumber = -1
getallen = []

while givenNumber != 0:
    givenNumber = int(input("Geef een geheel getal in, als je wilt stoppen geef het getal 0 in: "))
    if givenNumber != 0:
        getallen.append(givenNumber)

getallen.sort()
print(getallen)