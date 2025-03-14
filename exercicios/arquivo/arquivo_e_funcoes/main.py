import os
import lib

os.chdir(os.path.dirname(os.path.abspath(__file__)))

with open("access.log", "r") as arq:
  linhas = arq.readlines()

while True:
  lib.linhas(52)
  print("Olá! bem-vindo ao seu sistema de detecção de ataques")
  lib.linhas(52)
  print("Opção 01: Quantos IPs diferentes foram detectados")
  print("Opção 02: Qual dia houve maior número de ataques")
  print("Opção 03: Qual dia houve menor número de ataques")
  print("Opção 04: Sair")
  lib.linhas(52)
  print("O que seja consultar hoje?")
  opcao = int(input("Digite aqui uma opção: "))
  if opcao < 1 or opcao > 4:
    lib.linhas(52)
    print("Digite uma opção válida")
    break
  elif opcao == 4:
      break
  else:
    if opcao == 1:
      lib.linhas(52)
      print(f"A quantidade de IPs detectados foram: {len(lib.ips(linhas))}")
    elif opcao == 2:
      lib.linhas(52)
      print("O dia que houve mais ataques foi:", *lib.dia_maior_ataque(linhas))
    elif opcao == 3:
      lib.linhas(52)
      print("O dia que houve menos ataques foi:", *lib.dia_menor_ataque(linhas))
    lib.linhas(52)
    continuar = input("Deseja continuar? (S/N): ")
    if continuar[0].lower() == "s":
      continue
    else:
      break
lib.linhas(52)