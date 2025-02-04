notas = [0] * 8
count = 0

for i in range(len(notas)):
  notas[i] = int(input("Digite um numero: "))
  if notas[i] >= 0 and notas[i] <= 100:
    count += 1

print(f"Foram informadas {count} notas válidas para o Suap")