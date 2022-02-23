from oefn8 import Priemgetal

if __name__ == "__main__":
    getal = int(input("Geef een getal in en wij geven het volgende priemgetal: "))

    NieuweGetal = False
    while (NieuweGetal == False):
        getal = getal + 1
        NieuweGetal = Priemgetal(getal)
    
    print(f"Het volgende priemgetal is {getal}")
