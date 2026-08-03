# Exercício 10 - Desenhando um quadrado

n = int(input("Digite o tamanho do quadrado: "))

for i in range(n):
    for j in range(n):
        print("*", end="")
    print()