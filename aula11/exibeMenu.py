def exibe_menu(options):
    print("Opções:")
    for i, option in enumerate(options):
        print(f"{i+1} - {option}")
    operador = input("Escolha uma opção: ")
    return operador

def sair():
    return True

def formatar_msg(msg):
    print("-------------------------")
    print(msg)
    print("-------------------------")