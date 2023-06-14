"""
# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos
digitos separados.
    Ex:
    - Digite um número: 1834
    - unidade: 4
    - dezena: 3
    - centena: 8
    - milhar: 1
"""

number = int(input('Digite um número entre 0 e 9999: '))

u = number // 1 % 10
d = number // 10 % 10
c = number // 100 % 10
m = number // 1000 % 10

print('Analisando o número {}'.format(number))
print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))

#  Código mais avançado utilizando for
# unidades = ['unidade', 'dezena', 'centena', 'milhar']

# numbers = []
# for num in number:
#     numbers.append(int(num))

# numbers.reverse()
# for i in range(len(numbers)):
#     print('-> {}: {}'.format(unidades[i], numbers[i]))
