notas = [0] * 3

for i in range(len(notas)):
  notas[i] = int(input("Digite a notas: "))
  
soma = (sum(notas))/len(notas)
print(soma)