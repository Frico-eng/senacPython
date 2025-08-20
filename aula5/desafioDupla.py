#Código de exemplo com 2 números para ver se estão em ordem cresctent ou decrescente com condição de parada quando os dois forem iguais

x = float(input("Insira o primeiro número:"))
y = float(input("Insira o segundo número:"))
while x!=y:
    if x>y:
        print("Decrescente")
    else:
        print("crescente")
    x = float(input("Insira o primeiro número:"))
    y = float(input("Insira o segundo número:"))