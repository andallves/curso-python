from datetime import datetime, date

# recebendo data
dataInformada = input('Informe uma data "ex: 12 de junho de 2010": ')
data = dataInformada.split()

# pegar elementos separados
diaInformado = int(data[0])
mesNome = data[2]
anoInformado = int(data[4])

meses = ['janeiro', 'fevereiro', 'marco', 'abril', 'maio', 'junho',
         'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro']
for i in range(len(meses)):
    if meses[i] == mesNome:
        mesInformado = i + 1

dataAtual = date.today()

diaAtual = dataAtual.day
mesAtual = dataAtual.month
anoAtual = dataAtual.year

t1 = datetime(year=anoAtual, month=mesAtual, day=diaAtual)
t2 = datetime(year=anoInformado, month=mesInformado, day=diaInformado)
t3 = t1 - t2

print('A diferença de dias entre a data informada e a data de hoje são de {}'
      .format(t3))
