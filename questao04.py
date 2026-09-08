#Script 4 – Cadastro e análise de produtos
#Crie um programa que permita cadastrar 5 produtos.
#Para cada produto, armazene:
#   • nome;
#   • preço;
#   • quantidade em estoque.
#Depois, o programa deverá mostrar:
#   • produto mais caro;
#   • produto mais barato;
#   • valor total do estoque de cada produto;
#   • valor total de todo o estoque.
#Utilize o cálculo:
#valor do estoque = preço × quantidade


produtos = []
for i in range(5):
    print(f"Cadastro do produto {i + 1}:")
    nome = input("Digite o nome do produto: ")
    preco = float(input("Digite o preço do produto: "))
    quantidade = int(input("Digite a quantidade em estoque: "))
    produtos.append({"nome": nome, "preco": preco, "quantidade": quantidade})

print("\nAnálise dos produtos cadastrados:")

mais_caro = produtos[0]
mais_barato = produtos[0]
soma_total_estoque = 0

for produto in produtos:
    if produto["preco"] > mais_caro["preco"]:
        mais_caro = produto
    if produto["preco"] < mais_barato["preco"]:
        mais_barato = produto
    
    soma_estoque = produto["preco"] * produto["quantidade"]
    print(f" - {produto['nome']}: R$ {produto['preco']:.2f} (estoque: {produto['quantidade']})")
    print(f"   Valor total do estoque: R$ {soma_estoque:.2f}")
    soma_total_estoque = soma_total_estoque + soma_estoque 




print(f"\nProduto mais caro: {mais_caro['nome']} - R$ {mais_caro['preco']:.2f}")
print(f"Produto mais barato: {mais_barato['nome']} - R$ {mais_barato['preco']:.2f}")
print(f"Valor total de todo o estoque: R$ {soma_total_estoque:.2f}")
