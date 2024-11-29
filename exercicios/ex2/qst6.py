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