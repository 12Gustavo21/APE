n = int(input("Digite o valor de n: "))

calculo = 0
quadrado_perfeito = 0

for i in range(n):
  calculo = i ** 2
  if calculo <= n:
    quadrado_perfeito = calculo
  
print(f"O quadrado de {n} é: {quadrado_perfeito}")