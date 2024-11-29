print("="*10, "QUESTAO 08", "="*10)

valor_total_compra = 0
valor_total_cashback = 0

for i in range(400):
  valor_compra = float(input("Digite o valor da compra: "))
  print("="*32)
  if valor_compra <= 100:
      print("Cashback de 4%")
      valor_total_cashback += 4
      valor_desconto = valor_compra * 0.96
      valor_total_compra += valor_desconto
      print("="*32)
      print(f"O valor final da compra foi: R$ {valor_desconto:.2f}")
      print("="*32)
  elif valor_compra <= 200:
      print("Cashback de 6%")
      valor_total_cashback += 6
      valor_desconto = valor_compra * 0.94
      valor_total_compra += valor_desconto
      print("="*32)
      print(f"O valor final da compra foi: R$ {valor_desconto:.2f}")
      print("="*32)
  elif valor_compra <= 400:
      print("Cashback de 8%")
      valor_total_cashback += 8
      valor_desconto = valor_compra * 0.92
      valor_total_compra += valor_desconto
      print("="*32)
      print(f"O valor final da compra foi: R$ {valor_desconto:.2f}")
      print("="*32)
  else:
      print("Cashback de 10%")
      valor_total_cashback += 10
      valor_desconto = valor_compra * 0.90
      valor_total_compra += valor_desconto
      print("="*32)
      print(f"O valor final da compra foi: R$ {valor_desconto:.2f}")
      print("="*32)

print(f"Valor total arrecadado: {valor_total_compra}")
print("="*32)
print(f"Valor total de cashback gerado: {valor_total_cashback}%")
print("="*32)