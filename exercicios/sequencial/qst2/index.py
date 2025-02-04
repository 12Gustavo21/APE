idades = [0] * 2

for i in range(len(idades)):
    idades[i] = int(input("Digite a idade da pessoa: "))
  
if idades[0] > idades[1]:
    print("A pessoa mais velha tem", idades[0], "anos")
else:
  print("A pessoa mais velha tem", idades[1], "anos")