aantalDagen = int(input("Geef aantal dagen in: "))
aantalUren = int(input("Geef aantal uren in: "))
aantalMinuten = int(input("Geef aantal minuten in: "))
aantalSeconden = int(input("Geef aantal seconden in: "))

AANTAL_SECONDEN_DAG = 86400
AANTAL_SECONDEN_UUR = 3600
AANTAL_SECONDEN_MINUUT = 60

print(f"Totaal aantal seconden dan deze tijdstip vertegenwoordigt is {(aantalDagen * AANTAL_SECONDEN_DAG) + (aantalUren * AANTAL_SECONDEN_UUR) + (aantalMinuten * AANTAL_SECONDEN_MINUUT) + aantalSeconden}")