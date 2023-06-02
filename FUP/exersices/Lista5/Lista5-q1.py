import random
# Gerar um vetor aleatório de 10 posições
# em seguida ordená-lo de forma crescente e,
# depois, decrescente

array = []

for i in range(10):
    array.append(random.randint(1, 100))

crescent = sorted(array)
decrescent = sorted(array, reverse=True)

print(crescent)
print(decrescent)
