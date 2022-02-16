klinkers = ["a","e","i","o","u"]
letter = input("Geef een letter in: ")

if letter.lower() in klinkers:
    print(f"{letter} is een klinker")
elif letter.lower() == "y":
    print(f"{letter} is soms een klinker en soms een medeklinker")
elif len(letter) > 1:
    print(f"Dit kan ik niet weten, je mag maar 1 letter ingeven")
else:
    print(f"Dit is een medeklinker")
