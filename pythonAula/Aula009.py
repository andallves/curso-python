#  Text Manipulation

phrase = 'Andre Alves Pereira'

# ========== Fatiamento ==========
# Podemos pegar apenas uma letra utilizando o indice
# pega a letra que está no indice 9
print(phrase[9])

# pega a parte do texto que inicia na posição 6 até o 11(N-1)
print(phrase[6:11])

# pega a parte do texto que inicia no indice 6 vai até o indice 18 pulando
# de dois em dois
print(phrase[6:19:2])

# omitindo o valor inicial, então ele inicia do indice 0, no caso ele vai
# iniciar do 0 e vai até o 5
print(phrase[:5])

# omitindo o valor final, então ele inicia no 12 e vai até o final
print(phrase[12:])

# vai pegar do indice 6 até o final, pulando de 3 em 3
print(phrase[6::3])


# ========== Análise ==========
# retorna o tamanho da string na variavel
print(len(phrase))

# retorna quantas letras 'e' há na string
print(phrase.count('e'))

# retorna quantas letras 'e' tem no fatiamento do indice 0 até 12
print(phrase.count('e', 0, 12))

# retorna quantas vezes essa parte foi encontrada e onde que começa
print(phrase.find('re'))

# retorna um valor -1 quando não encontra a string desejada
print(phrase.find('lucas'))

# retorna um valor booleano true se encontrar o valor deseja
# ou false senão encontrar
print('Andre' in phrase)


# ========== Transformação ==========

# o método replace substitui todos os 'e' encontrados por 'E'
print(phrase.replace('e', 'E'))

# o método upper deixa toda a string em maiuscula
print(phrase.upper())

# o método lower deixa toda a string em minuscula
print(phrase.lower())

# o método capitalize deixa somente a primeira letra da frase em maiuscala
print(phrase.capitalize())

# o método title deixa a primeira letra de cada palavra em maiuscula
print(phrase.title())

test = '  usando o strip  '
# o método strip remove todos os espaços inuteis no inicio e no fim
print(test.strip())

# se adicionar o r no strip (rstrip) ele vai remover o espaço do lado direito
print(test.rstrip())

# de forma similar se eu adicionar o l no strip (lstrip) ele vai remover
# o espaço do lado esquerdo
print(test.lstrip())

# ========== Divisão ==========

# o método split por default divide a palavra nos espaços
dividido = phrase.split()
print(dividido)

# ========== Junção ==========

# o método join é utilizado para juntar palavras
print('-'.join(dividido))

# 3 aspas dupla são usadas para string em varias linhas
# ou multiplos comentários
print("""Welcome! Are you completely new to programming?
about why and how to get started with Python. Fortunately
an experienced programmer in any programming language
(whatever it may be) ca pick up Python very quickly.
Its also ease for beginners to use and learn, so jump in!""")

# posso juntar os métodos
print(phrase.upper().count('A'))

# usando o método len para saber quantos caracteres há no phrase
print(len(phrase))

"""
============ DESAFIOS ============
# Crie um program que leia o nome completo de uma pessoa e mostre:
    - O nome com todas as letras maiúsculas
    - O nome com todas as letras minúsculas
    - Quantas letras ao todo (sem considerar espaços)
    - Quantas letras tem o primerio nome

# Faça um program que leia um número de 0 a 9999 e mostre na tela cada um dos
digitos separados.
    Ex:
    - Digite um número: 1834
    - unidade: 4
    - dezena: 3
    - centena: 8
    - milhar: 1

# Crie um programa que leia o nome de uma cidade e diga se ela começa
ou não com o nome "SANTO".

# Crie um programa que leia o nome de uma pessoa e diga se ela
tem "SILVA" no nome.

# Faça um programa que leia uma frase pelo teclado e mostre:
    - Quantas vezes aparece a letra "A";
    - Em que posição ela aparece a primeira vez;
    - Em que posição ela aparece a última vez.

# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida
o primeiro e o último nome separadamente.
    Ex: Ana Maria de Sousa
    - primeiro = Ana
    - último = Souza
"""
