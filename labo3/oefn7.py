from matplotlib.pyplot import get


def is_integer(getal):
    getal = getal.strip()
    if(getal[0] == "+" or getal[0] == "-" or getal[0].isalpha() == False):
        for i in range(0,len(getal)):
            if(getal[i].isalpha() == True):
                return False
        return True
    return False

if __name__ == "__main__":
    getal = input("Geef een getal in en wij checken of het een getal is: ")
    result = is_integer(getal)
    print(result)



