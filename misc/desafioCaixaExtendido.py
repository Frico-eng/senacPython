saldo = 1000
flag = True
while flag:
    print('------------------')
    print("1 - Checar saldo|")
    print("2 - Saque       |")
    print("3 - Deposito    |")
    print("4 - Sair        |")
    print('-----------------')
    operador = int(input("insira a operação desejada:"))
    match operador:
        case 1:
            print(f"\n\nO seu saldo é de R${saldo}\n\n")
        case 2:       
            saque = float(input("Insira o valor do saque em reais: "))
            if saque>saldo:
                print("\n\nNão foi possível sacar mais do que o seu saldo, tente novamente\n\n")
            elif (saldo-saque)<10:
                print("\n\nNão foi possível sacar, voçê precisa manter pelo menos R$10 na sua conta, tente novamente\n\n")
            else:
                saldo = saldo-saque
                print(f"\n\nSaque realizado com sucesso, novo saldo de R${saldo:.2f}\n\n")
                
        case 3:
            deposito = float(input("Insira o quanto desejas depositar em reais: "))
            saldo += deposito
            print(f"\n\Deposito realizado com sucesso, novo saldo de R${saldo:.2f}\n\n")
        case 4:
            flag = False
        case _:
            print("\n------------------------------------------")
            print("Opção incorreta, por favor tente novamente")
            print("------------------------------------------\n")