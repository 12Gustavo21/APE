print("="*10, "QUESTAO 09", "="*10)

count_sim = 0
count_nao = 0
count_invalidos = 0

for i in range(4):
  voto = input("Digite seu voto (SIM/NAO): ")
  if voto == "SIM":
    count_sim += 1
  elif voto == "NAO":
    count_nao += 1
  else:
    count_invalidos += 1
    
sim_porcentagem = (count_sim / 4) * 100
nao_porcentagem = (count_nao / 4) * 100
invalidos_porcentagem = (count_invalidos / 4) * 100
    
print("="*32)
print(f"Votos (SIM) foram: {sim_porcentagem}%")
print(f"Votos (NAO) foram: {nao_porcentagem}%")
print(f"Votos invalidos foram: {invalidos_porcentagem}%")
print("="*32)