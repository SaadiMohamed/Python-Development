from numpy import number


som = 0

for i in range(1,1000,1):
    if(i % 3 == 0 or i % 5 == 0):
        som = som + i

print(som)