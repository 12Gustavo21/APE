soma = 0
count = 0

while count < 2:
  nota = float(input())
  if nota >= 0 and nota <= 10:
    soma += nota
    count += 1
  else:
    print("nota invalida")

print(f"media = {soma/count}")