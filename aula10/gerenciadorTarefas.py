def inserir(elemento, lista):
    """Adiciona uma tarefa à lista se ainda não existir"""
    if elemento not in lista:
        lista.append(elemento)
    else:
        print("Tarefa já está na lista")


def remover(elemento, lista):
    """Remove uma tarefa da lista se existir"""
    if elemento in lista:
        lista.remove(elemento)
    else:
        print("Tarefa não está na lista")


def listar(lista):
    """Exibe todas as tarefas cadastradas"""
    if not lista:
        print("Nenhuma tarefa cadastrada")
    else:
        print("\nTarefas cadastradas:")
        for i, tarefa in enumerate(lista, start=1):
            print(f"{i} - {tarefa}")


def operacoes(operador, lista):
    """Executa a operação escolhida pelo usuário"""
    match operador:
        case "1":
            tarefa = input("Insira uma tarefa para cadastro: ")
            inserir(tarefa, lista)
        case "2":
            tarefa = input("Insira uma tarefa para remoção: ")
            remover(tarefa, lista)
        case "3":
            listar(lista)
        case "4":
            return True
        case _:
            print("Opção inválida, tente novamente")
    return False

def menu():
    print("\n=== Gerenciador de Tarefas ===")
    print("1 - Adicionar tarefa")
    print("2 - Remover tarefa")
    print("3 - Listar tarefas")
    print("4 - Finalizar programa")

def main():
    tarefas = []
    while True:
        menu()
        operador = input("Insira uma opção: ").strip()
        if operacoes(operador, tarefas):
            print("Programa finalizado")
            break

main()
