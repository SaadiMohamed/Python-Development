def schrikkeljaar(jaar):
    if (jaar % 4 == 0):
        if(jaar % 100 != 0):
            #print("Het is een schrikkeljaar")
            return True
        else:
            if(jaar % 400 == 0):
                #print("Het is een schrikkeljaar")
                return True
            else:
                #print("Het is geen schrikkeljaar")
                return False
    else:
        #print("Het is geen schrikkeljaar")
        return False

def BerekenDagen(maand, jaar):
    normaalDagen = [31,28,31,30,31,30,31,31,30,31,30,31]
    result = schrikkeljaar(jaar)
    if result == True:
        normaalDagen[1] = 29
    
    return normaalDagen[maand-1]

def main():
    maand = int(input("Geef de maand op waarvan je de aantal jaren wilt weten (in getallen): "))
    jaar = int(input("Geef het jaar op: "))
    print(f"Er zijn {BerekenDagen(maand,jaar)} dagen in dat maand")

if __name__ == "__main__":
    main()