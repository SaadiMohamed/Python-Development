from oefn10 import passwordGenerate
from oefn11 import passwordCheck


def main():
    sterkewachtwoord = False
    AantalProberen = 0
    while (sterkewachtwoord == False):
        AantalProberen = AantalProberen + 1
        sterkewachtwoord = passwordCheck(passwordGenerate())
    
    print(f"Je had {AantalProberen} keer nodig om een sterk wachtwoord te hebben")


if __name__ == "__main__":
    main()