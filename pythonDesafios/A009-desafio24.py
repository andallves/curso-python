"""
# Crie um programa que leia o nome de uma cidade e diga se ela começa
ou não com o nome "SANTO".
"""

name = input('Qual é o seu nome: ')

hasSanto = name.lower().find('santo')

if hasSanto != -1 and hasSanto == 0:
    print('Seu nome começa com Santo')
else:
    print('Seu nome não começa com Santo')
