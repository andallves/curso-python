# Gerar/Criar um vetor de 10 posições, randomicamente,
# depois contar quantos pares e quanto ímpares existem no vetor
import random

array = []
even = 0
old = 0

for i in range(10):
    array.append(random.randint(1, 100))

for i in array:
    if i % 2 == 0:
        even += 1
    else:
        old += 1
print(array)
print('No vetor há {} números pares e {} número ímpares.'.format(even, old))
