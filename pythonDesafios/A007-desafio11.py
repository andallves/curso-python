# Faça um programa que leia a largura e a altura de uma parede em metros,
# calcule a quantidade de tinta necessária para pintá-la,
# sabendo que cada litro de tinta, pinta uma área de 2m².

width = float(input('Informe a largura da parede: '))
height = float(input('Informe a altura da parede: '))
area = width * height
tinta = area / 2

print('Sua parede tem a dimnsão de {} x {} e sua área é de {}m²'.
      format(width, height, area))
print('A quantidade de tinta necessario é {:.1f}L de tinta.'.format(tinta))
