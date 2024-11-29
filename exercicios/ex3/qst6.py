print("="*10, "QUESTAO 06", "="*10)

soma = 0
for i in range(6):
  nota = int(input(f"Digite a nota {i + 1}: "))
  soma += nota

media = soma / 6
print(f"Média: {media:.2f}")
print("="*32)