idades = [0] * 40

for i in range(len(idades)):
  idades[i] = int(input("Digite a idade: "))
  maisVelha = idades[0]
  maisNova = idades[0]
  
  if idades[i] > maisVelha:
    maisVelha = idades[i]
  elif idades[i] < maisNova:
    maisNova = idades[i]
    
print(f"Mais velha: ", maisVelha)
print(f"Mais nova: ", maisNova)