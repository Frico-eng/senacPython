preco_unit = float(input("insira o preço unitário do produto: "))
unidades = int(input("insira quantas unidades foram compradas: "))
pago = float(input("insira o dinheiro recebido: "))

troco = pago-(preco_unit*unidades)

print(f"\n\nPara a compra de R$ {preco_unit*unidades:.2f} com pagamento de R$ {pago:.2f} o seu troco será de: R$ {troco:.2f}\n\n")