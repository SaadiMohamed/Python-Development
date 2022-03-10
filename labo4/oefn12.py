def checkAnnagram(woord1,woord2):
    letters1 = {}
    letters2 = {}
    for i in woord1:
        if i in letters1.keys():
            letters1[i] = letters1[i] +1
        else:
            letters1[i] = 1

    for i in woord2:
        if i in letters2.keys():
            letters2[i] = letters2[i] +1
        else:
            letters2[i] = 1

    if len(letters1) != len(letters2):
        return False

    for key,value in letters1.items():
        if key in letters2.keys():
            if letters1[key] != letters2[key]:
                return False
        else:
            return False
    return True


print(checkAnnagram("saadi","idaas"))