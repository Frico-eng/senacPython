saudo = 1000
saque = float(input("Insira o valor do saque em reais: "))

if saque>saudo:
    print("não é possível sacar mais do que o seu saudo, tente novamente")
else:
    print(f"Saque realizado com sucesso, novo saudo de R${saudo-saque:.2f}")
