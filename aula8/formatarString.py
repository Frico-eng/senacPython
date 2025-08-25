def formatar_string(nome,sobrenome,idade):
        return f"{nome.title()}, {sobrenome.title()}, {idade} anos"
    
nome= input("Digite seu nome: ")
sobrenome= input("Digite seu sobrenome: ")
idade= int(input("Digite sua idade: "))

resultado = formatar_string(nome,sobrenome,idade)

print(f"String formatada: {resultado}")

