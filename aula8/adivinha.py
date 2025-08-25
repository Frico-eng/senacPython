import random

def gerar_num():
    return random.randint(1,10)

def jogo_advinha():  
    tentativas = 1
    numero = gerar_num()
    while tentativas<=3:
        chute = int(input(f"Advinhe o número você tem {4-tentativas} tentativas: "))
        if chute>numero:
            print("Resposta errada, o número é menor")
            tentativas+=1
        elif chute<numero:
            print("Resposta errada, o número é maior")
            tentativas+=1
        else:
            if tentativas==1:
                print(f"Parabéns, você acertou com {tentativas} tentativa")
            else:
                print(f"Parabéns, você acertou com {tentativas} tentativas")
            
            break
    if tentativas==4:
        print(f"Você esgotou o número de tentativas, o número era {numero}, mais sorte na próxima")
    
jogo_advinha()