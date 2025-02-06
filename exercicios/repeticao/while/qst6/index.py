soma = 0
count = 0

while True:
  i = int(input())
  if i >= 0:
    soma += i
    count += 1
  else:
    break
  
print(soma/count)