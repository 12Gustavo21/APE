import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))


# Registros encontrados no arquivo
def registros(file: str) -> list:
    arq = open(file, "r", encoding="utf-8")
    lista = arq.read().splitlines()
    arq.close()
    # A primeira linha contém o cabeçalho de cada campo.
    # Retornar a partir da segunda linha
    return lista[1:]


# Quantidade de registros
def quantidade_registros(registros: list) -> int:
    return len(registros)


# Relação dos Campi da Instituição.
def campi(registros: list) -> list:
    campus = []
    for itens in registros:
        campi = itens.split(';')[4].replace('"','')  
        if campi not in campus:
            campus.append(campi)
    return campus


# Relação dos Cursos de um determinado Campus.
def cursos(registros: list, nome_campus: str) -> list:
    cursos = []
    for linha in registros:
        if nome_campus in linha:
            item = linha.split(";")[6].replace('"', "")
            if item not in cursos:
                cursos.append(item)
    return cursos


# Maior nota da instituição
def maior_nota_instituicao(registros: list) -> float:
    notas_instituicao = []
    for registro in registros:
        nota = registro.split(";")[16]
        nota_nova = float(nota.replace('"', "").replace(",", "."))
        notas_instituicao.append(nota_nova)
    maior_nota = max(notas_instituicao)
    return maior_nota


# Maior nota do Campus
def maior_nota_campus(registros: list, nome_campus: str) -> float:
    notas_campus = []
    for registro in registros:
        if nome_campus in registro:
            nota = registro.split(";")[16]
            nota_nova = float(nota.replace('"', "").replace(",", "."))
            notas_campus.append(nota_nova)
    maior_nota = max(notas_campus)
    return maior_nota


# Maior nota de um Curso
def maior_nota_curso(registros: list, codigo_curso: int) -> float:
    notas_curso = []
    for linha in registros:
        if codigo_curso == int(linha.split(';')[5].replace('"','')):
            nota = linha.split(';')[16].replace('"', '').replace(',', '.')
            notas_curso.append(nota)
    maior_nota = max(notas_curso)
    return float(maior_nota)


# Maior nota de corte da instituição
def maior_nota_corte_instituicao(registros: list) -> float:
    notas_instituicao = []
    for registro in registros:
        nota = registro.split(";")[17]
        nota_nova = float(nota.replace('"', "").replace(",", "."))
        notas_instituicao.append(nota_nova)
    maior_nota = max(notas_instituicao)
    return maior_nota   


# Maior nota do Campus
def maior_nota_corte_campus(registros: list, nome_campus: str) -> float:
    notas_campus = []
    for registro in registros:
        if nome_campus in registro:
            nota = registro.split(";")[17]
            nota_nova = float(nota.replace('"', "").replace(",", "."))
            notas_campus.append(nota_nova)
    maior_nota = max(notas_campus)
    return maior_nota


# Maior nota de um Curso
def maior_nota_corte_curso(registros: list, codigo_curso: int) -> float:
    notas_curso = []
    for linha in registros:
        if codigo_curso == int(linha.split(';')[5].replace('"','')):
            nota = linha.split(';')[17].replace('"', '').replace(',', '.')
            notas_curso.append(nota)
    maior_nota = max(notas_curso)
    return float(maior_nota)


# Retorna o código de um determinado curso de um determinado campus
def codigo_curso(registros: list, nome_campus: str, nome_curso: str) -> int:
    for itens in registros:
        if nome_campus in itens and nome_curso in itens:
            cod = itens.split(";")[5]
            novo_cod = int(cod.replace('"', "").replace(",", "."))
            return novo_cod