def formata_string(resultado):
    print(f"Resultado da operação: {resultado}")
def soma_calc(a,b):
    return (a+b)
def sub_calc(a,b):
    return (a-b)
def mult_calc(a,b):
    return (a*b)
def div_calc(a,b):
    if b==0:
        print("Operação invalida - divisão por 0")
    else:
        return(a/b)
def calculadora():
    while True:
        print("Opções:")
        print("1 - Soma")
        print("2 - Subtração")
        print("3 - Multiplicação")
        print("4 - Divisão")
        print("5 - Sair")
        operador = input("Escolha uma opção: ")
        match operador:
            case "1":
                a = int(input("Insira o primeiro número da soma: "))
                b = int(input("Insira o segundo número da soma: "))
                resultado =soma_calc(a,b)
                formata_string(resultado)
            case "2":
                a = int(input("Insira o primeiro número da subtração: "))
                b = int(input("Insira o segundo número da subtração: "))
                resultado =sub_calc(a,b)
                formata_string(resultado)
            case "3":
                a = int(input("Insira o primeiro número da multiplicação: "))
                b = int(input("Insira o segundo número da multiplicação: "))
                resultado =mult_calc(a,b)
                formata_string(resultado)
            case "4":
                a = int(input("Insira o primeiro número da divisão: "))
                b = int(input("Insira o segundo número da divisão: "))
                resultado =div_calc(a,b)
                formata_string(resultado)
            case "5":
                break
            case _:
                print("operação invalida, tente novamente")
calculadora()