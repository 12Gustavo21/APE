print("="*10, "QUESTAO 05", "="*10)
cont = 0
for i in range(6):
  a = int(input("Digite o valor de a: "))
  b = int(input("Digite o valor de b: "))
  c = int(input("Digite o valor de c: "))
  
  if a < b + c and b < a + c and c < a + b:
    cont += 1
    
  print("="*32)

print(f"{cont} medidas validas")
print("="*32)