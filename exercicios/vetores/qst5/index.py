import random

numeros = [None] * 6

for i in range(len(numeros)):
  numeros[i] = random.randint(1, 60)
  
numeros_unicos = []

for i in range(len(numeros)):
  if numeros[i] not in numeros_unicos:
    numeros_unicos.append(numeros[i])

print(numeros_unicos)

for i in range(len(numeros_unicos)):
  for j in range(i, len(numeros_unicos)):
    if numeros_unicos[i] > numeros_unicos[j]:
      numeros_unicos[i], numeros_unicos[j] = numeros_unicos[j], numeros_unicos[i]

print(numeros_unicos)