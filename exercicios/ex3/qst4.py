print("="*10, "QUESTAO 04", "="*10)
n = int(input("Digite o numero N: "))
x = int(input("Digite o numero x: "))
y = int(input("Digite o número y: "))

cont = 0

for numero in range(x, y + 1):
  if numero % n == 0:
    cont += 1
  
print(f"O total de mutiplos de {n} entre {x} e {y} e: {cont}")
print("="*32)