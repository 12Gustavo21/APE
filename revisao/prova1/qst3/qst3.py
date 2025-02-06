qnt_cupom = 0
valor_total_vendas = 0
qnt_total_cupons = 0
maior_valor = -1
cupons_maior_valor = -1

for i in range(200):
    print("="*32)
    valor_compra = float(input("Digite o valor da sua compra: "))
    valor_total_vendas += valor_compra

    print("="*32)
    if valor_compra >= 30:
        qnt_cupom = valor_compra // 30
        qnt_total_cupons += qnt_cupom
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
        print(f"R$ {(30 - valor_compra):.2f} para um novo cupom")

    if valor_compra > maior_valor:
        maior_valor = valor_compra
        cupons_maior_valor = qnt_cupom
        

print("="*32)
print(f"valor total de vendas: {valor_total_vendas:.2f}")
print("="*32)
print(f"total de cupons distribuidos: {qnt_total_cupons}")
print("="*32)
print(f"maior compra: {maior_valor} e {cupons_maior_valor} de cupons")
print("="*32)