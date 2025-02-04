valor_compra = int(input("Digite o valor da compra: "))

if valor_compra <= 100:
  valor_desconto = valor_compra * 0.96
elif valor_compra > 100 and valor_compra <= 200:
  valor_desconto = valor_compra * 0.94
elif valor_compra > 200 and valor_compra <= 400:
  valor_desconto = valor_compra * 0.92
elif valor_compra > 400:
  valor_desconto = valor_compra * 0.90
  
print(f"{valor_desconto:.2f}")