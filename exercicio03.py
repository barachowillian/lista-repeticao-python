# Exercício 3 - Contador de vogais

texto = input("Digite uma palavra ou frase: ")

contador = 0
vogais = "aeiouAEIOU"

for letra in texto:
    if letra in vogais:
        contador += 1

print(f"Quantidade de vogais: {contador}")