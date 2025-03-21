'''
    Nome: lib_vogais
    Descrição: Biblioteca para manipulação de vogais em textos.
    Autores: Valéria Cavalcanti, Gustavo Almeida
    Data: 27/02/2025
    Versão: 1.0
'''

import random
vogais = "aeiouAEIOU"

# Verifica se um determinado símbolo é vogal.
def eh_vogal(simbolo: str) -> bool:
    return simbolo in vogais and len(simbolo) > 0

# Verifica se um texto é formado apenas por vogais.
def eh_texto_vogal(texto: str) -> bool:
    if len(texto) > 0:
        so_vogais = True
        for i in range(len(texto)):
            if eh_vogal(texto[i]) != True:
                so_vogais = False
                break
        return so_vogais
    else:
        return False

# Retorna a quantidade de vogais em um texto.
def quantidade_vogais(texto: str) -> int:
    if len(texto) > 0:
        qtd = 0
        for i in range(len(texto)):
            if eh_vogal(texto[i]):
                qtd += 1
        return qtd
    else:
        return 0

# Remove as vogais de um texto.
def remove_vogais(texto:str) -> str:
    if len(texto) > 0:
        if quantidade_vogais(texto) > 0:
            novo_texto = ""
            for i in range(len(texto)):
                if eh_vogal(texto[i]) != True:
                    novo_texto += texto[i]
            return novo_texto
        else:
            return "Texto ficou/não tem vogal"
    else:
        return ""

# Identifica as vogais que estão presentes em um texto.
def identifica_vogais(texto: str) -> list:
    if len(texto) > 0:
        novo_texto = []
        for i in range(len(texto)):
            if eh_vogal(texto[i]) == True:
                novo_texto.append(texto[i])
        return novo_texto
    else:
        return []

# Frequêcia de vogais em um texto.
def frequencia_vogais(texto: str) -> list:
    if len(texto) > 0:
        frequenciaA = 0
        frequenciaE = 0
        frequenciaI = 0
        frequenciaO = 0
        frequenciaU = 0
        for i in range(len(texto)):
            if (texto[i] == "a" or texto[i] == "A"):
                frequenciaA += 1
            elif (texto[i] == "e" or texto[i] == "E"):
                frequenciaE += 1
            elif (texto[i] == "i" or texto[i] == "I"):
                frequenciaI += 1
            elif (texto[i] == "o" or texto[i] == "O"):
                frequenciaO += 1
            elif (texto[i] == "u" or texto[i] == "u"):
                frequenciaU += 1
        frequencia = []
        frequencia.append(frequenciaA)
        frequencia.append(frequenciaE)
        frequencia.append(frequenciaI)
        frequencia.append(frequenciaO)
        frequencia.append(frequenciaU)
        if sum(frequencia) != 0:
            return frequencia   
        else:
            return []
    else:
        return []

# Substitui as vogais de um texto por * (asterísco).
def substitui_vogais(texto: str) -> str:
    if len(texto) > 0:
        novastring = ""
        for char in texto:
            if eh_vogal(char):
                novastring += "*"
            else:
                novastring += char
        return novastring
    else:
        return ""

# Identifica a vogal que mais aparece em um texto. Pode haver mais de uma vogal com a mesma frequência.
def vogal_mais_frequente(texto: str) -> list:
    if len(texto) > 0 and sum(frequencia_vogais(texto)) != 0:
        frequencia = frequencia_vogais(texto)
        max_freq = max(frequencia)
        mais_frequentes = []
        for i in range(len(frequencia)):
            if frequencia[i] == max_freq and i == 0:
                mais_frequentes.append("a")
            elif frequencia[i] == max_freq and i == 1:
                mais_frequentes.append("e")
            elif frequencia[i] == max_freq and i == 2:
                mais_frequentes.append("i")
            elif frequencia[i] == max_freq and i == 3:
                mais_frequentes.append("o")
            elif frequencia[i] == max_freq and i == 4:
                mais_frequentes.append("u")
        return mais_frequentes
    else:
        return []

# Sortear uma vogal.
def sortear_vogal(texto: str) -> str:
    if len(texto) != 0:
        vogais_presentes = identifica_vogais(texto)
        if len(vogais_presentes) != 0:
            aleatorio = random.randint(0, len(vogais_presentes)-1)
            return vogais_presentes[aleatorio]
        else:
            return ""
    else:
        return ""