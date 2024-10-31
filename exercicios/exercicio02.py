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

print("="*10, "QUESTAO 04", "="*10)
n1 = int(input("Digite um número inteiro positivo: "))
print("="*32)
if n1 >= 0:
  n2 = int(input("Digite o segundo número inteiro positivo: ")) 
  print("="*32)   
  if n2 >= 0:
    n3 = int(input("Digite o terceiro número inteiro positivo: "))
    print("="*32)
    if n3 >= 0:
      if (n1 == n2) and (n2 == n3):
        print("Todos os números são iguais")
        print("="*32)
      else:
        print("Os números são diferentes")
        print("="*32)
    else:
      print("Digite um número positivo")
      print("="*32)
  else:
    print("Digite um número positivo")
    print("="*32)
else:
  print("Digite um número positivo")
  print("="*32)

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
  
print("="*10, "QUESTAO 06", "="*10)
tabela_meses_trinta_um = [
  ["JAN, MAR, MAI, JUL, AGO, OUT, DEZ", 31],
]

tabela_meses_vinte_nove = [
  ["FEV", 29],
]

tabela_meses_trinta = [
  ["ABR, JUN, SET, NOV", 30]
]

cabecalhos = ["MÊS/MESES", "DIAS"]

jan = 1
fev = 2
mar = 3
abr = 4
mai = 5
jun = 6
jul = 7
ago = 8
set = 9
out = 10
nov = 11
dez = 12

mes_escolhido = int(input("Digite o mês no qual você quer ver os dias: "))

if (mes_escolhido < 1) or (mes_escolhido > 12):
  print("Digite um mês válido")
elif (mes_escolhido == 1) or (mes_escolhido == 3) or (mes_escolhido == 5) or (mes_escolhido == 7) or (mes_escolhido == 8) or (mes_escolhido == 10) or (mes_escolhido == 12):
  print(f"+{"="*5}+{"="*35}+")
  print(f"|{cabecalhos[1]:<5}|{cabecalhos[0]:<35}|")
  print(f"+{"="*5}+{"="*35}+")
  for linha in tabela_meses_trinta_um:
    print(f"|{linha[1]:<5}|{linha[0]:<35}|")
    print(f"+{"="*5}+{"="*35}+")
elif (mes_escolhido == 2):
  print(f"+{"="*5}+{"="*35}+")
  print(f"|{cabecalhos[1]:<5}|{cabecalhos[0]:<35}|")
  print(f"+{"="*5}+{"="*35}+")
  for linha in tabela_meses_vinte_nove:
    print(f"|{linha[1]:<5}|{linha[0]:<35}|")
    print(f"+{"="*5}+{"="*35}+")
    
elif (mes_escolhido == 4) or (mes_escolhido == 6) or (mes_escolhido == 9) or (mes_escolhido == 11):
  print(f"+{"="*5}+{"="*35}+")
  print(f"|{cabecalhos[1]:<5}|{cabecalhos[0]:<35}|")
  print(f"+{"="*5}+{"="*35}+")
  for linha in tabela_meses_trinta:
    print(f"|{linha[1]:<5}|{linha[0]:<35}|")
    print(f"+{"="*5}+{"="*35}+")