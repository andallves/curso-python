"""
# Crie um programa que leia o nome de uma cidade e diga se ela começa
ou não com o nome "SANTO".
"""

name = str(input('Em que cidade você nasceu? ')).strip().lower()

hasSanto = name.find('santo')

if hasSanto != -1 and hasSanto == 0:
    print('Começa com Santo')
else:
    print('Não começa com Santo')
