
import csv

arquivo = "data/raw/DENGBR20.csv"

# Números das linhas identificadas na execução anterior.
linhas_interesse = {35772, 304668, 1143685, 1391878}

with open(arquivo, "r", encoding="latin1", newline="") as file:

    leitor = csv.reader(file, delimiter=",")

    cabecalho = next(leitor)

    for numero_linha, linha in enumerate(leitor, start=2):

        if numero_linha in linhas_interesse:

            print(f"\n===== LINHA {numero_linha} =====")

            # Exibe todos os campos preenchidos.
            for nome, valor in zip(cabecalho, linha):
                if valor.strip():
                    print(f"{nome}: {valor}")

            print("-" * 40)
