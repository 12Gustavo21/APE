print("="*10, "QUESTAO 10", "="*10)

idade = int(input("Digite a idade 1: "))
mais_velha = idade
mais_nova = idade

for i in range(39):
  idade = int(input(f"Digite a idade {i+2}: "))
  if idade > mais_velha:
    mais_velha = idade
  if idade < mais_nova:
    mais_nova = idade

print("="*32)

print(f"A pessoa mais velha tem {mais_velha} anos")
print(f"A pessoa mais nova tem {mais_nova} anos")

print("="*32)