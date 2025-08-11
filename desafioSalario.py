salario_inicial = float(input("\nInsira o seu salário para iniciar o reajuste:"))
if salario_inicial<=280:
    salario = salario_inicial*1.2
    ajuste = "20%"
elif salario_inicial<=700:
    salario = salario_inicial*1.15
    ajuste = "15%"
elif salario_inicial<=1500:
    salario = salario_inicial*1.1
    ajuste = "10%"
else:
    salario = salario_inicial*1.05
    ajuste = "5%"


print(f"\nO seu salário de R${salario_inicial}")
print(f"O seu salário passou por um reajuste de {ajuste}")
print(f"O que resultou em um aumento nominal de R${salario-salario_inicial:.2f}")
print(f"O seu salário reajustado é de R${salario:.2f}\n")