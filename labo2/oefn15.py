woord = input("Geef een woord in en wij checken of het een palingdroom is: ")
nieuwewoord = ""

for i in range(len(woord)-1, -1, -1):
    nieuwewoord = nieuwewoord + woord[i]

if(nieuwewoord == woord):
    print(f"{woord} is een palingdroom")
else:
    print(f"{woord} is geen palingdroom")


