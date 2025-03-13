import manipula_lista as ml

notas = ml.gerar_lista(4, 0, 100)

# a) As notas dos estudantes.
print(f"a) As notas dos estudantes: {notas}")

# b) A média das notas da turma.
print(f"b) A média das notas da turma: {ml.calcular_media(notas):.2f}")

# c) A quantidade de estudantes com nota acima da média da turma.
print(f"c) Quantidade de estudantes com nota acima da média: {ml.quantidade_elementos_acima_da_media(notas)}")

# d) A quantidade de estudantes com nota abaixo da média da turma.
print(f"d) Quantidade de estudantes com nota abaixo da média: {ml.quantidade_elementos_abaixo_da_media(notas)}")

# e) A quantidade de estudantes aprovados (nota maior ou igual a 70).
print(f"e) Quantidade de estudantes aprovados (nota >= 70): {ml.quantidade_elementos_entre_dois_valores(notas, 70, 100)}")

# f) A quantidade de estudantes reprovados (nota menor que 70).
print(f"f) Quantidade de estudantes reprovados (nota < 70): {ml.quantidade_elementos_entre_dois_valores(notas, 0, 69)}")

# g) A quantidade de estudantes que não possuem nota entre 70 e 80 (inclusive).
print(f"g) Quantidade de estudantes sem nota entre 70 e 80: {ml.quantidade_elementos_fora_de_um_intervalo(notas, 70, 80)}")

# h) Notas que foram encontradas na avaliação.
print(f"h) Notas encontradas na avaliação: {ml.elementos_distintos(notas)}")

# i) Nota(s) mais frequente(s).
print(f"i) Nota(s) mais frequente(s): {ml.elemento_mais_frequente(notas)}")