def fixHoofdLetter(zinnen):
    nieuweZinbool = False
    nieuweZin = ""

    for i in zinnen:
        if(i.isalpha() == True and nieuweZinbool == False):
            nieuweZin = nieuweZin + i.upper()
            nieuweZinbool = True
        elif(i == "?" or i == "." or i == "!"):
            nieuweZinbool = False
            nieuweZin = nieuweZin + i
        else:
            nieuweZin = nieuweZin + i
    return nieuweZin

zin = input("Geef een zin op: ")
print(f"{fixHoofdLetter(zin)}")


