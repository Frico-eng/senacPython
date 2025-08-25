#Controle de Vendas em uma Loja
n_produtos = int(input("Insira o número de produtos vendidos no dia de hoje: "))


for i in range(n_produtos):
    nome_produto = input("Insira o nome do produto: ")
    preco_produto = float(input("Insira o preço do produto: "))
    if preco_produto<50:
        print(f"\n{nome_produto} é barato\n")
    elif preco_produto<=200:
        print(f"\n{nome_produto} tem preço médio\n")
    else:
        print(f"\n{nome_produto} é caro\n")
        
#Controle de Estacionamento
capacidade_maxima = int(input("Insira a capacidade máxima do estacionamento: "))
capacidade_atual = 0
movimentacoes = int(input("Insira o numero de movimentoações que serão simuladas: "))
while movimentacoes>0:
    print("opções:")
    print("E - Entrada")
    print("S - saída")
    operador = input("insira uma opção:")
    match operador:
        case "E":
            if capacidade_atual<capacidade_maxima:
                capacidade_atual += 1
                movimentacoes-=1
            else:
                print("Operação inválida, capacidade máxima excedida")
        case "S":
            if capacidade_atual>0:
                capacidade_atual -= 1
                movimentacoes-=1
            else:
                print("Operação inválida, capacidade máxima excedida")
        case _:
            print("operação invalida, tente novamente")
    print(f"Capacidade {capacidade_atual}/{capacidade_maxima}")
    
#Controle de Ingressos de Cinema
ingressos_vendidos = int(input("Insira a quantidade de ingressos vendidos: "))
infantil=0
adulto=0
idoso=0
for i in range(ingressos_vendidos):
    idade_cliente = int(input("Insira a sua idade: "))
    if idade_cliente<12:
        print("Ingresso infantil")
        infantil+=1
    elif idade_cliente<=59:
        print("Ingresso adulto")
        adulto+=1
    if idade_cliente>59:
        print("Ingresso idoso")
        idoso+=1
print("\nRelatório do dia:")
print(f"Ingressos infantis: {infantil}")
print(f"Ingressos para adultos: {adulto}")
print(f"Ingressos para idoso: {idoso}")