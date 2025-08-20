#deprecated version using flag control
# flag = True
# tentativas = 3
# while flag:
#     senha = input("Insira a sua senha:\n")
#     if senha == "2002":
#         print("\nSenha correta, seja bem vindo\n")
#         flag = False
#     elif tentativas > 1:
#         tentativas = tentativas-1
#         print(f"\nSenha incorreta, você tem mais {tentativas} tentativas\n")
#     else:
#         print("\nSenha incorreta, sua conta foi bloqueada\n")
#         flag = False


senha_Correta = "senha"
tentativas = 3

while tentativas>0:
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