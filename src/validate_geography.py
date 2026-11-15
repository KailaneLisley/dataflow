import csv
from collections import Counter

arquivo = "data/raw/DENGBR20.csv"

# Códigos oficiais das 27 unidades federativas.
ufs_validas = {
    "11", "12", "13", "14", "15", "16", "17",
    "21", "22", "23", "24", "25", "26", "27",
    "28", "29", "31", "32", "33", "35", "41",
    "42", "43", "50", "51", "52", "53"
}

total_registros = 0
ufs = Counter()

municipios_ausentes = 0
ufs_invalidas = Counter()
municipios_com_codigo_invalido = 0
inconsistencias_geograficas = 0

# Guardamos poucos exemplos para investigar depois.
exemplos_inconsistencias = []

with open(arquivo, "r", encoding="latin1", newline="") as file:

    leitor = csv.reader(file, delimiter=",")

    cabecalho = next(leitor)

    # Descobre as posições das colunas.
    pos_uf = cabecalho.index("SG_UF")
    pos_municipio = cabecalho.index("ID_MN_RESI")

    for numero_linha, linha in enumerate(leitor, start=2):

        if not linha or len(linha) != len(cabecalho):
            continue

        total_registros += 1

        uf = linha[pos_uf].strip()
        municipio = linha[pos_municipio].strip()

        # Conta os registros por UF.
        if uf:
            ufs[uf] += 1

        # Verifica se o código da UF é válido.
        if uf not in ufs_validas:
            ufs_invalidas[uf] += 1

        # Verifica se o município está ausente.
        if not municipio:
            municipios_ausentes += 1
            continue

        # Verifica se o código municipal possui seis dígitos.
        if len(municipio) != 6 or not municipio.isdigit():
            municipios_com_codigo_invalido += 1
            continue

        # Compara os dois primeiros dígitos do município
        # com o código da UF de residência.
        if uf and municipio[:2] != uf:

            inconsistencias_geograficas += 1

            if len(exemplos_inconsistencias) < 10:
                exemplos_inconsistencias.append(
                    (numero_linha, uf, municipio)
                )


print("\n===== VALIDAÇÃO GEOGRÁFICA =====")

print(f"Registros analisados: {total_registros}")

print("\nCódigos de UF encontrados:")
for uf, quantidade in sorted(ufs.items()):
    print(f"{uf}: {quantidade}")

print(f"\nQuantidade de UFs encontradas: {len(ufs)}")
print(f"Códigos de UF inválidos: {sum(ufs_invalidas.values())}")
print(f"Municípios ausentes: {municipios_ausentes}")
print(
    "Códigos municipais com formato inválido:",
    municipios_com_codigo_invalido
)
print(
    "Inconsistências entre UF e município:",
    inconsistencias_geograficas
)

print("\nExemplos de inconsistências:")
for exemplo in exemplos_inconsistencias:
    print(exemplo)
