print("="*8, "QUESTAO 02 e 03", "="*7)
nome01 = input("Digite seu nome: ")
print("="*32)
idade01 = int(input("Digite sua idade: "))
if idade01 >= 0:
  print("="*32)
  nome02 = input("Digite seu nome: ")
  print("="*32)
  idade02 = int(input("Digite sua idade: "))
  print("="*32)
  if idade02 >= 0:
    if idade01 > idade02:
      print(f"{nome01} é a pessoa mais velha")
    elif idade01 == idade02:
      print(f"As pessoas {nome01} e {nome02} tem a mesma idade")
    else:
      print(f"{nome02} é a pessoa mais velha")
  else:
    print("Digite um número positivo")   
else:
  print("="*32)
  print("Digite um número positivo")
print("="*32)