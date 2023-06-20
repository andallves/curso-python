"""
Faça uma função em python para ler um valor n qualquer e, em seguida, calcular
e informar a função exponencial (2n) deste valor, recursivamente.
"""


def exponential(n):
    if n == 0:
        return 1
    return 2 * exponential(n - 1)


number = int(input('Digite um número qualquer: '))
exponential(number)
