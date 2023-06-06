"""
Dizemos que uma matriz quadrada inteira é um quadrado mágico se a soma dos
elementos de cada linha, a soma dos elementos de cada coluna e a soma dos
elementos das diagonais principal e secundária são todas iguais.

Implemente uma matriz quadrada (quadrado mágico), insira valores aleatórios e,
depois, mostre a mensagem “É uma matriz QUADRADO MÁGICO” ou “NÃO é uma matriz
QUADRADO MÁGICO” e os seus valores. 762
"""
n = 3
matriz = []

for i in range(n):
    line = []
    for j in range(n):
        line.append(int(input('Informe um nº: ')))
    matriz.append(line)

lista = []

# soma das linhas
for i in range(n):
    sum = 0
    for j in range(n):
        sum += matriz[i][j]
    lista.append(sum)

# soma das colunas
for j in range(n):
    sum = 0
    for i in range(n):
        sum += matriz[i][j]
    lista.append(sum)

# soma da diagonal principal
sum = 0
for i in range(n):
    sum += matriz[i][i]
lista.append(sum)

# soma da diagonal secundaria
sum = 0
i = 0
j = 2
while i < n:
    sum += matriz[i][j]
    i += 1
    j -= 1
lista.append(sum)

magico = True
index = 1

while magico and index < len(lista):
    if lista[index] != lista[0]:
        magico = False
    index += 1

if magico:
    print('É uma matriz QUADRADO MÁGICO')
else:
    print('NÃO é uma matriz QUADRADO MÁGICO')
