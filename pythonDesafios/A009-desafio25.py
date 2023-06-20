"""
# Crie um programa que leia o nome de uma pessoa e diga se ela
tem "SILVA" no nome.
"""

name = str(input('Qual é o seu nome completo: ')).strip().lower()

hasSilva = name.find('silva')

if hasSilva != -1:
    print('Você tem Silva no seu nome')
else:
    print('Você não tem Silva no seu nome')

# uma outra forma de fazer é
# print('Seu nome tem Silva? {}'.format('silva' in name))
