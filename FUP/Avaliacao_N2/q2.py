"""
Faça uma função recursiva para calcular e apresentar o somatório dos números
pares (intervalo de 1 a 20);
(1, 5 pt);
"""


def sumEvens(n):
    if n == 2:
        return 2
    if n % 2 == 0:
        return n + sumEvens(n - 1)
    return sumEvens(n - 1)


print(sumEvens(20))
