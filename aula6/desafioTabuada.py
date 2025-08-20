tabuada = 10
while True:
    n = int(input("Insira um número para tabuada:"))
    if n>0:
        for i in range(1,tabuada+1):
            print(f"{n}*{i} = {n*i} ")
    elif n==0:
        print("zero * qualquer coisa é zero")
    elif n<0:
        print("número negativo não suportado na versão atual, tente novamente")
    else:
        break