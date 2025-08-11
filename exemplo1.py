nota = float(input("Insira a nota de uma aluno: "))

if nota>10:
    print("Nota invalida, favor tentar novamente")
elif nota>=7 and nota<=10:
    print("Aluno aprovado")
elif nota>=5 and nota<7 :
    print("Aluno em recuperação")
else:
    print("Aluno não aprovado")