"""
Faça uma função em python que leia uma matriz 3x3 de inteiros e retorne a soma
da diagonal desta matriz.
"""


def sumDiagonal(n):
    matriz = []
    for i in range(n):
        line = []
        for j in range(n):
            line.append(
                int(input('Digite um valor para a linha {} e coluna {}: '
                          .format(i+1, j+1))))
        matriz.append(line)

    # Soma da diagonal
    sum = 0
    for i in range(n):
        for j in range(n):
            if i == j:
                sum += matriz[i][j]

    return sum


sumDiagonal(3)
