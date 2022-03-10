woorden =[]
woord = input("geef steeds een woord in, als je wilt stoppen geef dan niets in: ")

while woord != "":
    woord = input("geef steeds een woord in, als je wilt stoppen geef dan niets in: ")
    if woord != "":
        woorden.append(woord)


for woord in set(woorden):
    print(woord)
