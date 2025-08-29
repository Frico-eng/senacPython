import random

def gera_num():
    return random.randint(1, 10)

def verifica(chute, resposta):
    if chute == resposta:
        return True
    if chute > resposta:
        print("Menor")
    else:
        print("Maior")
    return False


def adivinha(tentativas, resposta):
    tentativa = 0
    while tentativa < tentativas:
        try:
            chute = int(input(f"Insira um número você tem {5-tentativa} tentativas: "))
            if verifica(chute, resposta):  # se acertou, para o loop
                print(f"Resposta correta, você acertou em {tentativa+1} tentativas")
                break
            tentativa += 1
        except ValueError:
            print("Valor inválido, tente novamente")
    else:  # só roda se esgotar todas as tentativas
        print(f"Você perdeu! A resposta era {resposta}")

        

def main():
    adivinha(tentativas=5, resposta=gera_num())

main()
