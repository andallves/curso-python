# O mesmo professor do desafio anterior quer sortear a ordem de apresentação
# de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos
# e mostre a ordem sorteada.

from random import shuffle

"""
n1 = str(input('Primeiro aluno: ))
n2 = str(input('Segundo aluno: ))
n3 = str(input('Terceiro aluno: ))
n4 = str(input('Quarto aluno: ))
list = [n1, n2, n3, n4]

shuffle(list)
print('A ordem de apresentaçaõ será')
print(list)
"""
students = []

for i in range(4):
    studentName = str(input('Informe o nome do {}º aluno: '.format(i + 1)))
    students.append(studentName)

orderApresention = shuffle(students)
print('A ordem de apresentação será')
print(students)
