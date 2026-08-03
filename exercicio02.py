# Exercício 2 - Soma dos números pares

n = int(input("Digite um número inteiro positivo: "))

soma = 0

for i in range(2, n + 1, 2):
    soma += i

print(f"Soma dos números pares: {soma}")