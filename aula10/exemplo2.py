while True:
    try:
        n1 = float(input("\nDigite o primeiro número: "))
        n2 = float(input("\nDigite o segundo número: "))
        op = input("Insira uma operação: ")
        match op:
            case "+":
                print(f"\nResultado: {n1} + {n2} = ",n1+n2)
            case "-":
                print(f"\nResultado: {n1} - {n2} = ",n1-n2)
            case "*":
                print(f"\nResultado: {n1} * {n2} = ",n1*n2)
            case "/":
                print(f"\nResultado: {n1} / {n2} = ",n1/n2)
            case "quit":
                break
            case _:
                print("opção invalida")
            
    except ValueError:
        print("Digite apenas números")
    except ZeroDivisionError:
        print("impossível dividir por zero")