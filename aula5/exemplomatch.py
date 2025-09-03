#Código de exemplo do match case
opcao = int(input("Escolha uma operação:\n1 - Soma\n2 - Subtração\n3 - multiplicação\n4 - divisão\n------------------\n"))
num1 = float(input("\nnInsira o primeiro número:"))
num2 = float(input("\nInsira o segundo número:"))

match opcao:
    case 1:
        print(f"Resultado da soma: {num1+num2}")
    case 2:
        print(f"Resultado da subtração: {num1-num2}")
    case 3:
        print(f"Resultado da soma: {num1*num2}")
    case 4:
        print(f"Resultado da soma: {num1/num2}")
    case _:
        print(f"Opeção invalida")