
from unittest import result


def Scrabble(woord):
    alfabet = "abcdefghijklmnopqrstuvwxyz"
    punten = [1,3,5,2,1,4,3,4,1,4,3,3,3,1,1,3,10,2,2,2,4,4,5,8,8,4]
    scores = {}
    for i in range(0,len(alfabet),1):
        scores[alfabet[i]] = punten[i]

    result = 0

    for i in woord:
        result = result + scores[i]
    
    return result


print(Scrabble("saadi"))
