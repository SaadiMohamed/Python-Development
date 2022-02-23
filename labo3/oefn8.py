from re import I
from matplotlib.pyplot import get
from numpy import False_


def Priemgetal(getal):

    for i in range(1,getal+1,1):
        if (i != 1):
            if(i != getal):
                if(getal % i == 0):
                    return False
    return True


if __name__ == "__main__":
    getal = int(input("Geef een getal in en wij checken of het een priemgetal is: "))
    result = Priemgetal(getal)
    print(result)    
    