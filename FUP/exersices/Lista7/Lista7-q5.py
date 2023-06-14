altura = float(input('Informe a altura: '))
peso = float(input('Informe o peso: '))


def calcularImc(altura: float, peso: float):
    imc = peso / altura ** 2

    if imc > 40:
        return print('OBESIDADE GRAVE - Grau III')
    if imc > 29.5:
        return print('OBESIDADE - Grau II')
    if imc > 24.9:
        return print('SOBREPESO - Grau I')
    if imc >= 18.5:
        return print('NORMAL - grau 0')
    if imc < 18.5:
        return print('MAGREZA - grau 0')


calcularImc(altura, peso)
