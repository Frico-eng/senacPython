#registrar chegada
#verificar lotação
#sair

capacidade_maxima = int(input("Insira a capacidade máxima do restaurante: "))
capacidade_atual = 0
while True:
    print("Opções")
    print("1. Registrar chegada de cliente")
    print("2. Verificar ocupação")
    print("3. Registrar saída de clientes")
    print("4. Sair")
    operador = input("Escolha uma opção: ")
    match operador:
        case "1":
            clientes = int(input("Informe a quantidade de clientes que chegaram: "))
            if clientes+ capacidade_atual<=capacidade_maxima:
                print(f"----------------------")
                print(f"operação bem sucessida")
                print(f"----------------------")
                capacidade_atual+=clientes
            else:
                print(f"--------------------------------------------")
                print("Não há mais vagas disponíveis,tente novamente")
                print(f"--------------------------------------------")
        case "2":
            print(f"------------------------")
            print(f"Ocupação autal: {capacidade_atual}/{capacidade_maxima}")
            print(f"------------------------")
        case "3":
            clientes = int(input("Informe a quantidade de clientes que sairam: "))
            
            if capacidade_atual-clientes>0:
                print(f"----------------------")
                print(f"operação bem sucessida")
                print(f"----------------------")
                capacidade_atual-=clientes
            else:
                print(f"-----------------------------------------------------------------------")
                print("impossível remover mais clientes do que estão presentes, tente novamente")
                print(f"-----------------------------------------------------------------------")
        case "4":
            break
        case _:
            print("Opção invalida, tente novamente")