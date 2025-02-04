m = [[10, 20, 30, 40], [50, 60, 70, 80], [90, 100, 110, 120]]

soma = 0
count = 0

maiores_media = []

for i in range(3):
  for j in range(4):
    soma += m[i][j]
    count += 1

for i in range(3):
  for j in range(4):
    if m[i][j] > (soma/count):
      maiores_media.append(m[i][j])

print(soma/count)
print(maiores_media)