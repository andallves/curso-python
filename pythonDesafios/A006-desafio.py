n = input('Digite algo: ')
print('O que você digitou é um número: {}'.format(n.isnumeric()))
print('O que você digitou é uma letra: {}'.format(n.isalpha()))
print('O que você digitou é uma letra e um número: {}'.format(n.isalnum()))
