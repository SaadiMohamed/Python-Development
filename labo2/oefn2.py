leeftijdMensenJaren = int(input("Geef je leeftijd van je hond in mensen jaren: "))

if (leeftijdMensenJaren < 0):
    print("Dit is niet mogelijk")
elif (leeftijdMensenJaren > 0 and leeftijdMensenJaren < 3 ):
    print(f"je hond is {(leeftijdMensenJaren * 10.5)} jaar oud in hondenjaren")
else:
    print(f"Je hond is {int((2* 10.5) + ((leeftijdMensenJaren-2)*4))} jaar oud in hondenjaren")