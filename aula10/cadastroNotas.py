def media(notas):
    return sum(notas)/len(notas)
def verifica_condicao(media):
    if media>=7:
        return True
    else:
        return False

def float_2_str(lista):
    lista_str =[]
    for i in range(len(lista)):
        lista_str.append(str(lista[i]))
    return lista_str

def cadastro():
    notas = []
    print("---Cadastro de notas---")
    qntd_notas = int(input("Insira a quantidade de notas: "))
    for i in range(qntd_notas):
        nota = float(input(f"Insira a {i+1}° nota: "))
        notas.append(nota)
    
    # converte cada nota para string
    notas_str = float_2_str(notas)
    print("Notas cadastradas: " + ", ".join(notas_str))

    return notas
def main():
    notas = cadastro()
    media_notas = media(notas)
    print(f"Média do aluno:{media_notas:.2f}")
    if verifica_condicao(media_notas):
        print("Aluno aprovado no sistema")
    else:
        print("Aluno reprovado no sistema")
main()