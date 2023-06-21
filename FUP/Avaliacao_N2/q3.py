"""
Faça uma função para calcular e apresentar os múltiplos de 3
(intervalo de 3 a 30) em um vetor; (1, 5 pt);
"""


def multipleThree(n):
    vect = []
    for i in range(3, n+1):
        if i % 3 == 0:
            vect.append(i)

    return vect


print(multipleThree(30))
