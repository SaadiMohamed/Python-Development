jaar = int(input("Geef een jaar op: "))

if (jaar % 4 == 0):
    if(jaar % 100 != 0):
        print("Het is een schrikkeljaar")
    else:
        if(jaar % 400 == 0):
            print("Het is een schrikkeljaar")
        else:
            print("Het is geen schrikkeljaar")
else:
    print("Het is geen schrikkeljaar")

