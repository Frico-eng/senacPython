import sys
import math

def raiz_log(numero):
    if numero < 0:
        print("Erro: números negativos não são suportados")
        return None
    elif numero == 0:
        return 0
    return math.exp(0.5 * math.log(numero))

def main():
    # Verifica se recebeu argumentos suficientes
    if len(sys.argv) < 2:
        print("\nUso: python script.py <numero>")
        print("Exemplo: python script.py 400\n")
        sys.exit(1)

    try:
        numero = float(sys.argv[1])
    except ValueError:
        print("Erro: argumentos devem ser numéricos")
        sys.exit(1)

    resultado = raiz_log(numero)
    if resultado is not None:
        print(f"A raiz de {numero} é {resultado:.4f}")

if __name__ == "__main__":
    main()
