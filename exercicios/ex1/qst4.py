import math

print("="*10, "QUESTAO 04", "="*10)
carga_horaria = 50
segundos_necessarios = int(input("Digite os segundos necessarios para realizar a prova: "))
segundos_para_minutos = segundos_necessarios / 60
tempo_necessario = math.ceil(segundos_para_minutos / carga_horaria)
print(f"Aulas necessarias para a realizacao da prova: {tempo_necessario}")
print("="*32)