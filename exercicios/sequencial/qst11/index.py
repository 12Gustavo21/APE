aprovados = int(input("Digite a quantidade de alunos aprovados: "))
reprovados = int(input("Digite a quantidade de alunos reprovados: "))

totalAlunos = aprovados + reprovados

porcentagemAprovados = (aprovados / totalAlunos) * 100

print(f"A porcentagem de alunos aprovados: {porcentagemAprovados:.2f}%")