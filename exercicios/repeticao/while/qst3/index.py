while True:
  x, y = list(map(int, input().split()))
  
  if x > 0 and y > 0:
    print("Primeiro")
  elif x < 0 and y > 0:
    print("Segundo")
  elif x < 0 and y < 0:
    print("Terceiro")
  elif x > 0 and y < 0:
    print("Quarto")
  elif x == 0 or y == 0:
    break