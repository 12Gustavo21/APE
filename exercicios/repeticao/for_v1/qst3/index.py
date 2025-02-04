n = int(input("Digite o valor de n: "))
x = int(input("Digite o valor de x: "))
y = int(input("Digite o valor de y: "))

for i in range(x, y + 1):
  if i % n == 0:
    print(i, end=" ")