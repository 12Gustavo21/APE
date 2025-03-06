import manipula_lista as ml

# Função: gerar_lista
numeros = ml.gerar_lista(4, 1, 100)

# Função: exibir_lista
print("Exibir lista:")
ml.exibir_lista(numeros)

# Função: calcular_media
print(f"Média dos elementos da lista: {ml.calcular_media(numeros):.2f}")

# Função: elementos_acima_da_media
print(f"Elementos acima da média: {ml.elementos_acima_da_media(numeros)}")

# Função: elementos_abaixo_da_media
print(f"Elementos abaixo da média: {ml.elementos_abaixo_da_media(numeros)}")

# Função: elementos_entre_dois_valores
print(f"Elementos entre dois valores (1 e 50): {ml.elementos_entre_dois_valores(numeros, 1, 50)}")

# Função: elementos_fora_de_um_intervalo
print(f"Elementos fora do intervalo (1 e 50): {ml.elementos_fora_de_um_intervalo(numeros, 1, 50)}")

# Função: elementos_distintos
print(f"Elementos distintos na lista: {ml.elementos_distintos(numeros)}")

# Função: elemento_mais_frequente
print(f"Elemento mais frequente na lista: {ml.elemento_mais_frequente(numeros)}")

# Função: quantidade_elementos_acima_da_media
print(f"Quantidade de elementos acima da média: {ml.quantidade_elementos_acima_da_media(numeros)}")

# Função: quantidade_elementos_abaixo_da_media
print(f"Quantidade de elementos abaixo da média: {ml.quantidade_elementos_abaixo_da_media(numeros)}")

# Função: quantidade_elementos_entre_dois_valores
print(f"Quantidade de elementos entre dois valores (1 e 50): {ml.quantidade_elementos_entre_dois_valores(numeros, 1, 50)}")

# Função: quantidade_elementos_fora_de_um_intervalo
print(f"Quantidade de elementos fora do intervalo (1 e 50): {ml.quantidade_elementos_fora_de_um_intervalo(numeros, 1, 50)}")

# Função: quantidade_elementos_distintos
print(f"Quantidade de elementos distintos na lista: {ml.quantidade_elementos_distintos(numeros)}")