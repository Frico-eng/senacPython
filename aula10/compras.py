def verifica_lista(lista, elemento):
    """Adiciona 'elemento' à lista se não estiver presente. Retorna True se adicionado."""
    if elemento in lista:
        return False
    lista.append(elemento)
    return True


def listar_itens(lista):
    """Exibe os itens da lista de compras."""
    if not lista:
        print("A lista está vazia")
    else:
        print("\nLista de compras:")
        for index, item in enumerate(lista, start=1):
            print(f"{index} - {item}")


def menu():
    lista_compras = []
    while True:
        print("\nOpções:")
        print("i - Inserir")
        print("l - Listar")
        print("s - Sair")
        operador = input("Insira uma opção: ").strip().lower()

        match operador:
            case "i":
                compra = input("Insira um item para a sua lista de compras: ").strip()
                if not verifica_lista(lista_compras, compra):
                    print(f"{compra} já está na lista")
            case "l":
                listar_itens(lista_compras)
            case "s":
                print("Até a próxima.")
                break
            case _:
                print("Opção inválida, tente novamente.")


def main():
    menu()


if __name__ == "__main__":
    main()
