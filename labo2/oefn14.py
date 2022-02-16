alfabet = "abcdefghijklmnopqrstuvwxyz"
alfabetHoofdletter = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

zin = input("Geef en zin en wij encrypteren het met een ceaser factor: ")
factor = int(input("Wat is jouw factor?: "))
NieuweZin = ""

for i in zin:
    if(i in alfabet or i in alfabetHoofdletter):
        NieuweZin = NieuweZin + alfabet[(alfabet.find(i) + factor)% 26]
    else:
        NieuweZin = NieuweZin + i

print(NieuweZin)



