"""
Deseja-se atualizar as contas correntes dos clientes de uma agência bancária.
É dado o cadastro de 5 clientes contendo para cada um as seguintes informações:
o número da conta, nome, saldo e OP (pode ser C ou D).; implemente uma matriz
5 x 5 que mostre o movimento bancário de cada um desses cliente. Os dados são
fornecidos pelo usuário.
"""
from random import randint

msg = ['nome: ', 'Nº da conta: ', 'Saldo: ',
       'operação de Crédito: ', 'operação de Débito: ']
allClients = []

for i in range(1):
    client = []
    credit = randint(0, 1000)

    for j in range(5):
        if j <= 2:
            client.append(input('Infome o/a {}'.format(msg[j])))
        elif j == 3:
            client.append(str(credit))
        elif j == 4:
            client.append(str(int(client[2]) + credit))

    allClients.append(client)
    print('')

for i in range(len(allClients)):
    print('INFORMAÇÕES DO CLIENTE')
    print('Cliente {} com Nº de conta {} tem um saldo de R${},00.'
          .format(allClients[i][0], allClients[i][1], allClients[i][2]))
    print('Com total de R${},00 para crédito e de R${},00 para débito'
          .format(allClients[i][3], allClients[i][4]))
    print('')
