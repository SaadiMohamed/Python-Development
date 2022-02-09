import math

straal = float(input("Wat is de straal van de cilinder? (in meter): "))
hoogte = float(input("Wat is de hoogte van de cilinder? (in meter): "))

oppervlakte = math.pi * straal ** 2

volume = oppervlakte * hoogte

print(f"De volume van je cilinder is {round(volume,1)} m³")
