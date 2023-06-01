import random

# Criar uma lista com búmeros entre 10 e 50

#  gera uma lista e armazerna no vetor
vetor = list(range(10, 50))

print(vetor)

# Embaralha a lista de números
random.shuffle(vetor)
print('vetor embaralhado')
print(vetor)
