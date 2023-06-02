"""
Deseja-se atualizar as contas correntes dos clientes de uma agência bancária.
É dado o cadastro de 5 clientes contendo para cada um as seguintes informações:
o número da conta, nome, saldo e OP (pode ser C ou D).; implemente uma matriz
5 x 5 que mostre o movimento bancário de cada um desses cliente. Os dados são
fornecidos pelo usuário.
"""

msg = ['Informe seu nome: ', 'Nº da conta: ', 'Saldo: ',
       'Operação de Crédito: ', 'Operação de Débito: ']
allClients: list = []

for i in range(5):
    client = []

    for j in range(5):
        client.append(input('{}'.format(msg[j])))

    allClients.append(client)

for i in range(len(allClients)):
    print(allClients[i])
