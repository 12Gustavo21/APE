import os
import lib

os.chdir(os.path.dirname(os.path.abspath(__file__)))

with open("access.log", "r") as arq:
  linhas = arq.readlines()

print(linhas[0])
print(lib.ip(linhas[0]))
print(lib.ip(linhas[300]))
print(lib.ip(linhas[600]))
print(lib.ip(linhas[900]))

lib.linhas(38)
print(lib.ips(linhas))
lib.linhas(38)
for i in range(len(lib.ips(linhas))):
  print(i+1, lib.ips(linhas)[i])

lib.linhas(38)
print(lib.dia(linhas[0]), type(lib.dia(linhas[0])))
print(lib.dia(linhas[300]), type(lib.dia(linhas[300])))
print(lib.dia(linhas[600]), type(lib.dia(linhas[600])))
print(lib.dia(linhas[900]), type(lib.dia(linhas[900])))

lib.linhas(38)
print(lib.dia_maior_ataque(linhas))
lib.linhas(38)
for i in range(len(lib.dia_maior_ataque(linhas))):
  print(i+1, lib.dia_maior_ataque(linhas)[i])


lib.linhas(38)
print(lib.dia_menor_ataque(linhas))
lib.linhas(38)
for i in range(len(lib.dia_menor_ataque(linhas))):
  print(i+1, lib.dia_menor_ataque(linhas)[i])