mediaSemestral = int(input("Digite sua media semestral: "))
notaFinal = int(input("Digite sua nota final: "))

mediaFinal = ((mediaSemestral * 6) + (notaFinal * 4)) / 10
print(f"Sua nota final é: {mediaFinal}")