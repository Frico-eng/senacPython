#parte1
nome_gerente = input("Insira o seu nome:")
nome_loja = input("\nInsira o nome da sua loja:")
print(f"\nOlá {nome_gerente},seja bem vindo ao sistema da loja {nome_loja}\n")
#parte2
valor_unit = float(input("Insira o valor unitário de um produto:"))
quantidade = int(input("\nInsira a quantidade de produtos vendida:"))
valor_total = valor_unit*quantidade
print(f"\nO valor total foi de R$ {valor_total}")
#parte3
if(valor_total>500):
    valor_desconto = valor_total*0.9
    print(f"Voce está elegível para um desconto de 10%, a sua compra saiu no valor de R$ {valor_desconto}")
else:
    print(f"A sua compra saiu no valor de R$ {valor_total}")
#parte4
estoque = int(input("Insira a quantidade dispónível em estoque:"))
if(estoque == 0):
    print("Produto indisponível")
else:
    print("Produto disponível para venda\n")
#parte5
tipo_cliente = ""
valor_gasto = float(input("Insira o valor gasto pelo cliente:"))
if valor_gasto>1000:
    tipo_cliente = "VIP"
elif valor_gasto>=500:
    tipo_cliente="Premium"
else:
    tipo_cliente="Comum"
print(f"O cliente é do tipo {tipo_cliente}")