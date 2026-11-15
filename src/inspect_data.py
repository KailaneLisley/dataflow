import csv

# Caminho do arquivo CSV dentro do projeto.
arquivo = "data/raw/DENGBR20.csv"

# open() abre o arquivo para leitura.
# encoding="latin1" define a codificação usada na leitura do texto.
# newline="" evita problemas na interpretação das quebras de linha.
# with garante que o arquivo seja fechado ao terminar o bloco.
with open(arquivo, "r", encoding="latin1", newline="") as file:

    # csv.reader() interpreta o conteúdo como um arquivo CSV.
    # delimiter="," informa que as colunas são separadas por vírgulas.
    leitor = csv.reader(file, delimiter=",")

    # next() pega o próximo registro do leitor.
    # A primeira linha do CSV contém os nomes das colunas.
    cabecalho = next(leitor)

    # A segunda linha contém o primeiro registro de dados.
    primeira_linha = next(leitor)

# len() retorna a quantidade de elementos de uma lista.
print(f"Quantidade de colunas no cabeçalho: {len(cabecalho)}")
print(f"Quantidade de campos na primeira linha: {len(primeira_linha)}")

# [:23] seleciona os primeiros 23 elementos de cada lista.
# zip() combina os nomes das colunas com seus respectivos valores.
print("\nPrimeiros 23 campos:")
for nome, valor in zip(cabecalho[:23], primeira_linha[:23]):
    print(f"{nome}: {valor}")

# Compara as quantidades de campos.
# Se forem iguais, a primeira linha tem a mesma quantidade
# de campos que o cabeçalho.
print("\nAs quantidades coincidem?",
      len(cabecalho) == len(primeira_linha))
