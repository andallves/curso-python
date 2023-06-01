number1 = int(input('Digite um número: '))
number2 = float(input('Digite outro número: '))
sum = number1 + number2
print('A soma entre {} e {} vale {}'.format(number1, number2, sum))
print(type(number1), type(number2)) # o type serve para saber o tipo do valor

# Os tipos primitivos são (int, float, bool, str)

valueBoolean = bool(input('Digite um valor: ')) # Se tiver valor vai ser verdeiro, senão é falso
print(valueBoolean)

# METODOS PARA STRING (há metodos para cada tipo de dado)
n = input('Digite algo: ')
print(n.isnumeric()) # uma função para saber se o n é um númeroz
print(n.isalpha()) # uma função para saber se o n é uma letra
print(n.isalnum()) # uma função para saber se o n é um alpha numerico
