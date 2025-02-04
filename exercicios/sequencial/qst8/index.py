aulas = int(input("Digite a quantidade de notas: "))
faltas = int(input("Digite a quantidade de faltas: "))

frequencia = ((aulas - faltas) / aulas) * 100

print(f"Sua frequencia é de: {frequencia:.2f}%")