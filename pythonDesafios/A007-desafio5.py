# Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor.

number = int(input('Digite um número: '))
print('Analisando o {} o antecessor é {} e o sucessor é {}.'
      .format(number, (number - 1), (number + 1)))
