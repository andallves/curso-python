n = 3
matriz = []

for i in range(n):
    line = []
    for j in range(n):
        line.append(int(input('Informe um valor para linha {} e coluna {}: '
                              .format(i + 1, j + 1))))
    matriz.append(line)


def calculateMatriz(matriz: list):
    lines = []
    columns = []

    # soma das linhas
    sumLines = 0
    for i in range(n):
        sum = 0
        for j in range(n):
            sum += matriz[i][j]

        sumLines += sum
        lines.append(sum)

    # soma das colunas
    sumColumns = 0
    for j in range(n):
        sum = 0
        for i in range(n):
            sum += matriz[i][j]

        sumColumns += sum
        columns.append(sum)

    for i in range(n):
        print(matriz[i])

    print('A soma das linhas é {} e a linha com maior valor tem {}'
          .format(sumLines, max(lines)))
    print('A soma das colunas é {} e a coluna com maior valor tem {}'
          .format(sumColumns, max(columns)))


calculateMatriz(matriz)
