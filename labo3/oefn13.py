def breukenVereeenvoudigen(teller, noemer):
    kleinste = 0
    grootste = 0
    gemeenschappelijkedeler = 0
    if teller > noemer:
        kleinste = noemer
        grootste = teller
    else:
         kleinste = teller
         grootste = noemer

    for i in range(kleinste,0,-1):
        if ((kleinste % i == 0) and (grootste % 1 == 0)):
            gemeenschappelijkedeler = i
        break
    teller = int(teller / gemeenschappelijkedeler)
    noemer = int(noemer / gemeenschappelijkedeler)
    print(f"vereenvoudigde breuk is {teller}/{noemer}")

def main():
    teller = int(input("Geef de teller op: "))
    noemer = int(input("Geef de noemer op: "))
    breukenVereeenvoudigen(teller,noemer)


if __name__ == "__main__":
    main()
       

