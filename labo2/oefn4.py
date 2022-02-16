getallen = ["Drie","Vier","Vijf","Zes","Zeven","Acht","Negen","Tien"] 
zijden = int(input("Hoeveel zijden heeft je veelhoek?: "))

if (zijden > 10 or zijden < 3):
    print(f"Dit soort veelhoek bestaat niet")
else:
    print(f"Dit is een {getallen[zijden-3]}hoek")
