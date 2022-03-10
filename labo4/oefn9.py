def omgekeerd_Zoeken(dictionary, waarde):
    result = []
    for key,value in dictionary.items():
        if value == waarde:
            result.append(key)

    return result

ik = {
    "naam": "Mohamed Saadi",
    "taal": "python",
    "leeftijd": 20
}

print(omgekeerd_Zoeken(ik,20))
