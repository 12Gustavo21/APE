count = 0

for i in range(6):
  a = int(input("Digite o valor de a: "))
  b = int(input("Digite o valor de b: "))
  c = int(input("Digite o valor de c: "))

  if a < b + c and b < a + c and c < a + b:
    count += 1
    
print("Quantidade de piramides: ", count)