#   Script 2 – Analisador de consumo mensal
#   Crie um programa que receba o consumo de energia elétrica de uma residência durante 6 meses.
#   O programa deverá:
#       • armazenar os valores em uma lista;
#       • calcular o consumo médio;
#       • informar o maior consumo;
#       • informar o menor consumo;
#       • contar quantos meses ficaram acima da média.
#   Desafio extra: informar a posição do mês de maior consumo.



consumo = []
for i in range(6):
    consumo.append(float(input(f"Digite o consumo do mês {i+1}: ")))

media = sum(consumo) / len(consumo)
maior = max(consumo)
menor = min(consumo)
acima_da_media = len([x for x in consumo if x > media])
#Transforma os itens da lista em X e compara com a média, contando quantos são maiores que a média.

print(f"Consumo médio: {media:.2f}")
print(f"Maior consumo: {maior}")
print(f"Menor consumo: {menor}")
print(f"Meses acima da média: {acima_da_media}")

# Desafio extra

#index() retorna a posição do primeiro elemento encontrado na lista, então somamos +1 para indicar o mês correto (1 a 6).
posicao_maior = consumo.index(maior) + 1
print(f"Posição do mês de maior consumo: {posicao_maior}")