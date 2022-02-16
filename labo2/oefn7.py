jaar = int(input("Geef je gebrootejaar in: "))
rest = jaar % 12


if (jaar < 0):
    print("Dit is onmogelijk")
elif(rest == 4):
    print("Je bent een rat")
elif (rest == 5):
    print("Je bent een Os")
elif (rest == 6):
    print("Je bent een Tijger")
elif (rest == 7):
    print("Je bent een Konijn")
elif (rest == 8):
    print("Je bent een Draak")
elif (rest == 9):
    print("Je bent een Slang")
elif (rest == 10):
    print("Je bent een Paard")
elif (rest == 11):
    print("Je bent een Geit")
elif (rest == 0):
    print("Je bent een Aap")
elif (rest == 1):
    print("Je bent een Haan")
elif (rest == 2):
    print("Je bent een Hond")
elif (rest == 3):
    print("Je bent een Varken")
