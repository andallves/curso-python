def calcularPagamento(qtdHoras, valorHoras):
    horas = float(qtdHoras)
    taxa = float(valorHoras)

    if horas <= 40:
        salario = horas * taxa
    else:
        horaExcd = horas - 40
        salario = 40 * taxa + (horaExcd * (1.5 * taxa))

    return salario


strHoras = input('Informe as horas: ')
strTaxa = input('Informe a taxa: ')
totalSalario = calcularPagamento(strHoras, strTaxa)
print('O valor de seus rendimentos é R$ {}'.format(totalSalario))
