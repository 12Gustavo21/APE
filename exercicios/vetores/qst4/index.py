import random

numeros = [None] * 100

for i in range(len(numeros)):
  numeros[i] = random.randint(1, 40)
  
numeros_repetidos = []

for i in range(len(numeros)):
  if numeros[i] in numeros_repetidos:
    continue
  for j in range(i + 1, len(numeros)):
    if numeros[i] == numeros[j]:
      numeros_repetidos.append(numeros[i])
      break

print(numeros_repetidos)