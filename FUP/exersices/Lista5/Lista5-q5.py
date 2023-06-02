# Preencher um vetor com números de 10 a 20
# mostrar os valores pares do vetor de trás para frente

array = []
evenArray = []

for i in range(10, 21):
    array.append(i)

for i in array:
    if i % 2 == 0:
        evenArray.append(i)

evenArray = sorted(evenArray, reverse=True)

print('O vetor original: {}'.format(array))
print('O vetor de pares reverso: {}'.format(evenArray))
