def verzend_prijs(artikelen):
    prijs = 0
    if artikelen > 0:
        prijs = 8.5 + (float)(3 * (artikelen-1))
    
    return prijs

artikelen = int(input("Hoeveel artikels heb je?: "))
verzendkosten = verzend_prijs(artikelen)
print(f"De verzendkosten is in totaal {verzendkosten} euro")


