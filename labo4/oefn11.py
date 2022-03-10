from numpy import true_divide


def checkUnique(zin):
    letters = {}
    AantalUniek = 0
    zin = zin.replace(" ","")
    for i in zin:
        if i in letters.keys():
            letters[i] = letters[i] +1
        else:
            letters[i] = 1
    
    for i in letters.values():
        if i == 1:
            AantalUniek = AantalUniek +1
    return AantalUniek


zin = input("Geef een zin en wij zeggen hoeveel unieke charachters er zijn: ")
print(checkUnique(zin))
