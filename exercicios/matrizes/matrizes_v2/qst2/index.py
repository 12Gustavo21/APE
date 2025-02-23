t = 3
dp = 0
rm = 0

m = [[int(input()) for _ in range(t)] for _ in range(t)]

for i in range(t):
  if m[i][i] == 1:
    dp += 1
  for j in range(t):
    if i != j and m[i][j] == 0:
      rm += 1

    
if dp == t and rm == (t*(t-1)):
  print("SIM")
else:
  print("NAO")