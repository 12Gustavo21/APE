print("="*10, "QUESTAO 03", "="*10)
n = int(input("Digite o numero N: "))
x = int(input("Digite o numero x: "))
y = int(input("Digite o número y: "))

for numero in range(x, y + 1):
  if numero % n == 0:
    print(numero, end=" ")
print("="*32)