"""
Faça uma função em python para gerar um vetor de 10 valores inteiros e informar
o maior valor deste, recursivamente.
"""
from random import randint


def generateVector(vect):
    if len(vect) == 10:
        return max(vect)

    vect.append(randint(1, 99))

    return generateVector(vect)


vect: list = []
print(generateVector(vect))
