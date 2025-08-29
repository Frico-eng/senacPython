def classifica(numero):
    condicao = numero%2
    if condicao == 0:
        print("o número é par")
    else:
        print("o número é ímpar")


numero = int(input("Insira um número: "))
classifica(numero)

def tabuada (numero_2):
    for i in range(1,11):
        print(f"{numero_2}*{i} = {numero_2 * i}")
        numero_3 = int(input("Digite o número:"))
        tabuada(numero_3)

def soma_N (numero):
    soma = 0
    i = 1
    while i<=numero:
        soma += i
        i+=1
        return soma
numero_4 = int(input("Digite o número:"))
soma = soma_N(numero_4)
print(f"A soma de 1 a {numero_4} é igual a {soma}")

def eh_primo(numero):
    contador = 0
    for i in range(1,numero):
        resto = numero%i
    if resto == 0:
        contador+=1
    if contador<=2:
        print("é primo")
    else:
        print("não é primo")

numero_5 = int(input("Digite o número:"))
eh_primo(numero_5)


soma_notas = 0
num_notas = 0
num_maior = 0
num_menor = 99999999999

def media(soma_notas,num_notas):
    media_notas = soma_notas/num_notas
    return media_notas
def maior_nota(maior, nota):
    if nota > maior:
        return nota
    return maior
def menor_nota(menor, nota):
    if nota < menor:
        return nota
    return menor


nota = float(input("Digite uma nota: "))
while nota>=0:
    soma_notas = soma_notas+nota
    num_notas = num_notas+1
    num_maior=maior_nota(num_maior, nota)
    num_menor=menor_nota(num_menor, nota)
    nota = float(input("Digite uma nota: "))

media_notas = media(soma_notas,num_notas)
print(f"A média é {media_notas}")
print(f"A nota maior: {num_maior}")
print(f"A menor nota é:{num_menor}")

def caixa(valor):
    nota50 = 0
    nota20 = 0
    nota10 = 0
    nota1 = 0

    while valor>0:
        if valor-50>=0:
            valor-=50
            nota50+=1
        elif valor-20>=0:
            valor-=20
            nota20+=1
        elif valor-10>=0:
            valor-=10
            nota10+=1
        elif valor -1>=0:
            valor-=1
            nota1+=1
        else:
            break
    print(f"Voçê sacou: {nota50} notas de 50 reais {nota20} notas de 20 reais {nota10} notas de 10 reais {nota1} notas de 1 reais sacadas")

valor = int(input("Insira o valor do saque: "))
caixa(valor)