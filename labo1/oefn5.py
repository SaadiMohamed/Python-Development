KLEINE_FLES_PRIJS = 0.12
GROTE_FLES_PRIJS = 0.25

aantalKleineFlessen = int(input("Hoeveel kleine flessen heb je?: "))
aantalGroteFlessen = int(input("Hoeveel grote flessen heb je?: "))

totaalPrijs = round((KLEINE_FLES_PRIJS * aantalKleineFlessen) + (GROTE_FLES_PRIJS * aantalGroteFlessen),2)

print(f"Aantal statiegeld: {totaalPrijs}")

