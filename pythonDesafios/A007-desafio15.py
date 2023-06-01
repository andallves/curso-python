# Escreva um programa que pergunte a quantidade de Km percorridos por um
# alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço
# a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado

days = int(input('Quantos dias alugados? '))
km = float(input('Quantos Km rodados? '))
price = days * 60 + km * 0.15

print('O valor total a ser pago é R${:.2f}.'.format(price))
