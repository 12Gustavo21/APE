countSim = 0
countNao = 0
countInvalidos = 0

for i in range(80):
  voto = input("Digite seu voto: ")
  if voto == "SIM":
    countSim += 1
  elif voto == "NAO":
    countNao += 1
  else:
    countInvalidos += 1
    
total = countSim + countNao + countInvalidos

print(f"Votos Sim: {((total - countSim) / total) * 100:.2f}%")
print(f"Votos Nao: {(countNao / total) * 100:.2f}%")
print(f"Votos Invalidos: {(countInvalidos / total) * 100:.2f}%")