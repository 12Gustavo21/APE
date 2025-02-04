import math

segundos = int(input("Digite a quantidade de segundo necessarios: "))
aulas = 50

segundosParaMinutos = segundos / 60

aulasNecessarias = segundosParaMinutos / aulas

print("Quantidade de aulas necessarias: ", math.ceil(aulasNecessarias))