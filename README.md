# DataFlow

Projeto prático de estudo em Ciência de Dados e Engenharia de Dados, utilizando dados públicos de saúde para construir, passo a passo, um fluxo de análise reproduzível.

## Objetivo

Explorar como dados públicos podem ser coletados, inspecionados, processados e transformados em informações úteis, desenvolvendo conhecimentos em Python, análise exploratória, estatística e organização de dados.

## Estudo de caso: SINAN/Dengue

O primeiro estudo utiliza dados de notificações de dengue do Sistema de Informação de Agravos de Notificação (SINAN), disponibilizados pelo Ministério da Saúde.

**Escopo definido:**
- **Tema:** Dengue e saúde pública.
- **Fonte:** Ministério da Saúde — SINAN.
- **Recorte geográfico:** residentes em Pernambuco.
- **Período planejado:** 2020 a 2025.
- **Abordagem inicial:** análise exploratória de dados.

A seleção geográfica considera a UF de residência (`SG_UF`), e não a UF da unidade notificadora. Essa distinção é importante para evitar interpretações incorretas dos registros.

Fonte: [Dados Abertos do SUS — Arboviroses/Dengue](https://dadosabertos.saude.gov.br/dataset/arboviroses-dengue).

## Etapas do projeto

- [x] Definição da fonte de dados e do recorte de estudo.
- [x] Consulta ao dicionário de dados.
- [x] Inspeção estrutural inicial do arquivo de 2020.
- [ ] Comparação estrutural dos arquivos de 2021 a 2025.
- [ ] Seleção e organização dos registros de residentes em Pernambuco.
- [ ] Limpeza e preparação dos dados.
- [ ] Análise exploratória e estatística.
- [ ] Construção de visualizações e indicadores.
- [ ] Avaliação de possibilidades de aplicação de Machine Learning.

As etapas serão desenvolvidas gradualmente, priorizando a compreensão dos dados, a documentação das decisões e a reprodutibilidade do processo.

## Tecnologias e ferramentas

- **Python:** leitura e inspeção dos dados.
- **CSV:** leitura de arquivos e análise estrutural inicial.
- **Git e GitHub:** versionamento, documentação e acompanhamento das etapas.
- **Pandas e SQL:** ferramentas previstas para etapas posteriores.

## Estrutura do projeto

```text
dataflow/
├── data/
│   ├── raw/          # Dados originais, mantidos localmente
│   └── processed/    # Dados após tratamento
├── notebooks/        # Exploração e análises
├── src/              # Scripts Python
├── tests/            # Testes
└── README.md
```

Os dados brutos não são versionados no Git, permanecendo preservados localmente.

## Status

Em desenvolvimento. A inspeção estrutural inicial da base de 2020 foi concluída. O próximo passo é verificar a estrutura dos arquivos dos demais anos e identificar possíveis diferenças antes de integrar os dados.

---

Projeto pessoal de aprendizagem, com foco na aplicação de Ciência de Dados a problemas de saúde pública.