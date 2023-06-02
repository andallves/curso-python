# Preencher um primeiro vetor com o quadrado dos números pares
# do intervalo 2 a 20
# Preencher um segundo vetor com os números de 10 a 19.
# Mostrar a soma dos dois vetores.

array1 = []
array2 = []
sum = []

for i in range(2, 21):
    if i % 2 == 0:
        array1.append(i**2)

    if (i >= 10) and (i <= 19):
        array2.append(i)

for i in range(array1.__len__()):
    sum.append((array1[i] + array2[i]))

print(sum)
