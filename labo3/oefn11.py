from pip import main


def passwordCheck(password):
    Min8char = False
    Min1Capital = False
    Min1Lower = False
    Min1Digit = False

    if(len(password) >8):
        Min8char = True
    
    for i in password:
        if(i.islower() == True):
               Min1Lower = True
        if(i.isupper() == True):
            Min1Capital = True
        if(i.isdigit() == True):
            Min1Digit = True

    if(Min1Capital == True and Min1Digit == True and Min1Lower == True and Min8char == True):
        return True
    else: 
        return False
        

def main():
    password = input("Geef een wachtwoord in en wij checken of het sterk of zwak is: ")
    result = passwordCheck(password)
    if result == True:
        print("Je wachtwoord is sterk")
    else:
        print("Je wachtwoord is zwak")


if __name__ == "__main__":
    main()