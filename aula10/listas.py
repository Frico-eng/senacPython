frutas = ["maçã", "banana", "laranja"]
print("Frutas iniciais: ",",".join(frutas))

frutas.append("uva")
print("frutas após, alterações: ",",".join(frutas))
print("número de frutas na lista",len(frutas))
frutas.insert(1,"morango")
print("frutas após, alterações: ",",".join(frutas))
print("número de frutas na lista",len(frutas))
frutas.remove("banana")
frutas.sort()
print("frutas após, alterações: ",",".join(frutas))
print("número de frutas na lista",len(frutas))

#
idades = [15,22,10,30,25]
print("Maior idade: ",max(idades))
print("Menor idade: ",min(idades))
print("Soma das idades: ",sum(idades))
print("Quantidade de idades: ",len(idades))

#
filmes = ["Vingadores","Titanic","Avatar","Matrix","Interstellar"]
i = 0
while i<len(filmes):
    print(f"{i+1}.{filmes[i]}")
    i+=1
print(len(filmes))