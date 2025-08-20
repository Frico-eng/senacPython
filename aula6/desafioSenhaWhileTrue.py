senha_Correta = "2002"
tentativas = 3

while True:
    if tentativas>0:
        senha = input("Insira a sua senha:\n")
        if senha==senha_Correta:
            print("Acesso concedido, seja bem vindo!")
            break
        elif tentativas>1:
            tentativas=tentativas-1
            print(f"Senha incorreta você tem mais {tentativas} tentativas")
        else:
            print("Limite de tentativas, sua conta foi bloqueada")
            break