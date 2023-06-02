# Gerar/Criar um vetor de 10 posições, randomicamente, depois
# contar quando valores repetios existem no vetor gerado, imprimindo-os
import random

array = []

for i in range(10):
    array.append(random.randint(1, 100))

print(array)

for i, elemento in enumerate(array):
    if elemento in array[i+1:]:
        print(f'Elemento repetido: {elemento}')

    else:
        print('Não há elementos repetidos.')
