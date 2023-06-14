print('Cédulas disponíveis para saque 2, 5, 10, 20, 50, 100, 200')
saque = int(input('Quanto deseja sacar? R$'))


def cedulasSaque(valor: int):
    if saque < 4:
        return print('Valor inválido! O valor precisar ser pelo menos R$ 4,00')

    total = valor
    cedula = [2, 5, 10, 20, 50, 100, 200]
    totalCedula = 0
    a = len(cedula) - 1

    while True:
        if total >= cedula[a]:
            total -= cedula[a]
            totalCedula += 1

        if total < cedula[a]:
            if totalCedula > 0:
                print(f'Total de {totalCedula} cédulas de R${cedula[a]}')
                totalCedula = 0
                a -= 1
            else:
                a -= 1
        if total == 0:
            break


cedulasSaque(saque)
