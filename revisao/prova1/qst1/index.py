import math

qnt_cupom = 0
print("="*32)
valor_compra = float(input("Digite o valor da sua compra: "))

print("="*32)
if valor_compra >= 30:
    qnt_cupom = valor_compra / 30

print(f"{math.floor(qnt_cupom)} cupons")
print("="*32)