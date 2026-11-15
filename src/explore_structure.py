import csv
from collections import Counter

arquivo = "data/raw/DENGBR20.csv"

# Contadores: armazenam apenas os resultados das análises.
quantidade_registros = 0
quantidade_campos = Counter()
quantidade_ufs = Counter()
campos_ausentes = Counter()

# Guardaremos apenas alguns exemplos de linhas inconsistentes.
linhas_inconsistentes = []

# Campos que queremos observar quanto à ausência de valores.
campos_importantes = [
    "DT_NOTIFIC",
    "DT_SIN_PRI",
    "SG_UF",
    "ID_MN_RESI"
]

with open(arquivo, "r", encoding="latin1", newline="") as file:

    leitor = csv.reader(file, delimiter=",")

    # Lê o cabeçalho.
    cabecalho = next(leitor)

    # Descobre a posição de cada campo pelo nome.
    posicoes = {
        campo: cabecalho.index(campo)
        for campo in campos_importantes
    }

    # Verifica se existem nomes de colunas duplicados.
    colunas_duplicadas = [
        nome for nome, quantidade in Counter(cabecalho).items()
        if quantidade > 1
    ]

    # Percorre os registros restantes, um por vez.
    for numero_registro, linha in enumerate(leitor, start=2):

        # Ignora linhas completamente vazias.
        if not linha:
            continue

        quantidade_registros += 1

        # Conta quantos campos existem em cada registro.
        quantidade_campos[len(linha)] += 1

        # Verifica se a quantidade de campos é diferente
        # da quantidade de colunas do cabeçalho.
        if len(linha) != len(cabecalho):

            if len(linhas_inconsistentes) < 10:
                linhas_inconsistentes.append(
                    (numero_registro, len(linha))
                )

            # Não tenta analisar os campos de uma linha desalinhada.
            continue

        # Conta os valores ausentes nos campos selecionados.
        for campo, posicao in posicoes.items():
            if linha[posicao].strip() == "":
                campos_ausentes[campo] += 1

        # Conta os registros por UF de residência.
        uf = linha[posicoes["SG_UF"]].strip()

        if uf:
            quantidade_ufs[uf] += 1


# Exibe os resultados.
print("\n===== ESTRUTURA DO ARQUIVO =====")

print(f"Quantidade de colunas: {len(cabecalho)}")
print(f"Quantidade de registros: {quantidade_registros}")

print("\nDistribuição da quantidade de campos:")
for quantidade, frequencia in sorted(quantidade_campos.items()):
    print(f"{quantidade} campos: {frequencia} registros")

print("\nLinhas inconsistentes:")
print(linhas_inconsistentes)

print("\nColunas duplicadas:")
print(colunas_duplicadas)

print("\n===== VALORES AUSENTES =====")

for campo in campos_importantes:
    print(f"{campo}: {campos_ausentes[campo]}")

print("\n===== DISTRIBUIÇÃO POR UF DE RESIDÊNCIA =====")

for uf, quantidade in sorted(quantidade_ufs.items()):
    print(f"UF {uf}: {quantidade} registros")
