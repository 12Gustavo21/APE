t = 3
min = 1
max = 100

m = [[int(input()) for _ in range(t)] for _ in range(t)]

dp = [m[i][i] for i in range(t)]

for linha in m:
    print(linha)
    
print(f"\n{dp}")