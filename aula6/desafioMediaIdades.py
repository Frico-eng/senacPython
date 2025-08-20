soma = 0
contador = 0

while True:
    idade = int(input("Insira a sua idade: "))
    if idade < 0:  # stop input on negative number
        break
    soma += idade
    contador += 1

if contador == 0:
    print("Impossível calcular, nenhuma idade válida foi inserida")
else:
    media = soma / contador
    print(f"A média das idades é {media:.2f}")
