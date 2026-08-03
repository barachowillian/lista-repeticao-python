# Exercício 6 - Estatísticas de uma turma

quantidade = int(input("Quantidade de alunos: "))

soma = 0

for i in range(quantidade):
    nota = float(input(f"Nota do aluno {i + 1}: "))

    if i == 0:
        maior = nota
        menor = nota
    else:
        if nota > maior:
            maior = nota
        if nota < menor:
            menor = nota

    soma += nota

media = soma / quantidade

print(f"Maior nota: {maior}")
print(f"Menor nota: {menor}")
print(f"Média da turma: {media:.2f}")