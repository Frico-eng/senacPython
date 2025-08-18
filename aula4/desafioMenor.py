print("Para a proxima operação, voce terá que inserir 3 números: ")

n1 = float(input("Insira o primeiro número: "))
n2 = float(input("Insira o segundo número: "))
n3 = float(input("Insira o terceiro número: "))

menor = n1
if n2<n1:
    menor = n2
if n3<n1:
    menor = n3
    
print(f"O menor número é {menor}")