#código de soma dos n primeiros números

# metodo por soma dos elementos da progressão aritimética
# soma_pa = (1+n)*n/2
# print(f"soma por PA {soma_pa}")
n = int(input("Insira a quantidade de números a ser somada:"))
n_temp = n
soma = 0
while n_temp>0:
    soma=soma+n_temp
    n_temp=n_temp-1
print(f"\nA soma até {n} é igual a {soma}\n")