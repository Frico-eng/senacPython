# variaveis
largura = float(input("insira o largura do terreno:"))
comprimento = float(input("insira o comprimento do terreno:"))
valor_m2 = float(input("insira o valor do m²:"))

# calculos
area = largura*comprimento
valor_do_terreno = area*valor_m2

# vizualização
print(f"\nÁrea: {area:.2f} M²")
print(f"Valor do terreno: R$ {valor_do_terreno:.2f}\n")