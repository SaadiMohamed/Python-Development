
def white_space(woord, ruimte):
    newWoord =""
    if (len(woord) > ruimte):
        return woord
    else:
        for i in range(0,(ruimte- len(woord)),1):
            newWoord = newWoord + " "
        
        newWoord = newWoord + woord
    
    return newWoord


woord = input("Geef een woord in: ")
ruimte = int(input("Geef het aantal karakters ruimte in: "))
NieuweWoord = white_space(woord, ruimte)
print(NieuweWoord)



    