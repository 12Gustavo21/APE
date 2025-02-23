l = 3
c = 4

m = [[int(input()) for _ in range(c)] for _ in range(l)]

soma = 0
count = 0

maiores_media = []

for i in range(l):
  for j in range(c):
    soma += m[i][j]
    count += 1

for i in range(l):
  for j in range(c):
    if m[i][j] > (soma/count):
      maiores_media.append(m[i][j])

print(soma/count)
print(maiores_media)