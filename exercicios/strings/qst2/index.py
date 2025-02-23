text = input()

for char in text:
  unicode = ord(char)
  print(char, ord(char), bin(unicode), hex(unicode), oct(unicode))