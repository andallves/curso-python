# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre
# quantos Dólares ela pode comprar.

money = int(input('Quanto de dinheiro tens na carteira? R$'))
dolar = money / 3.27
print('Com R${:.2f} você pode comprar até $ {:.2f} dólares'
      .format(money, dolar))
