while True:
    try:
        idade = int(input("\nDigite a sua idade:"))
        print(f"\nSua idade é de {idade} anos")
    except ValueError:
        print("\nError, isso não é um número inteiro")