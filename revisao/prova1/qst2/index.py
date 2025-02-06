qnt_cupom = 0
print("="*32)
valor_compra = float(input("Digite o valor da sua compra: "))

print("="*32)
if valor_compra >= 30:
    qnt_cupom = valor_compra // 30
    print(f"{qnt_cupom} cupons")
    saldo = valor_compra - qnt_cupom * 30
    print("="*32)
    print(f"R$ {saldo} de saldo")
    print("="*32)
    falta_novo_cupom = 30 - saldo
    print(f"R$ {falta_novo_cupom} para um novo cupom")
else:
    print("sem cupons")
    print("="*32)
    saldo = valor_compra - qnt_cupom * 30
    print(f"{saldo} de saldo")
    print("="*32)
    print(f"R$ {(30 - valor_compra):.2f} para um novo cupom")
print("="*32)