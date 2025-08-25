def calcular_imc(peso,altura):
    return peso/(altura**2)
def classifica_imc(imc):
    if imc<18.5:
        print(F"IMC de {imc:.2f}, abaixo do peso")
    elif imc<25:
        print(F"IMC de {imc:.2f}, peso normal")
    elif imc<30:
        print(F"IMC de {imc:.2f}, sobrepeso")
    elif imc<35:
        print(F"IMC de {imc:.2f}, obesidade grau I")
    elif imc<40:
        print(F"IMC de {imc:.2f}, obesidade grau II")
    else:
        print(F"IMC de {imc:.2f}, obesidade grau III")

def main():
    print("---------------")
    print("Calculadora IMC")
    print("---------------")
    altura = float(input("\nInsira a sua altura: "))
    peso = float(input("\nInsira o seu peso: "))
    imc = calcular_imc(peso,altura)
    classifica_imc(imc)

main()