#Script 5 – Função para análise de senhas
#Crie uma função chamada:
#validar_senha()
#A função deverá receber uma senha e verificar se ela possui:
#   • pelo menos 8 caracteres;
#   • pelo menos uma letra;
#   • pelo menos um número;
#   • pelo menos um caractere especial.
#O programa deverá informar se a senha é Forte ou Fraca. Caso seja fraca, deverá informar quais 
#requisitos não foram atendidos.



def validar_senha(senha):
    # Verificar se a senha possui pelo menos 8 caracteres
    if len(senha) < 8:
        return False, ["Senha deve ter pelo menos 8 caracteres"]

    # Verificar se a senha possui pelo menos uma letra
    #A variável c significa simplesmente caractere.
    #isalpha() verifica se o caractere é uma letra.
    #any() retorna True se pelo menos um dos elementos do iterável for verdadeiro.
    #not any() retorna True se todos os elementos do iterável forem falsos.
    if not any(c.isalpha() for c in senha):
        return False, ["Senha deve conter pelo menos uma letra"]

    # Verificar se a senha possui pelo menos um número
    #isdigit() verifica se o caractere é um dígito.
    if not any(c.isdigit() for c in senha):
        return False, ["Senha deve conter pelo menos um número"]

    # Verificar se a senha possui pelo menos um caractere especial
    caracteres_especiais = "!@#$%^&*()-+"
    #in verifica se o caractere está presente na string de caracteres especiais.
    if not any(c in caracteres_especiais for c in senha):
        return False, ["Senha deve conter pelo menos um caractere especial"]

    return True, ["Senha é forte"]

print("Análise de senhas")
senha = input("Digite a senha para análise: ")
print("\nResultado da análise:")
print(f"Senha: {validar_senha(senha)}")