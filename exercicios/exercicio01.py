print("="*10, "QUESTAO 01", "="*10)
n1 = int(input("Digite a primeira nota: "))
n2 = int(input("Digite a segunda nota: "))
n3 = int(input("Digite a terceira nota: "))
media = (n1 + n2 + n3) / 3
print("A média aritmética das notas é: ", media)

print("="*10, "QUESTAO 02", "="*10)
numero_aulas = int(input("Digite a quantidade de aulas: "))
numero_faltas = int(input("Digite a quantidade de faltas: "))
frequencia = ((numero_aulas - numero_faltas) / numero_aulas) * 100
print(f"Você compareceu a {frequencia:.1f}% da discplina")

print("="*10, "QUESTAO 03", "="*10)
media_semestral = int(input("Digite a media semestral: "))
nota_final = int(input("Digite a nota final: "))
media_final = ((media_semestral*6) + (nota_final*4)) / 10
print("Sua média final é: ", media_final)

print("="*10, "QUESTAO 04", "="*10)
carga_horaria = 50
segundos_necessarios = int(input("Digite os minutos necessarios para realizar a prova: "))
minutos_para_segundos = segundos_necessarios * 60
tempo_necessario = minutos_para_segundos / (carga_horaria * 60)
print(f"Aulas necessarias para a realizacao da prova: {tempo_necessario:.1f}")

print("="*10, "QUESTAO 05", "="*10)
alunos_aprovados = int(input("Digite a quantidade de alunos aprovados: "))
alunos_reprovados = int(input("Digite a quantidade de alunos reprovados: "))
total_alunos = alunos_aprovados + alunos_reprovados
aprovados_porcetagem = ((total_alunos - alunos_reprovados) / total_alunos) * 100
print(f"A porcentagem total de alunos aprovados e: {aprovados_porcetagem:.1f}%")
print("="*32)