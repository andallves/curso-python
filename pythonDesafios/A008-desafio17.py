# Faça um program que leia o comprimento do cateto oposto e do cateto adjacente
# de um triângulo retãngulo, calcule e mostre o comprimento da hipotenusa

import math

opposite = float(input('Digite o comprimento do cateto oposto: '))
adjacent = float(input('Digite o comprimento do cateto adjacente: '))

# Essa é uma maneira usando calculo matemático
hypotenuse = math.sqrt(opposite ** 2 + adjacent ** 2)
print('O valor da hipotenusa é {:.2f}'.format(hypotenuse))

# Essa é uma maneira de calcular usando um metodo hypot da lib math
hypotenuse2 = math.hypot(opposite, adjacent)
print('O valor da hipotenusa é {:.2f}'.format(hypotenuse2))
