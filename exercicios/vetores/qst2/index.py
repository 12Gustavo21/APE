import random

numeros = [None] * 100

for i in range(len(numeros)):
  numeros[i] = random.randint(1, 60)

numeros_unicos = []

for i in range(len(numeros)):
  if numeros[i] not in numeros_unicos:
    numeros_unicos.append(numeros[i])
  
print(numeros_unicos)