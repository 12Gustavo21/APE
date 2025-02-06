n = int(input())

a = []

for i in range(n):
  a.append(int(input()))
  
b = []
  
for i in range(len(a)):
  if a[i] % 2 == 0:
    b.append(0)
  else:
    b.append(1)
    
print(b)