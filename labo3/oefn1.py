import math


zijde1 = float(input("Geef de lengte van de eerste zijde in m: "))
zijde2 = float(input("Geef de lengte van de tweede zijde in m: "))

def hypotenusa_berekenaar(zijde1, zijde2):
    return (zijde1**2) + (zijde2**2)

schuine_zijde = hypotenusa_berekenaar(zijde1, zijde2)
schuine_zijde = math.sqrt(schuine_zijde)
print(f"De schuine zijde is gelijk aan {schuine_zijde}m")


