"""
1. Escreva uma função recursiva em python para mostrar a série fibonacci até
o 12º. termo.
"""


def fibonacci(n):
    if n <= 1:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)


for i in range(12):
    print(fibonacci(i))
