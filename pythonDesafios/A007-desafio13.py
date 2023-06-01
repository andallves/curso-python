# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo
# salário, com 15% de aumento

salario = float(input('Informe o salário atual: R$'))
salarioComAumento = salario + (salario * 15 / 100)
print('O salario de {:.2f} com aumento de 15% ficou {:.2f}'
      .format(salario, salarioComAumento))
