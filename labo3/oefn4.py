def median(value1, value2,value3):
    getallen = [value1,value2,value3]
    getallen.sort()
    return getallen[1]


getal1 = int(input("Geef je eerste getal in: "))
getal2 = int(input("Geef je tweede getal in: "))
getal3 = int(input("Geef je derde getal in: "))

mediaan = median(getal1,getal2,getal3)

print(f"De mediaan is {mediaan}")