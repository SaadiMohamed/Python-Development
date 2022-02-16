maanden31Dagen = ["januari","maart","mei","juli","augustus","oktober","december"]
maanden30Dagen = ["april","juni","september","november"]

maand = input("Geef een maand op?: ")

if maand.lower() in maanden30Dagen:
    print("30")
elif maand.lower() in maanden31Dagen:
    print("31")
elif maand.lower() == "februari":
    print("28 of 29")
else:
    print("Dit is geen geldige maand")