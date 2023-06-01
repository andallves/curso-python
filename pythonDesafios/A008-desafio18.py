# Faça um program que leia um ângulo qualquer e mostre na tela o valor de seno,
# cosseno e tangente desse ãngulo

from math import sin, cos, tan, radians

angle = float(input('Informe um ângulo que você deseja: '))
seno = sin(radians(angle))
cosseno = cos(radians(angle))
tagente = tan(radians(angle))

print('O ângulo de {} tem o SENO de {:.2f}'.format(angle, seno))
print('O ângulo de {} tem o COSSENO de {:.2f}'.format(angle, cosseno))
print('O ângulo de {} tem a TANGENTE de {:.2f}'.format(angle, tagente))
