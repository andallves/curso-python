# Um professor quer sorter um dos seus quatro alunos para apagar o quadro.
# Faça um programa que ajude ele,
# lendo o nome deles e escrevendo o nome do escolhido
from random import choice

"""
n1 = str(input('Primeiro nome: '))
n2 = str(input('Segundo nome: '))
n3 = str(input('Terceiro nome: ))
n4 = str(input('Quarto nome: '))

list = [n1, n2, n3, n4]
choosen = random.choice(list)
print('O aluno escolhido foi {}'.format(choosen))
"""

students = []

for i in range(4):
    studentName = input('Digite o nome do {}º aluno: '.format(i + 1))
    students.append(studentName)

print('O aluno sorteado para apagar o quadrado é {}.'
      .format(choice(students)))
