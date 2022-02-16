alfabet = "abcdefghijklmnopqrstuvwxyz"
alfabetHoofdletter = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

zin = input("Geef en zin en wij decrypteren het met een ceaser factor: ")
factor = int(input("Wat is jouw factor?: "))
NieuweZin = ""

for i in zin:
    if(i in alfabet or i in alfabetHoofdletter):
        nieuweFactor = (alfabet.find(i) + factor)% 26
        if (nieuweFactor < 0):
            NieuweZin = NieuweZin + alfabet[26 - abs(nieuweFactor)]
        else:
            NieuweZin = NieuweZin + alfabet[(alfabet.find(i) + factor)% 26]
    else:
        NieuweZin = NieuweZin + i

print(NieuweZin)
