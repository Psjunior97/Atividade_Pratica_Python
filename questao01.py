#   Script 1 – Classificador de desempenho acadêmico
#   Crie um programa que solicite:
#       • nome do aluno;
#       • três notas;
#       • quantidade de faltas.
#   O programa deverá calcular a média e informar a situação:
#       • média ≥ 7 e faltas ≤ 10 → Aprovado;
#       • média entre 5 e 6,9 → Recuperação;
#       • média < 5 → Reprovado;
#       • mais de 10 faltas → Reprovado por falta.
#   Ao final, exiba nome, média e situação.

def media(nota1, nota2, nota3):
    return(nota1 + nota2 + nota3) / 3

print("--- Classificador de Desempenho Academico ---")
nome = input("Digite o nome do aluno: ")
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
faltas = int(input("Digite o número de faltas: "))


if media(nota1, nota2, nota3) >= 7 and faltas <= 10:
    situacao = "Aprovado"
elif media(nota1, nota2, nota3) >= 5 and media(nota1, nota2, nota3) < 7 and faltas <= 10:
    situacao = "Recuperação"
elif media(nota1, nota2, nota3) < 5:
    situacao = "Reprovado"
else:
    situacao = "Reprovado por faltas"    


print(f" Nome: {nome} ")
print(f" Média: {media(nota1, nota2, nota3):.2f} ")
print(f" Situação: {situacao} ")
