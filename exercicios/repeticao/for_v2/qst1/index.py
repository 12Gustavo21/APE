n = int(input("Digite o valor de n: "))

result = 1

for i in range(1, n + 1):
    result *= i

print(f"O fatorial de {n} é {result}")