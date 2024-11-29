print("="*10, "QUESTAO 02", "="*10)
numero_aulas = int(input("Digite a quantidade de aulas: "))
numero_faltas = int(input("Digite a quantidade de faltas: "))
frequencia = ((numero_aulas - numero_faltas) / numero_aulas) * 100
print(f"Você compareceu a {frequencia:.1f}% da discplina")
print("="*32)