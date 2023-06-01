# Crie um algoritmo que leia um núemro e mostre o seu dobro, 
# triplo e raiz quadrada.

number = int(input('Digite um número: '))
print('O dobro do {} é {}'.format(number, number * 2))
print('O triplo do {} é {}'.format(number, number * 3))
print('A raíz quadrada do {} é {:.2f}'.format(number, number**(1/2)))

# utilizando o pow() para calcular a raíz quadrada
print('A raíz quadrada de {} é {:.2f}.'.format(number, pow(number, (1/2))))
