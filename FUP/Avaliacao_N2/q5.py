import unidecode
msg = ['nome', 'nota', 'curso (“Computação”, “Informática”, “Redes”)',
       'situação (“Aprovado” e “Reprovado”)']
n = 2

matriz = []
for i in range(n):
    line = []
    for j in range(4):
        line.append(str(input('Informe o/a {}: '.format(msg[j]))).lower())
    matriz.append(line)

# mostrar a matriz preenchida
for i in range(n):
    print(matriz[i])

# média geral da turma
overall = 0.0
for i in range(n):
    overall += float(matriz[i][1])
overall = overall / n

print('A média geral do alunos é {:.2f}.'.format(overall))

# alunos de cada curso
cc = 0
inf = 0
re = 0
for i in range(n):
    curso = matriz[i][2]
    curso = unidecode.unidecode(curso)
    if curso == 'computacao':
        cc += 1
    elif curso == 'informatica':
        inf += 1
    else:
        re += 1

print('''O curso de Computação tem {} alunos, Informática tem {} alunos e Redes
      tem {} alunos.'''.format(cc, inf, re))

# alunos aprovados ou reprovados
aprov = 0
repro = 0
for i in range(n):
    situacao = matriz[i][3]
    if situacao == 'aprovado':
        aprov += 1
    else:
        repro += 1

print('Dentre os {} alunos, {:.1f}% dos alunos foram aprovados'
      .format(n, (aprov / n) * 100))
print('e {:.1f}% dos alunos foram reprovados'.format((repro / n) * 100))

# aluno com maior nota
maiorNota = 0.0
cursoAluno = ''
for i in range(n):
    notaAluno = float(matriz[i][1])
    if notaAluno * 10 > maiorNota * 10:
        maiorNota = notaAluno
        cursoAluno = matriz[i][2]

print('A maior nota foi {:.2f} e do curso de {}. '
      .format(maiorNota, cursoAluno))
