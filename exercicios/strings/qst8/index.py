texto = input().split()
palavras = {}

for indice, palavra in enumerate(texto):
    if palavra in palavras:
        palavras[palavra].append(indice)
    else:
        palavras[palavra] = [indice]

"""
sem list comprehensions

max_freq = 0
for indices in palavras.values():
    contagem = len(indices)
    if contagem > max_freq:
        max_freq = contagem

mais_frequentes = []
for palavra, indices in palavras.items():
    if len(indices) == max_freq:
        mais_frequentes.append(palavra)
"""

max_freq = max(len(indices) for indices in palavras.values())
mais_frequentes = [palavra for palavra, indices in palavras.items() if len(indices) == max_freq]

for palavra, indices in palavras.items():
    print("="*38)
    print("palavra: ", palavra)
    print("onde a palavra esta: ", *indices)
    print("quantas vezes a palavra aparece: ", len(indices))

print("="*38)
print("Palavra(s) mais frequente(s):")
print(', '.join(mais_frequentes), f"(frequência: {max_freq})")