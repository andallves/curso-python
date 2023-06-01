# Operadores Aritméticos

# Ordem de precedência
# '()' indica prioridade na operação
# '**' Potência
# '*' Multiplicação | '/' Divisão | '//' Divisão Inteira | '%' Resto da divisão
# '-' Subtração | '+' Adição
# '==' verifcar igualdade

ex1 = 5 + 3 * 2
print(ex1) # 11

ex2 = 3 * 5 + 4 ** 2
print(ex2) # 31

ex3 = 3 * (5 + 4) ** 2
print(ex3) # 243

name = input('Qual é o seu nome? ')
print('Prazer em te conhecer {:=^20}!'.format(name)) #':20' indica que será 20 caracteres e o '>' indica o alinhamento ou '^' para ficar centralizado

n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor:'))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
r = n1 % n2

print('A soma é {}, a multiplicação é {}, a divisão é {:.3f}'.format(s, m, d), end=' ') # ':.3f' indica a quantidade de casas decimais, o 'end=' '' e para não quebrar a linha
print('A divisão inteira é {},\n e exponecição é {}\n e o resto da divisão é {}'.format(di, e, r)) # o '\n' é para quebrar a linha

