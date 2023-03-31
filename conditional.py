#And, Or e Not
faltas = int(input("Quantidade de faltas: "))
mediaFinal = float(input("Sua média final: "))

if faltas <= 5 and mediaFinal > 6:
    print("Aluno aprovado!")
else:
    print("Aluno reprovado!")