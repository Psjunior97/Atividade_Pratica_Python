#Script 3 – Sistema de autenticação simples
#Crie um programa com usuário e senha previamente definidos no código. Exemplo:
#usuario_correto = "admin"
#senha_correta = "python123"
#O usuário terá no máximo 3 tentativas para realizar o login.
#Atividade Prática – Python
#O programa deverá:
#• permitir até três tentativas;
#• informar quando usuário ou senha estiverem incorretos;
#• liberar o acesso se os dados estiverem corretos;
#• bloquear o acesso após três erros.
#Não utilize bibliotecas externas.


usuario_correto = "admin"
senha_correta = "python123"


for tentativa in range(3):
    print(f"Tentativa {tentativa + 1} de 3")
    usuario = input("Digite o usuário: ")
    senha = input("Digite a senha: ")

    if usuario == usuario_correto and senha == senha_correta:
        print("Acesso liberado!")
        break
    # posição 2 corresponde à terceira tentativa, pois o range começa em 0.
    elif tentativa < 2:
        print("Usuário ou senha incorretos.")
    else:
        print("Acesso bloqueado por excesso de tentativas.")