countA = 0
countG = 0
countD = 0
while True:
  n = int(input())
  if n == 1:
    countA += 1
  if n == 2:
    countG += 1
  if n == 3:
    countD += 1
  if n == 4:
    break

print("MUITO OBRIGADO")
print(f"Alcool: {countA}")
print(f"Gasolina: {countG}")
print(f"Diesel: {countD}")