"""
# Crie um program que leia o nome completo de uma pessoa e mostre:
    - O nome com todas as letras maiúsculas
    - O nome com todas as letras minúsculas
    - Quantas letras ao todo (sem considerar espaços)
    - Quantas letras tem o primerio nome
"""

name = input('Nome completo: ')
print('')

print('O nome com todas as letras maiúsculas: {}'.format(name.upper()))
print('O nome com todas as letras minusculas; {}'.format(name.lower()))

qtdLetras = name.strip().split()
qtdLettersFirstName = len(qtdLetras[1])
qtdLetras = ''.join(qtdLetras)
print('O nome {} tem {} letras ao todo'.format(name, len(qtdLetras)))
print('o primeiro nome tem {} letras'.format(qtdLettersFirstName))


