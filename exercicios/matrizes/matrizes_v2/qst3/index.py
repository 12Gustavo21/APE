"""
CODIGO ORIGINAL

import random

t = 4

m = [[random.randint(1,100) for _ in range(t)] for _ in range(t)] 

for i in range(t):
  print(m[i])

print("="*38)

dp = [m[i][j] for i in range(t) for j in range(t) if i == j]
print(dp)

ds = [m[i][j] for i in range(t) for j in range(t) if i + j == len(m)-1]
print(ds)

rows = [sum(m[i]) for i in range(t)]
print(rows)

cols = [sum(m[j][i] for j in range(t)) for i in range(t)]
print(cols)

if sum(rows) == sum(cols) and sum(dp) == sum(ds):
  print("MATRIZ QUADRADO MAGICO")
else:
  print("MATRIZ NAO EH QUADRADO MAGICO")
"""

# CODIGO QUE O DEEPSEEK FORNECEU COM MELHORIAS
import random

tamanho = 4

matriz = [[random.randint(1, 100) for _ in range(tamanho)] for _ in range(tamanho)]

print("Matriz:")
for linha in matriz:
    print(linha)

print("=" * 38)

soma_diagonal_principal = sum(matriz[i][i] for i in range(tamanho))

soma_diagonal_secundaria = sum(matriz[i][tamanho-1-i] for i in range(tamanho))

print(f"Soma da diagonal principal: {soma_diagonal_principal}")
print(f"Soma da diagonal secundária: {soma_diagonal_secundaria}")

somas_linhas = [sum(linha) for linha in matriz]

somas_colunas = [sum(coluna) for coluna in zip(*matriz)]

print("Somas das linhas:", somas_linhas)
print("Somas das colunas:", somas_colunas)

# Verifica todas as condições para quadrado mágico
soma_magica = somas_linhas[0]
linhas_ok = all(soma == soma_magica for soma in somas_linhas)
colunas_ok = all(soma == soma_magica for soma in somas_colunas)
diagonais_ok = (soma_diagonal_principal == soma_magica) and (soma_diagonal_secundaria == soma_magica)

if linhas_ok and colunas_ok and diagonais_ok:
    print("MATRIZ É UM QUADRADO MÁGICO")
else:
    print("MATRIZ NÃO É UM QUADRADO MÁGICO")