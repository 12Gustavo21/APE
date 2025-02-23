m = [[10, 20, 30, 40], [50, 60, 70, 80], [90, 100, 110, 120]]
m.append([130, 140, 150, 160])

soma = 0

for i in range(4):
  for j in range(4):
    if i == j:
      soma += m[i][j]

print(soma)