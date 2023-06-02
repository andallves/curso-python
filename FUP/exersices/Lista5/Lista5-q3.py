# Gerar um vetor de 10 elementos
# verifique quantos números primos existem no vetor

import random

array = []
primos = []


for i in range(10):
    array.append(random.randint(1, 100))
for num in array:
    count = 0

    for i in range(1, num + 1):
        if num % i == 0:
            count += 1

    if count <= 2:
        primos.append(num)

print(array)
print(primos)
