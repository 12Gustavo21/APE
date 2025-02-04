import random

numeros = [None] * 10

for i in range(len(numeros)):
  numeros[i] = random.randint(1, 60)

for i in range(len(numeros)):
  repeticao = False
  if numeros[i] in numeros[i+1:]:
    repeticao = True
    break
    
print(numeros)

if repeticao:
  print('Existem números repetidos')
else:
  print('Não existem números repetidos')