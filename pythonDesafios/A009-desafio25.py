"""
# Crie um programa que leia o nome de uma pessoa e diga se ela
tem "SILVA" no nome.
"""

name = input('Qual é o seu nome: ')

hasSilva = name.lower().find('silva')

if hasSilva != -1:
    print('Você tem Silva no seu nome')
else:
    print('Você não tem Silva no seu nome')
