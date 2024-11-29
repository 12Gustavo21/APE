print("="*10, "QUESTAO 01", "="*10)
numero = int(input("Digite um número inteiro positivo: "))
print("="*32)

if numero >= 0:
  if numero % 2 == 0:
    print(f"O número {numero} é par")
  else:
    print(f"O número {numero} é número ímpar")
else: 
  print("Informe um número positivo")
print("="*32)