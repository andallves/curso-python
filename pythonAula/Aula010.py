# CONDIÇÕES -> Simples e Compostas

time = int(input('Quantos anos tem seu carro? '))
if time <= 3:
    print('carro novo')
else:
    print('carro velho')

# condição simplificada
print('carro novo' if time <= 3 else 'carro velho')

# =====================
name = str(input('Qual é seu nome? '))
if name == 'Andre':
    print('É um lindo nome')
else:
    print('é um nome bem comum')
print('Boa noite, {}!'.format(name))

# ======================
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2) / 2
print('A sua média foi {:.1f}'.format(m))
if m >= 7.0:
    print('Sua média foi boa! PARABÉNS!')
else:
    print('Sua média foi ruim! ESTUDE MAIS!')

print('PARABÉNS' if m >= 6 else 'REPROVADO!')

"""
DESAFIOS

Escreva um programa que faça o computador 'pensar' em um número interio entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
O programa deverá escrever na tela se o usuário venceu ou pedrdeu.

Escreva um programa que leia a velocidade de um carro. Se ele ultrapassaar 80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.

Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR

Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por km para viagens de até 200Km e R$0,45 para viagens mais longas.

Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO.

Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a 1.250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.

Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não forma um triângulo.
"""
