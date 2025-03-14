def ip(registro:str) -> str:
  partes = registro.strip().split()
  return partes[0] if partes else ""

def dia(registro:str) -> int:
  partes = registro.strip().split()
  return int(partes[3][1:3]) if partes else ""

def ips(registros:list) -> list:
  ips_unicos = []

  for item in registros:
      current_ip = ip(item)
      if current_ip and current_ip not in ips_unicos:
          ips_unicos.append(current_ip)

  return ips_unicos

def dia_maior_ataque(registros: list) -> list:
  dias = []
  contagens = []
  
  for i in range(len(registros)):
    if dia(registros[i]) in dias:
      i = dias.index(dia(registros[i]))
      contagens[i] += 1
    else:
      dias.append(dia(registros[i]))
      contagens.append(1)
  
  max_freq = max(contagens)
  
  mais_frequentes = [dias[i] for i in range(len(dias)) if contagens[i] == max_freq]
  
  return mais_frequentes

def dia_menor_ataque(registros: list) -> list:
  dias = []
  contagens = []
  
  for i in range(len(registros)):
    if dia(registros[i]) in dias:
      i = dias.index(dia(registros[i]))
      contagens[i] += 1
    else:
      dias.append(dia(registros[i]))
      contagens.append(1)
  
  min_freq = min(contagens)
  
  mais_frequentes = [dias[i] for i in range(len(dias)) if contagens[i] == min_freq]
  
  return mais_frequentes

def linhas(len: int):
  print("="*len)