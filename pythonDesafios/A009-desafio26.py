"""
# Faça um programa que leia uma frase pelo teclado e mostre:
    - Quantas vezes aparece a letra "A";
    - Em que posição ela aparece a primeira vez;
    - Em que posição ela aparece a última vez.
"""

phrase = str(input('Escreva um frase qualquer: ')).strip().upper()
howMuchLettersA = phrase.count('A')
positionFirstA = phrase.find('A') + 1
positionLastA = phrase.rfind('A') + 1

print('A letra "A" aparece {} vezes na frase.'.format(howMuchLettersA))
print('A primeira letra "A" aparece na {}ª posição'.format(positionFirstA))
print('A ultima letra "A" aparece na {}ª posição'.format(positionLastA))
