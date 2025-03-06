import random

# Gerar uma lista de tamanho n com valores aleatórios.
def gerar_lista(quantidade: int, menor_valor: int, maior_valor: int) -> list:
  lista = [random.randint(menor_valor, maior_valor) for _ in range(quantidade)]
  return lista

# Exibir os elementos da lista, um por linha.
def exibir_lista(lista: list):
  for i in range(len(lista)):
    print(lista[i])

# Calcular a média dos valores da lista.
def calcular_media(lista: list) -> float:
  media = sum(lista)/len(lista)
  return media

# Elementos com valores acima da média.
def elementos_acima_da_media(lista: list) -> list:
  acima_media =[]
  for i in range(len(lista)):
    if lista[i] > calcular_media(lista):
      acima_media.append(lista[i])
  return acima_media

# Elementos com valores abaixo da média.
def elementos_abaixo_da_media(lista: list) -> list:
  menor_media =[]
  for i in range(len(lista)):
    if lista[i] < calcular_media(lista):
      menor_media.append(lista[i])
  return menor_media

# Elementos com valores entre (inclusive) dois valores informados.
def elementos_entre_dois_valores(lista: list, valor1: int, valor2: int) -> list:
  valores = []
  for i in range(len(lista)):
    if (lista[i] >= valor1) and (lista[i] <= valor2):
      valores.append(lista[i])
    elif (lista[i] <= valor1) and (lista[i] >= valor2):
      valores.append(lista[i])
  return valores

# Elementos com valores fora de um intervalo informado.
def elementos_fora_de_um_intervalo(lista: list, valor1: int, valor2: int) -> list:
  valores = []
  for i in range(len(lista)):
    if valor1 > valor2:
      if (lista[i] > valor1) or (lista[i] < valor2):
        valores.append(lista[i])
    elif valor1 < valor2:
      if (lista[i] < valor1) or (lista[i] > valor2):
        valores.append(lista[i])
  return valores

# Elementos distintos da lista.
def elementos_distintos(lista: list) -> list:
  distintos = []
  for i in lista:
    if i not in distintos:
      distintos.append(i)
  return distintos

# Elemento mais frequente. Pode haver repetição.
def elemento_mais_frequente(lista: list) -> list:
  elementos = []
  contagens = []
  
  for nota in lista:
    if nota in elementos:
      i = elementos.index(nota)
      contagens[i] += 1
    else:
      elementos.append(nota)
      contagens.append(1)

  max_freq = max(contagens)
  
  mais_frequentes = [elementos[i] for i in range(len(elementos)) if contagens[i] == max_freq]
  
  return mais_frequentes

# Calcular a quantidade de elementos com valores acima da média.
def quantidade_elementos_acima_da_media(lista: list) -> int:
  qtd = len(elementos_acima_da_media(lista))
  return qtd

# Calcular a quantidade de elementos com valores abaixo da média.
def quantidade_elementos_abaixo_da_media(lista: list) -> int:
  qtd = len(elementos_abaixo_da_media(lista))
  return qtd

# Calcular a quantidade de elementos com valores entre (inclusive) dois valores informados.
def quantidade_elementos_entre_dois_valores(lista: list, menor_valor: int, maior_valor: int) -> int:
  qtd = len(elementos_entre_dois_valores(lista, menor_valor, maior_valor))
  return qtd

# Calcular a quantidade de elementos com valores fora de um intervalo informado.
def quantidade_elementos_fora_de_um_intervalo(lista: list, menor_valor: int, maior_valor: int) -> int:
  qtd = len(elementos_fora_de_um_intervalo(lista, menor_valor, maior_valor))
  return qtd

# Calcular a quantidade de elementos distintos da lista
def quantidade_elementos_distintos(lista: list) -> int:
  qtd = len(elementos_distintos(lista))
  return qtd