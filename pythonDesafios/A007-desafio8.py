# Escreva um programa que leia um valor em metros e o exiba convertido em 
# centimetros e milimetros

m = float(input('Digite um valor em m: '))

km = m / 1000
hm = m / 100
dam = m / 10
dm = m * 10
cm = m * 100
mm = m * 1000

print('O valor {}m é {:.3f}km'.format(m, km))
print('O valor {}m é {:.3f}hm'.format(m, hm))
print('O valor {}m é {:.3f}dam'.format(m, dam))
print('O valor {}m é {:.0f}dm'.format(m, dm))
print('O valor {}m é {:.0f}cm'.format(m, cm))
print('O valor {}m é {:.0f}mm'.format(m, mm))
