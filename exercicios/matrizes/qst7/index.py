m = [[10, 20, 30, 40], [50, 60, 70, 80], [90, 100, 110, 120]]

soma = 0
count = 0

for i in range(3):
  for j in range(4):
    soma += m[i][j]
    count += 1

print(soma/count)