print("="*10, "QUESTAO 07", "="*10)
count = 0

for i in range(8):
  nota = int(input(f"Digite a nota {i + 1}: "))
  if nota >= 0 and nota <= 100:
    count += 1
    
print(f"Foram informadas {count} notas válidas para o Suap")
print("="*32)