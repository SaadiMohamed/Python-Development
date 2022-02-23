from oefn14 import BerekenDagen

def MagicDate(dag,maand,jaar):
    jaarLaatse = str(jaar)
    jaarLaatse = int(jaarLaatse[2] + jaarLaatse[3])


    if (dag * maand == jaarLaatse):
        print(f"{dag}/{maand}/{jaar} is een magische datum")
        return True
    else:
        return False

def main():
    #dag = int(input("Geef de dag in: "))
    #maand = int(input("Geef de maand in: "))
    #jaar = int(input("Geef het jaar in: "))

    for i in range (1900, 2001):
        for j in range (1,13):
            for y in range(1,BerekenDagen(j,i)+1):
                MagicDate(y,j,i)



if __name__ == "__main__":
    main()