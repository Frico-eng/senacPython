#parte1
peso = float(input("Insira o seu peso em Kg:"))
altura = float(input("Insira a sua altura em m:"))
imc = peso/(altura**2)
if imc<18.5:
    print("Você está abaixo do peso")
elif imc<25:
    print("Você está no peso ideal")
else:
    print("Você está acima do peso")
#parte2
numero = int(input("\nInsira um número:"))
if numero%2 == 0:
    print(f"O número {numero} é par") 
else:
    print(f"O número {numero} é impar") 
#parte3
real = float(input("\nInsira um valor em reais:"))
real_em_Dolar = real/5.2
print(f"O valor de R${real} em dolares é de ${real_em_Dolar:.2f}")
#parte4
nota1 = float(input("\nInsira uma primeira nota:"))
nota2 = float(input("Insira uma segunda nota:"))
media = (nota1+nota2)/2
if media>=7:
    print(f"\nMédia de {media}. Aluno aprovado")
elif media>5:
    print(f"\nMédia de {media}. Aluno em recuperação")
else:
    print(f"\nMédia de {media}. Aluno reprovado")
#parte5
numero1 = float(input("\nInsira um primeiro número:"))
numero2 = float(input("Insira um segundo número:"))
numero3 = float(input("Insira um terceiro número:"))
maior = numero1

if numero2>maior:
    maior = numero2
if numero3>maior:
    maior = numero3
    
print(f"\nEntre os numeros {numero1},{numero2} e {numero3} o maior é {maior}")
#parte6
ano_nascimento = float(input("\nInsira o seu ano de nascimento:"))
idade = 2025-ano_nascimento
print(f"\nIdade de {idade}:")
if idade>=18 and idade<=70:
    print("Voto obrigatório")
elif idade>16 or idade>70:
    print("Voto opcional")
else:
    print("não pode votar")
#parte7

idade_cliente = int(input("\nInsira a sua idade:"))
if idade_cliente<12:
    print("O ingresso custa R$ 12")
elif idade_cliente<17:
    print("O ingresso custa R$ 15")
else:
    print("O ingresso custa R$ 20")