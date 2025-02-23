frase = input()

countMaisculas = 0
countMinusculas = 0
countNumericos = 0

for char in frase:
  if char.isupper():
    countMaisculas+=1
  elif char.islower():
    countMinusculas+=1
  elif char.isdigit():
    countNumericos+=1


print(countMaisculas)
print(countMinusculas)
print(countNumericos)