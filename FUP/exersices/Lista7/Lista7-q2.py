nota = int(input('Informe a nota do aluno: '))


def conceitoAprovacao(nota):
    if nota >= 9:
        return 'A'
    if nota >= 7:
        return 'B'
    if nota >= 5:
        return 'C'
    else:
        return 'D'


conceito = conceitoAprovacao(nota)

if conceito != 'D' and conceito != 'C':
    print('Aluno aprovado com conceito "{}"'.format(conceito))
if conceito != 'A' and conceito != 'B':
    print('Conceito: {}'.format(conceito))
