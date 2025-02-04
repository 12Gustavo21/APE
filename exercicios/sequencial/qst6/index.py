numero_mes = int(input("Digite o numero correspondente ao mes: "))

if numero_mes == 1 or numero_mes == 3 or numero_mes == 5 or numero_mes == 7 or numero_mes == 8 or numero_mes == 10 or numero_mes == 12:
  print("O mes digitado tem: ", 31, "dias")
elif numero_mes == 4 or numero_mes == 6 or numero_mes == 9 or numero_mes == 11:
  print("O mes digitado tem: ", 30, "dias")
elif numero_mes == 2:
  print("O mes digitado tem: ", 29, "dias")