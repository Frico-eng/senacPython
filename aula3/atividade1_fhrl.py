#bloco 1
print("\nOlá, este é meu primeiro programa em Python.")
print("Meu nome é Frederico Henrique do Rosario Lopes.")
print("Eu tenho 28 anos de idade.")
print("Eu sou de Belém do Pará.")
print("Is this the real life? Is this just fantasy?\nCaught in a landslide, no escape from reality\nOpen your eyes, look up to the skies and see\nI'm just a poor boy, I need no sympathy")
#bloco2
nome_usr = input("\nInsira o seu nome: ")
idade_usr = int(input("Insira a sua idade: "))
print(f"Olá, {nome_usr}! Você tem {idade_usr} anos\n")
numero_dobrar = float(input("Insira um número para ser dobrado: "))
print(f"O dobro do seu número {numero_dobrar} é {numero_dobrar*2}\n")
numero_somar1 = float(input("Agora, para a próxima operação insira um número: "))
numero_somar2 = float(input("Agora, insira um segundo número: "))
soma = numero_somar1+numero_somar2
print(f"A soma de {numero_somar1} com {numero_somar2} é igual a {soma}\n")
#bloco3
nota1 = float(input("Para a próxima operação insira uma nota: "))
nota2 = float(input("Para a próxima operação insira uma segunda nota: "))
nota3 = float(input("Para a próxima operação insira uma terceira nota: "))
media = (nota1+nota2+nota3)/3
print(f"A média das suas notas é de {media:.2f}\n")
idade_meses = 12*float(input("Insira a sua idade: "))
print(f"Você já viveu aproximadamente {idade_meses} meses de idade")
altura_ret = float(input("Insira uma altura (em cm) para um retângulo: "))
largura_ret = float(input("Insira uma largura (em cm) para um retângulo: "))
area_ret = altura_ret*largura_ret
print(f"Este retângulo tem área de {area_ret:.4f} cm²\n")
#bloco4
unidades_produto = int(input("Assuma que produto custa R$ 15.90, Inisira quantos deste produto você quer comprar: "))
preço_total = unidades_produto*15.90
print(f"A sua compra saiu no valor de R$ {preço_total:.2f}\n")
distancia = float(input("Assuma que você dirige um carro que faz, em média, 12 Km/l. Insira uma distância(em Km) que você pretende percorrer: "))
litros_nesc = distancia/12
print(f"Para percorrer a distância de {distancia} Km você presisará de {litros_nesc:.2f} litros")
salario = float(input("Insira o seu salário: "))
print(f"O seu salário reajustado em 10% é R$ {salario*1.1:.2f}")