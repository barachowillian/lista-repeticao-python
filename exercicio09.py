# Exercício 9 - Média dos valores digitados

contador = 0
soma = 0

while True:
    numero = float(input("Digite um número (-1 para encerrar): "))

    if numero == -1:
        break

    soma += numero
    contador += 1

if contador > 0:
    media = soma / contador
else:
    media = 0

print(f"Quantidade de números: {contador}")
print(f"Soma: {soma}")
print(f"Média: {media:.2f}")