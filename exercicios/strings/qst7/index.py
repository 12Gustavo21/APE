palavras = {}

while True:
  text = input()
  if text == "fim":
    break
  elif text in palavras:
    palavras[text] += 1
  else:
    palavras[text] = 1

for valores in palavras.items():
  print(*valores)