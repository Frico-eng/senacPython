
while True:
    numeros = int(input("Digite quantos números desejas incluir:"))
    if numeros>=0:
        break
    else:
        print("número negativo não suportado na versão atual, tente novamente")

dentro_intervalo = 0
fora_intervalo = 0

for i in range(1,numeros+1):
    n = int(input(f"Insira o {i}° número:"))
    if 10<=n<=20:
        dentro_intervalo+=1
    else:
        fora_intervalo+=1
print(f"Números dentro do intervalo: {dentro_intervalo}")
print(f"Números dentro do intervalo: {fora_intervalo}")