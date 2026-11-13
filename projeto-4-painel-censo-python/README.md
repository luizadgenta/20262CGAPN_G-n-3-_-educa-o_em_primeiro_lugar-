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

<img width="593" height="371" alt="Screenshot 2026-11-13 091714" src="https://github.com/user-attachments/assets/e5382b1f-41b0-4c3e-bf38-ae026d56186e" />
<img width="548" height="319" alt="Screenshot 2026-11-13 091721" src="https://github.com/user-attachments/assets/3e6b1d0f-e377-4acf-b728-71350e2e171e" />
<img width="554" height="313" alt="Screenshot 2026-11-13 091729" src="https://github.com/user-attachments/assets/dccecc50-7a6e-4a64-a231-bb4c9f2f3bc5" />
<img width="542" height="307" alt="Screenshot 2026-11-13 091736" src="https://github.com/user-attachments/assets/4683b006-c006-4dc9-8b1e-bec61464eb06" />
<img width="548" height="313" alt="Screenshot 2026-11-13 091743" src="https://github.com/user-attachments/assets/68a93488-8f65-472f-b591-e46bf8a4b57f" />
<img width="550" height="433" alt="Screenshot 2026-11-13 091752" src="https://github.com/user-attachments/assets/404dc3b3-631f-4332-b1e0-47658767665d" />
<img width="554" height="385" alt="Screenshot 2026-11-13 091759" src="https://github.com/user-attachments/assets/5f8c0fcc-91be-4093-ad4f-a97a228d45e4" />


Vale do Ribeira selecionado:

<img width="546" height="361" alt="Screenshot 2026-11-13 092108" src="https://github.com/user-attachments/assets/5ee49f01-03a8-4468-b489-0eccb11673da" />
<img width="525" height="324" alt="Screenshot 2026-11-13 092114" src="https://github.com/user-attachments/assets/3bf5373c-74da-4aa4-b0fe-f6451df9d6c4" />
<img width="529" height="322" alt="Screenshot 2026-11-13 092123" src="https://github.com/user-attachments/assets/23470cf0-55ce-4c21-bb7c-a7830b306ade" />
<img width="533" height="314" alt="Screenshot 2026-11-13 092133" src="https://github.com/user-attachments/assets/242cebb4-7953-4592-ad5a-045c6c89e167" />
<img width="533" height="315" alt="Screenshot 2026-11-13 092140" src="https://github.com/user-attachments/assets/19f41ca0-6f97-4e5e-bd4e-5bf8d0303556" />
<img width="555" height="425" alt="Screenshot 2026-11-13 092148" src="https://github.com/user-attachments/assets/4307a010-53b8-4764-8add-b008df28d7d4" />
<img width="550" height="353" alt="Screenshot 2026-11-13 092206" src="https://github.com/user-attachments/assets/b77750af-e725-4e74-8198-b70a5de0756f" />


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

**Link oficial:** https://www.gov.br/inep/pt-br/areas-de-atuacao/pesquisas-estatisticas-e-indicadores/censo-escolar 

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

**O que aprendemos com este projeto:** 

Ao realizar esse trabalho, pudemos aprender a criar um painel interativo e muito interessante que transforma dados de uma tabela em um frontend bonitinho e bem autoexplicativo. Esse tipo de painel pode ser muito útil para apresentar dados que inicialmente só estavam em linhas e colunas, mas que podem ser lidos em um painel extremamente útil. 

**Papel de cada integrante:**

- Beatriz Apóstolo Della Nina: ajudou a conferir se estava tudo correto
- Liz Vilibor: ajudou a conferir se estava tudo correto
- Liliana Palhares Souza: ajudou a conferir se estava tudo correto
- Luiza Dias Genta: criou os códigos para criação do painel e atualizou o github 
- Rafaela Panca: ajudou a conferir se estava tudo correto
