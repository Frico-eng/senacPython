from exibeMenu import exibe_menu, sair

def cadastrar_produto(produtos):
    while True:
        nome = input("Cadastre o nome do produto: ").strip()
        if any(nome.lower() == p[0].lower() for p in produtos):
            print("Produto já existe, tente novamente.")
            continue
        try:
            preco = float(input("Preço do produto: R$ "))
            return (nome, preco)
        except ValueError:
            print("Digite um valor válido para o preço.")

def listar(produtos):
    if produtos:
        print("--- Inventário ---")
        for i, (nome, preco) in enumerate(produtos, 1):
            print(f"{i} - {nome.title()}, R$ {preco:.2f}")
        print("-----------------")
    else:
        print("-----------------")
        print("Lista sem produtos.")
        print("-----------------")

def buscar_por_nome(produtos):
    nome_busca = input("Insira o nome do produto: ").strip().lower()
    produto = next((p for p in produtos if p[0].lower() == nome_busca), None)
    if produto:
        print("-----------------")
        print(f"Produto encontrado: {produto[0].title()} - R$ {produto[1]:.2f}")
        print("-----------------")
    else:
        print("-----------------")
        print("Produto não encontrado.")
        print("-----------------")

def remover_produto(produtos):
    nome_busca = input("Insira o nome do produto a remover: ").strip().lower()
    indice = next((i for i, p in enumerate(produtos) if p[0].lower() == nome_busca), None)
    if indice is not None:
        nome, preco = produtos.pop(indice)
        print("-----------------")
        print(f"Produto removido: {nome.title()} - R$ {preco:.2f}")
        print("-----------------")
    else:
        print("-----------------")
        print("Produto não encontrado.")
        print("-----------------")

def valor_total(produtos):
    total = sum(preco for _, preco in produtos)
    print("-----------------")
    print(f"Total do estoque: R$ {total:.2f}")
    print("-----------------")

def main():
    produtos = []
    opcoes = [
        "Cadastrar",
        "Listar",
        "Buscar por nome",
        "Remover produto",
        "Calcular valor total do estoque",
        "Sair"
    ]
    
    while True:
        escolha = exibe_menu(opcoes)
        match escolha:
            case "1":
                produtos.append(cadastrar_produto(produtos))
            case "2":
                listar(produtos)
            case "3":
                buscar_por_nome(produtos)
            case "4":
                remover_produto(produtos)
            case "5":
                valor_total(produtos)
            case "6":
                if sair():
                    print("\nAté a próxima!\n")
                    break
            case _:
                print("Opção inválida, tente novamente.")

if __name__ == "__main__":
    main()
