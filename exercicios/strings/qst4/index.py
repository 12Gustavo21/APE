alfanumerico = input()
novastring = ""

for char in alfanumerico:
  if char.isdigit():
    novastring += "*"
  else:
    novastring += char
    
print(novastring)