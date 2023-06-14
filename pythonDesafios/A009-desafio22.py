"""
# Crie um program que leia o nome completo de uma pessoa e mostre:
    - O nome com todas as letras maiúsculas
    - O nome com todas as letras minúsculas
    - Quantas letras ao todo (sem considerar espaços)
    - Quantas letras tem o primerio nome
"""

name = str(input('Nome completo: ')).strip()

print('O nome em maiúsculas: {}'.format(name.upper()))
print('O nome em minusculas: {}'.format(name.lower()))
print('O nome tem {} letras ao todo'.format(len(name) - name.count(' ')))
#  print('Seu primeiro nome tem {} letras'.format(name.find(' ')))
splitName = name.split()
print('O primeiro {} tem {} letras'.format(splitName[0], len(splitName[0])))
