qtd = int(input("Digite a quantidade de linhas: "))

if qtd >= 2:
  for i in range(qtd):
    print("*" * (i + 1))
else:
  print("A quantidade de linhas deve ser maior ou igual a 2")