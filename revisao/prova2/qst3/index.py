import random

m = []

for i in range(4):
  m.append([None] * 4)
  
for i in range(4):
  for j in range(4):
    m[i][j] = random.randint(1, 100)
    
dp = []

for i in range(4):
  for j in range(4):
    if i == j:
      dp.append(m[i][j])

for i in range(4):
  print(m[i])

print("="*38)
print(dp)

ds = []

for i in range(4):
  for j in range(4):
      if i + j == len(m)-1:
        ds.append(m[i][j])
      
print(ds)