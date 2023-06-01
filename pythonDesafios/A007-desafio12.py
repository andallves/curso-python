# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, 
# com 5% de desconto.

price = float(input('Digite o preço atual: R$'))
desconto = (price * 5) / 100
newPrice = price - desconto
print('O produto custava R${:.2f}, com o desconto de 5% vai custar R${:.2f}'
      .format(price, newPrice))
