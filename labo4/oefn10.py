import random

def SimuleerWorp():
    worp1 = random.randint(1,6)
    worp2 = random.randint(1,6)
    return worp1 + worp2

aantalWorpen = {}

for i in range(2,13,1):
     aantalWorpen[i] = 0

for i in range(0,1001):
    aantalWorpen[SimuleerWorp()] = aantalWorpen[SimuleerWorp()] + 1
print(aantalWorpen)


print("Totaal\tgesimuleerde percentage " )

for key,value in aantalWorpen.items():
    print(f"{key}\t{value/10}%")
