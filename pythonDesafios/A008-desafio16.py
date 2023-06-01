# Crie um programa que leia um número Real qualqeur pelo teclado e mostre 
# na tela a sua porção Inteira
from math import trunc

number = float(input('Digite um número real: '))
print('A porção inteira do número {} é {} - utilizando o trunc'
      .format(number, trunc(number)))

# outra forma que de pegar a porção inteira

print('A porção inteira do numero {} é {} - utilizando o int'
      .format(number, int(number)))
