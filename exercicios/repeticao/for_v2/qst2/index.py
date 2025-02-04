n = int(input("Digite o valor de n: "))

result = 0

for i in range(1, n + 1):
  result += 1 / i
  
print(f"a soma de s é: {result:.2f}")