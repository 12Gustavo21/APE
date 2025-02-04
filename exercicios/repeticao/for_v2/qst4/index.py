n = int(input("Digite o valor de n: "))

primo = False

for i in range(n):
  if n % (i+1) == 0:
    primo = True

if primo == True:
  print(f"{n} é primo")
else:
  print(f"{n} não é primo")