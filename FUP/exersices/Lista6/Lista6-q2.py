"""
Deseja-se fazer a emissão da folha de pagamento de uma empresa. Para 4
funcionários de uma empresa são dadas as seguintes informações:
(matrícula, nome, função e salário). Implemente uma matriz 4 x 4 para emissão
dessas informações, depois mostre quem ganha o maior e o menor salário.
"""

fieldForm = ['Matrícula', 'Nome', 'Cargo', 'Salário']
employees = []

for i in range(2):
    employee = []

    print('Informe os seguintes dados')
    for j in range(4):
        employee.append(input('{}: '.format(fieldForm[j])))

    employees.append(employee)
    print('')

salary = []
for i in range(2):
    print('Informações do {}º funcionário: '.format(i))
    print('O/A funcionário(a) {} com matrícula {} exerce a funçao de {}'
          .format(employees[i][1], employees[i][0], employees[i][2]))
    print('e recebe {} por mês.'.format(employees[i][3]))
    print('')

    salary.append(float(employees[i][3]))

print('O maior salário recebido é {:.2f}.'.format(max(salary)))
print('O menor salário recebido é {:.2f}.'.format(min(salary)))
