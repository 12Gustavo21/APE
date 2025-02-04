numeros = [0] * 3

for i in range(len(numeros)):
  numeros[i] = int(input("Digite um numero: "))
  
if numeros[0] == numeros[1] and numeros[0] == numeros[2]:
  print("Os numeros sao iguais")
else:
  print("Os numeros sao diferentes")