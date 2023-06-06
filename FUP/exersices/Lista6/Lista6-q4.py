"""
Dado o campeonato brasileiro de futebol, como exemplo da tabela seguinte,
implemente umaMATRIZ (12 x 7), com 12 times participantes e as informações
relacionadas (1- posição; 2 – time;3 – pontos; 4 – jogos; 5 – vitórias; 6 –
empates; 7 – derrotas), informadas pelo usuário, paramostrar o resultado
deste campeonato e os itens seguintes:

    a) O campeão brasileiro;
    b) Os 5 primeiros colocados que serão classificados para a libertadores
    da américa;
    c) Os 5 seguintes (de 6 a 10) que serão classificados para copa
    sul-américa;
    d) Os 2 últimos que serão rebaixados para a série B.
"""
serieA = []
line = 3
column = 7
columnHeader = ['a posição', 'o time', 'qtd de pontos', 'qtd de jogos',
                'qtd de vitórias', 'qtd de empates', 'qtd de derrotas']

for i in range(line):
    time = []
    for j in range(column):
        time.append(input('Informe {}: '.format(columnHeader[j])))
    serieA.append(time)
print('')
print('O campeão é o time {}'.format(serieA[0][1]))
print('')

i = 1
print('Os classificados para libertadores')
while i < 5:
    print('O {}º cologado foi o {}'.format(i, serieA[i-1][1]))
    i += 1
print('')

i = 1
print('Os classificados para a copa sul-américa')
while i > 4 and i > 10:
    print('O {}º colocado foi o {}'.format(i, serieA[i-1][1]))
    i += 1
print('')

i = 1
print('Os times que serão rebaixado para serie B')
while i > 9 and i < 12:
    print('O {}º colocado foi o {}'.format(i, serieA[i-1][1]))
    i += 1
