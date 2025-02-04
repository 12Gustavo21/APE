idades = [0] * 2
nomes = [0] * 2

for i in range(len(idades)):
    idades[i] = int(input("Digite a idade da pessoa: "))
    nomes[i] = input("Digite o nome da pessoa: ")
  
if idades[0] > idades[1]:
    print("A pessoa mais velha tem o nome", nomes[0])
else:
  print("A pessoa mais velha tem o nome", nomes[1])