print("="*10, "QUESTAO 05", "="*10)
alunos_aprovados = int(input("Digite a quantidade de alunos aprovados: "))
alunos_reprovados = int(input("Digite a quantidade de alunos reprovados: "))
total_alunos = alunos_aprovados + alunos_reprovados
aprovados_porcetagem = ((total_alunos - alunos_reprovados) / total_alunos) * 100
print(f"A porcentagem total de alunos aprovados e: {aprovados_porcetagem:.1f}%")
print("="*32)