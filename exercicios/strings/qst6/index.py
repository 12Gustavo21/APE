frase = input()
palavra = "Python"

count = 0

for letra in frase:
  if letra in palavra:
    count += 1

print(count)