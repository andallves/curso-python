"""
# Faça um programa que leia uma frase pelo teclado e mostre:
    - Quantas vezes aparece a letra "A";
    - Em que posição ela aparece a primeira vez;
    - Em que posição ela aparece a última vez.
"""

phrase = input('Escreva um frase qualquer: ')
howMuchLettersA = phrase.upper().count('A')

phraseArr = phrase.strip().split()
phrase = ''.join(phraseArr)
positionFirstA = phrase.upper().find('A')

c = 0
for letter in phrase.upper():
    if letter == 'A':
        positionLastA = c
    c += 1

print('A letra "A" aparece {} vezes na frase.'.format(howMuchLettersA))
print('A primeira letra "A" aparece {}º na posição'.format(positionFirstA + 1))
print('A ultima letra "A" aparece {}º na posição'.format(positionLastA + 1))
