# Projeto 4 — Painel Interativo do Censo Escolar em Python

**Objetivo:** painel interativo, feito com pandas e Streamlit, que mostra as escolas em atividade de 30 municípios de quatro regiões do estado de São Paulo (Região Metropolitana de SP, Baixada Santista, Litoral Norte e Vale do Ribeira) a partir do Censo Escolar 2024. Permite comparar regiões, municípios e redes de ensino quanto ao porte, à localização e à infraestrutura das escolas (água e esgoto), e ver onde elas estão no mapa. É a versão em Python do painel feito em Excel no Projeto 2.

## Como usar

**1. O que é preciso ter instalado:** Python 3 e os pacotes pandas e Streamlit:

```
python -m pip install pandas streamlit
```

**2. Como rodar:** abra o terminal na pasta do projeto, a mesma onde estão `projeto4.py` e `escolas_sp_regioes_2024_geo.csv`, e execute:

```
python -m streamlit run projeto4.py
```

O painel abre no navegador (normalmente em `http://localhost:8501`).

**3. Como usar os filtros** 

- **Região:** escolha uma das quatro regiões ou "Todas".
- **Município:** a lista mostra apenas os municípios da região escolhida; "Todos" mantém a região inteira.
- **Dependência administrativa:** escolha Federal, Estadual, Municipal ou Privada (só aparecem as opções que existem nas escolas já filtradas) ou "Todas".

Ao mudar qualquer filtro, tudo se recalcula: indicadores, gráficos, mapa e lista. Se nenhuma escola atender à combinação escolhida, o painel mostra um aviso.

## Prints do resultado

Todas as regiões, sem filtros:

![Painel com todas as regiões](prints/painel_todas_regioes.png)

Vale do Ribeira selecionado:

![Painel com o Vale do Ribeira](prints/painel_vale_do_ribeira.png)

## Elementos do painel

| Tipo | Elemento | Coluna da base usada |
| --- | --- | --- |
| Filtro | Região | `regiao` |
| Filtro | Município (depende da região escolhida) | `municipio` |
| Filtro | Dependência administrativa | `dependencia` |
| Indicador | Quantidade de escolas | contagem de linhas da base filtrada (uma linha por escola) |
| Indicador | Total de matrículas | soma de `matriculas` |
| Gráfico de característica | Escolas por porte | `porte` (criada a partir de `matriculas` pela função `classificar_porte`) |
| Gráfico de característica | Escolas por localização (Urbana ou Rural) | `localizacao` |
| Gráfico de infraestrutura | Escolas por abastecimento de água | `agua` |
| Gráfico de infraestrutura | Escolas por esgotamento sanitário | `esgoto` |
| Mapa | Cada escola como um ponto | `latitude` e `longitude` |
| Lista | Escolas que atendem aos filtros | `municipio`, `escola`, `dependencia`, `matriculas`, `porte` |

Faixas de porte (as mesmas do Projeto 1): **Pequena** até 200 matrículas, **Média** de 201 a 400 e **Grande** a partir de 401.

## O que o painel mostra

Ao selecionar o Vale do Ribeira, o painel mostra 338 escolas e 63777 matrículas, e o gráfico de esgotamento sanitário mostra que a forma mais comum é da rede pública. Podemos mudar os filtros selecionados e os dados aparecem conforme cada filtro escolhido. 

## Organização do programa

| Parte do código | O que faz | Elemento do Projeto 2 correspondente |
| --- | --- | --- |
| Função `classificar_porte` | Classifica a escola em Pequena, Média ou Grande pelo total de matrículas | Classificação das escolas por tamanho (faixas de matrícula) |
| Carregamento dos dados (`pd.read_csv`) e criação da coluna `porte` | Lê a base de escolas e acrescenta a coluna de porte | Importação e tratamento da base no Power Query |
| Filtros (`st.selectbox`) | Reduzem a base às escolas da região, do município e da dependência escolhidos | Segmentação de dados |
| Indicadores (`st.metric`) | Mostram o total de escolas e de matrículas da seleção | Números do dashboard |
| Gráficos (`st.bar_chart`) | Contam as escolas por porte, localização, água e esgoto | Gráficos dinâmicos |
| Mapa (`st.map`) | Plota cada escola pela latitude e longitude | Sem correspondência direta no Projeto 2 |
| Lista (`st.dataframe`) | Lista as escolas que atendem aos filtros | Tabelas dinâmicas / dados filtrados |

## Uso de Inteligência Artificial

Não utilizamos inteligência artificial para fazer esse projeto. 

## Fonte de Dados

**Fonte oficial:** Censo Escolar da Educação Básica 2024 (INEP).

**Link oficial:** https://www.gov.br/inep/pt-br/areas-de-atuacao/pesquisas-estatisticas-e-indicadores/censo-escolar *(conferir se o link abre antes de publicar)*

**O que os dados representam:** o Censo Escolar é o principal levantamento anual sobre as escolas de educação básica do país, feito pelo INEP. A base usada aqui (`escolas_sp_regioes_2024_geo.csv`) é um recorte fornecido na disciplina, com as escolas em atividade de 30 municípios de quatro regiões do estado de São Paulo, com suas características, infraestrutura e coordenadas geográficas. Este painel não é oficial e não representa o INEP nem o Ministério da Educação.

**Estrutura:** colunas da base usadas no painel.

| Coluna | O que representa |
| --- | --- |
| `regiao` | Região do estado: Região Metropolitana de SP, Baixada Santista, Litoral Norte ou Vale do Ribeira |
| `municipio` | Município da escola |
| `escola` | Nome da escola |
| `dependencia` | Dependência administrativa: Federal, Estadual, Municipal ou Privada |
| `localizacao` | Localização da escola: Urbana ou Rural |
| `matriculas` | Total de matrículas da escola |
| `porte` | Criada no programa a partir de `matriculas`: Pequena, Média ou Grande |
| `agua` | Principal forma de abastecimento de água |
| `esgoto` | Principal forma de esgotamento sanitário |
| `latitude`, `longitude` | Coordenadas da escola, usadas no mapa |

## Participação do Grupo

**O que aprendemos com este projeto:** *[DESCREVER.]*

**Papel de cada integrante:**

- Beatriz Apóstolo Della Nina: *[o que fez no projeto]*
- Liz Vilibor: *[o que fez no projeto]*
- Liliana Palhares Souza: *[o que fez no projeto]*
- Luiza Dias Genta: *[o que fez no projeto]*
- Rafaela Panca: *[o que fez no projeto]*
