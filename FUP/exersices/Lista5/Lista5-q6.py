# Crie/Gerar um vetor de 10 posições randomicamente
# ler um valor e verificar se ele está no vetor gerado, mostrando sua posição

import random

array = []
hasNumber = False

for i in range(10):
    array.append(random.randint(1, 100))

numberSeek = int(input('Qual valor estas procurando? '))

for i in array:
    if i == numberSeek:
        hasNumber = True

if hasNumber:
    print('O número {} buscado foi encontrado e está na posição {}.'
          .format(numberSeek, array.index(numberSeek)))
else:
    print('O número que estas procurando não está no vetor')
