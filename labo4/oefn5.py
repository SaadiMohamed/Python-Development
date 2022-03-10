def formater(woorden):
    zin = ""
    if(len(woorden) == 1):
        zin = woorden[0]
    elif(len(woorden) == 1):
        zin = woorden[0] + "en" + woorden[1]
    else:
        for i in range(0,len(woorden),1):
            if(i == len(woorden)-2):
                zin = zin + woorden[i] + " en "
            elif(i == len(woorden)-1):
                zin = zin + woorden[i]
            else:
                zin = zin + woorden[i]+ ","
    return zin

woorden =[]
woord = " "

while woord != "":
    woord = input("geef steeds een woord in, als je wilt stoppen geef dan niets in: ")
    if woord != "":
        woorden.append(woord) 

nieuwezin = formater(woorden)
print(nieuwezin)