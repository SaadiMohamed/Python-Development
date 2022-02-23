from random import randint

def passwordGenerate():
    AantalKarakters = randint(7,10)
    Wachtwoord = ""
    for i in range(0,AantalKarakters):
        Wachtwoord = Wachtwoord + chr(randint(32,128))
    
    return Wachtwoord

if __name__ == "__main__":
    password = passwordGenerate()
    print(password)    

