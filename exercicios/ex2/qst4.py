print("="*10, "QUESTAO 04", "="*10)
n1 = int(input("Digite um número inteiro positivo: "))
print("="*32)
if n1 >= 0:
  n2 = int(input("Digite o segundo número inteiro positivo: ")) 
  print("="*32)   
  if n2 >= 0:
    n3 = int(input("Digite o terceiro número inteiro positivo: "))
    print("="*32)
    if n3 >= 0:
      if (n1 == n2) and (n2 == n3):
        print("Todos os números são iguais")
        print("="*32)
      else:
        print("Os números são diferentes")
        print("="*32)
    else:
      print("Digite um número positivo")
      print("="*32)
  else:
    print("Digite um número positivo")
    print("="*32)
else:
  print("Digite um número positivo")
  print("="*32)