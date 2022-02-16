maand = input("Geef de huidige maand op: ").lower()
dag = int(input("Geef de huidige dag op: "))

if ((maand == "april") or (maand == "mei") or (maand == "juni" and dag < 21) or (maand == "maart" and dag >= 20)):
    print("lente")
elif ((maand == "januari") or (maand == "februari") or (maand == "maart" and dag < 20) or (maand == "december" and dag >= 21)):
    print("winter")
elif ((maand == "juli") or (maand == "augustus") or (maand == "september" and dag < 22) or (maand == "juni" and dag >= 21)):
    print("zomer")
else:
    print("herfst")