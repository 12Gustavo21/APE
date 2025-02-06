import random

m = []

for i in range(20):
  m.append([None] * 50)

for i in range(20):
  for j in range(50):
    m[i][j] = random.randint(1, 100)

print(m)

k = int(input())
for i in range(20):
  for j in range(50):
    if m[i][j] == k:
      print(i, j)