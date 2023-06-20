"""
# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida
o primeiro e o último nome separadamente.
    Ex: Ana Maria de Sousa
    - primeiro = Ana
    - último = Souza
"""

fullname = str(input('Digite seu nome completo: ')).strip()
fullnameArr = fullname.split()

print('O primeiro nome é: {}'.format(fullnameArr[0]))
print('O primeiro nome é: {}'.format(fullnameArr[len(fullnameArr) - 1]))
