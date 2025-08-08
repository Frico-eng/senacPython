nome = input("Digite o nome do funcionário: ")

valor_por_hora = float(input("Digite o valor por hora: "))

horas_trabalhadas = float(input("Digite a quantidade de horas trabalhadas: "))

# Calcular o pagamento bruto
pagamento_bruto = valor_por_hora * horas_trabalhadas

# Calcular o desconto de 7,5%
desconto = 0.075 * pagamento_bruto

# Calcular o pagamento líquido
pagamento_liquido = pagamento_bruto - desconto

print(f"O funcionário {nome} trabalhou {horas_trabalhadas} horas.")
print(f"Pagamento bruto: R${pagamento_bruto:.2f}")
print(f"Desconto (7,5%): R${desconto:.2f}")
print(f"Pagamento líquido: R${pagamento_liquido:.2f}")
