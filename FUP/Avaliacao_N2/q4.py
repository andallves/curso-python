"""
Faça uma função para receber um número N qualquer e, em seguida, retornar a
sua representação em binário; (1, 5 pt);
"""


def convertNumber(n):
    numberBi = format(n, 'b')

    return numberBi


print(convertNumber(8))
