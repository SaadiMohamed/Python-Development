import random

lottoNumbers = []

while (len(lottoNumbers) != 6):
    NieuweGetal = random.randint(1,49)
    if(NieuweGetal in lottoNumbers):
        continue
    else:
        lottoNumbers.append(NieuweGetal)

print(lottoNumbers)