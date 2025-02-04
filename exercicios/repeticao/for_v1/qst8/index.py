valor_total = 0
valor_total_cashback = 0

for i in range(400):
  valor_compra = int(input("Digite o valor da compra: "))
  
  if valor_compra <= 100:
    valor_desconto = valor_compra * 0.96
  elif valor_compra > 100 and valor_compra <= 200:
    valor_desconto = valor_compra * 0.94
  elif valor_compra > 200 and valor_compra <= 400:
    valor_desconto = valor_compra * 0.92
  elif valor_compra > 400:
    valor_desconto = valor_compra * 0.90
    
  valor_total += valor_desconto
  valor_total_cashback += valor_compra - valor_desconto
  
print(f"Valor total arrecadado: {valor_total}")
print(f"Valor total de cashback gerado: {valor_total_cashback:.2f} reais")