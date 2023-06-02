# Crie um vetor de inteiro para armazenar a
# sequência de Fibonacci até a 20ª posição

fibonacci = []

next = 1
prev = 0

for i in range(20):
    fibonacci.append(next)
    next = next + prev
    prev = next - prev

print(fibonacci)
