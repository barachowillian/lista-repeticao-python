# Exercício 7 - Caixa eletrônico

valor = int(input("Digite o valor: "))

cedulas = [100, 50, 20, 10, 5, 2, 1]

for cedula in cedulas:
    quantidade = valor // cedula
    valor %= cedula
    print(f"R${cedula}: {quantidade} cédula(s)")