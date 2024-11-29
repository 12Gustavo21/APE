print("="*10, "QUESTAO 05", "="*10)
valor_compra = float(input("Digite o valor da compra: "))
print("="*32)
if valor_compra >= 0:
  if valor_compra <= 100:
    print("Cachsback de 4%")
    valor_desconto = valor_compra * 0.96
    print("="*32)
    print(f"O valor final da compra foi: R$ {valor_desconto:.2f}")
    print("="*32)
  elif (valor_compra > 100) and (valor_compra <= 200):
    print("Cachsback de 6%")
    print("="*32) 
    valor_desconto = valor_compra * 0.94
    print(f"O valor final da compra foi: R$ {valor_desconto:.2f}")
    print("="*32)
  elif (valor_compra >= 201) and (valor_compra <= 400):
    print("Cachsback de 8%")
    print("="*32)
    valor_desconto = valor_compra * 0.92
    print(f"O valor final da compra foi: R$ {valor_desconto:.2f}")
    print("="*32)
  elif valor_compra > 400:
    print("Cachsback de 10%")
    print("="*32)
    valor_desconto = valor_compra * 0.90
    print(f"O valor final da compra foi: R$ {valor_desconto:.2f}")
    print("="*32)
else:
  print("Digite um número positivo")
  print("="*32)