
import csv
from collections import Counter

arquivo = "data/raw/DENGBR20.csv"

# Contadores para resumir os registros sem município de residência
total_sem_municipio = 0
ausencias_por_uf = Counter()
classificacoes = Counter()
registros_pernambuco = 0

# Campos que ajudam a entender cada ocorrência
campos_interesse = [
    "DT_NOTIFIC",
    "DT_SIN_PRI",
    "SG_UF",
    "ID_MN_RESI",
    "SG_UF_NOT",
    "ID_MUNICIP",
    "CLASSI_FIN",
    "EVOLUCAO"
]

exemplos = []

with open(arquivo, "r", encoding="latin1", newline="") as file:
    leitor = csv.reader(file, delimiter=",")
    cabecalho = next(leitor)

    # Relaciona o nome de cada campo à sua posição no CSV
    posicoes = {
        campo: cabecalho.index(campo)
        for campo in campos_interesse
    }

    for numero_linha, linha in enumerate(leitor, start=2):

        # Ignora linhas vazias ou estruturalmente inconsistentes
        if not linha or len(linha) != len(cabecalho):
            continue

        municipio = linha[posicoes["ID_MN_RESI"]].strip()

        # A análise considera somente registros sem município de residência
        if municipio == "":
            total_sem_municipio += 1

            uf = linha[posicoes["SG_UF"]].strip()
            classificacao = linha[posicoes["CLASSI_FIN"]].strip()

            ausencias_por_uf[uf or "VAZIO"] += 1
            classificacoes[classificacao or "VAZIO"] += 1

            if uf == "26":
                registros_pernambuco += 1

            # Guarda os campos relevantes para inspeção individual
            registro = {
                campo: linha[posicoes[campo]]
                for campo in campos_interesse
            }

            exemplos.append((numero_linha, registro))


print("=== RESUMO DOS MUNICÍPIOS AUSENTES ===")
print(f"Total de registros sem ID_MN_RESI: {total_sem_municipio}")
print(f"Registros com SG_UF = 26 (Pernambuco): {registros_pernambuco}")

print("\n=== AUSÊNCIAS POR UF DE RESIDÊNCIA ===")
for uf, quantidade in sorted(ausencias_por_uf.items()):
    print(f"{uf}: {quantidade}")

print("\n=== CLASSIFICAÇÃO FINAL ===")
for classificacao, quantidade in sorted(classificacoes.items()):
    print(f"{classificacao}: {quantidade}")

print("\n=== DETALHAMENTO DOS REGISTROS ===")
for numero_linha, registro in exemplos:
    print(f"\nLinha {numero_linha}:")
    for campo, valor in registro.items():
        print(f"  {campo}: {valor}")
