numeros = [0] * 6

for i in range(len(numeros)):
  numeros[i] = int(input("Digite um numero: "))
  
media = sum(numeros)/len(numeros)

print(f"Média = {media:.2f}")