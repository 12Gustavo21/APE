"""
CODIGO ORIGINAL 
  
import random

t = 2

m = [[random.randint(1, 100) for _ in range(t)] for _ in range(t)]

mt = [[m[j][i] for j in range(t)] for i in range(t)]

for i in range(t):
  print(m[i])
  
print("="*38)
  
for i in range(t):
  print(mt[i])

simetrica = True 
for i in range(t):
  for j in range(t):
    if m[i][j] != mt[i][j]:
      simetrica = False
      
if simetrica:
  print("matriz simetrica")
else:
  print("matriz nao simetrica")
"""

# CODIGO QUE O DEEPSEEK FORNECEU COM MELHORIAS

import random

TAMANHO = 2

matriz = [[random.randint(1, 100) for _ in range(TAMANHO)] for _ in range(TAMANHO)]

matriz_transposta = [list(linha) for linha in zip(*matriz)]

def imprimir_matriz(matriz, titulo):
    print(titulo)
    for linha in matriz:
      print([f"{numero:2}" for numero in linha])

imprimir_matriz(matriz, "Matriz Original")
print("=" * (TAMANHO * 5 + 2)) 
imprimir_matriz(matriz_transposta, "Matriz Transposta")

simetrica = matriz == matriz_transposta

print("\nResultado:", "Matriz simétrica" if simetrica else "Matriz não simétrica")