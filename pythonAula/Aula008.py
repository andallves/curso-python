# Utilizando Módulos

# Para adicionar uma lib ao programa eu utilizo o comando 'import nomedomodulo'
# import nomedomodulo

# Caso eu queira importar apenas uma funcionalidade de um módulo eu posso usar
# o seguinte comando

# from nomedomodulo import funcionalidade

import math
import random
import emoji

num = int(input('Digite um número: '))

raiz = math.sqrt(num)  # a metodo sqrt calcula a raíz quadrada
print('A raíz quadrada do {} é {:.2f}'.format(num, math.ceil(raiz)))
# o metodo ceil arredonda o número pra cima
print('A raíz quadrada do {} é {:.2f}'.format(num, math.floor(raiz)))
# o metodo floor arredonda o número pra baixo

fatorial = math.factorial(num)  # o metodo factorial calcula o fatorial rsrs

# ou posso importar so metodo

# from math import sqrt, floor
# raiz = sqrt(num) -> essa seria a forma importando o metodo diretamente
# print('A raíz quadrada do {} é {:.2f}'.format(num, floor(raiz)))

num2 = random.randint(1, 10)
print(num2)

print(emoji.demojize('Olá, mundo :sunglasses:', use_aliases=True))
