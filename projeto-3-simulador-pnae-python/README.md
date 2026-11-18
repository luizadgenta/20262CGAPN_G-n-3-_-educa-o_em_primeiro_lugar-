# Projeto 3 — Simulador de Repasse do PNAE em Python

## Objetivo

O simulador calcula o repasse anual do PNAE que a União destina a uma escola (creche, pré-escola e ensino fundamental), classifica o porte da escola e estima **que parcela do custo dos alimentos esse repasse consegue cobrir**. Pode ser usado para estimar recursos de uma escola e discutir se o valor federal é suficiente para a alimentação escolar. Aqui o simulador foi aplicado a uma escola pública real, **[PREENCHER: nome da escola]**.

## Como usar

**O que é preciso:** Python 3 instalado (https://www.python.org). Não é necessário instalar nenhum pacote.

**Como rodar:** abra o terminal na pasta do projeto e execute:

```bash
python simulador_pnae.py
```

(Em alguns computadores o comando é `python3 simulador_pnae.py`.)

**Perguntas do programa e respostas esperadas:**

| Pergunta | O que digitar |
| --- | --- |
| Digite o seu nome | texto livre |
| Digite o nome da sua escola | texto livre |
| Quantidade de dias letivos do ano | número inteiro (ex.: `200`) |
| Número de alunos na creche | número inteiro, `0` se a escola não tiver a etapa |
| Número de alunos na pré-escola | número inteiro, `0` se não tiver |
| Número de alunos no ensino fundamental | número inteiro, `0` se não tiver |

Só são aceitos números inteiros, sem vírgula, ponto ou espaço. Se o valor for inválido, o programa repete a pergunta.

**Teste de conferência (resultado do Projeto 1):** com 200 dias letivos, 60 alunos de creche, 80 de pré-escola e 50 de fundamental, o repasse anual total é **R$ 37.660,00** e o porte é **Pequena**.

## Prints do resultado

![Simulador rodando com a escola real](prints/simulador-escola-real.png)

![Teste de conferência com os dados do Projeto 1](prints/simulador-teste-projeto1.png)

## Escola simulada

| Campo | Valor |
| --- | --- |
| Nome | [PREENCHER] |
| Código INEP | [PREENCHER] |
| Município / UF | [PREENCHER] |
| Dependência administrativa | [PREENCHER: Municipal ou Estadual] |
| Situação de funcionamento | Em atividade |
| Matrículas de creche | [PREENCHER] |
| Matrículas de pré-escola | [PREENCHER] |
| Matrículas de ensino fundamental | [PREENCHER] |
| Dias letivos usados | 200 |

**Como os dados foram encontrados no Censo Escolar 2024:**

1. Arquivo utilizado: [PREENCHER: nome do arquivo de microdados, ex.: `microdados_ed_basica_2024.csv`] e o dicionário de dados do Censo.
2. Variáveis usadas: [PREENCHER: confirmar os nomes no dicionário] para nome (`NO_ENTIDADE`), código INEP (`CO_ENTIDADE`), município (`NO_MUNICIPIO`), UF (`SG_UF`), dependência administrativa (`TP_DEPENDENCIA`), situação de funcionamento (`TP_SITUACAO_FUNCIONAMENTO`) e matrículas de creche, pré-escola e ensino fundamental.
3. Filtro: [PREENCHER: como a escola foi filtrada, ex.: por `NO_ENTIDADE` e `NO_MUNICIPIO`, confirmando depois o `CO_ENTIDADE`].
4. [PREENCHER, se for o caso: "A escola não tem matrículas em [etapa]; o simulador recebeu 0 para ela."]

## Custo dos alimentos

| Item | Informação |
| --- | --- |
| Valor adotado por refeição | R$ [PREENCHER] |
| Fonte | [PREENCHER: instituição e documento] |
| Link | [PREENCHER] |
| Data da informação | [PREENCHER] |
| Justificativa | [PREENCHER: por que o valor é razoável para esta escola] |

**Ressalvas de comparabilidade:** [PREENCHER: se a fonte é de outro município, outro ano ou outra etapa de ensino, dizer isso e comentar como pode afetar o resultado. Ex.: um valor de 2025 tende a subestimar o custo de 2026 pela inflação de alimentos.]

Este valor é só o custo dos **alimentos**. A Lei nº 11.947/2009 limita o uso do recurso do PNAE à compra de gêneros alimentícios; merendeiras, gás, equipamentos e cozinhas são pagos por estados e municípios com recursos próprios e **não entram** neste cálculo.

## Resultados e reflexão

### Resultados

| Indicador | Valor |
| --- | --- |
| Repasse anual total | R$ [PREENCHER] |
| Custo anual estimado dos alimentos | R$ [PREENCHER] |
| Cobertura do repasse federal | [PREENCHER]% |
| Diferença a ser coberta por outras fontes | R$ [PREENCHER] |

### Como o cálculo é feito

- Custo anual dos alimentos = total de alunos × dias letivos × custo dos alimentos por refeição (uma refeição por aluno por dia letivo).
- Cobertura (%) = repasse anual total ÷ custo anual dos alimentos × 100.
- Diferença = custo anual − repasse. Se o repasse for igual ou maior que o custo, a diferença é zero e o programa informa que o repasse cobre o custo estimado.

### Reflexão

> Rascunho para o grupo revisar, ajustar com os números reais e **conferir contra as três leituras indicadas** (Todos Pela Educação, 2023; Observatório da Alimentação Escolar, 21/10/2025; Brasil de Fato, 16/10/2025). Citem as leituras pelo nome e substituam as frases genéricas por dados que vocês leram nelas.

O repasse federal do PNAE é complementar: a Constituição e a lei preveem que estados e municípios completem o valor com recursos próprios. No caso de [ESCOLA], o repasse cobre [X]% do custo estimado dos alimentos, e a diferença anual de R$ [Y] precisa vir do orçamento do [município/estado]. Quando essa diferença não é coberta, a escola precisa escolher o que sacrificar. As leituras indicam que o efeito aparece na qualidade do cardápio (menos alimentos in natura, mais itens baratos e ultraprocessados), na quantidade servida e na dificuldade de cumprir metas como a compra de alimentos da agricultura familiar.

Isso importa porque, para muitos estudantes, a refeição escolar é a principal refeição do dia. Redes com menos capacidade fiscal tendem a complementar menos, e a desigualdade de financiamento entre municípios se transforma em desigualdade de alimentação.

### Simplificações do simulador

- As **matrículas são de 2024** e os **valores per capita são de 2026**; os períodos são diferentes.
- O cálculo considera **apenas três etapas** (creche, pré-escola e fundamental); a escola pode ter outras (EJA, AEE, ensino médio) que também recebem repasse.
- A estimativa supõe **uma refeição por aluno por dia letivo**, mas há alunos em tempo integral, que fazem mais refeições, e faltas ao longo do ano.
- O **custo dos alimentos** vem de uma única fonte, que pode não representar os preços reais pagos pela escola.
- O repasse do PNAE é feito ao estado ou município, não diretamente à escola; aqui ele é atribuído à escola de forma proporcional às matrículas.

## Organização do programa

| Parte do código | O que faz | Correspondência no Projeto 1 (Excel) |
| --- | --- | --- |
| Parâmetros (`VAL_CRECHE`, `VAL_PREESCOLA`, `VAL_FUNDAMENTAL`, `LIMITE_PEQUENA`, `LIMITE_MEDIA`) | valores per capita e faixas de porte no topo do arquivo | aba `Parametros_PNAE` |
| `CUSTO_ALIMENTOS_REFEICAO` | custo dos alimentos por refeição, com a fonte em comentário | sem correspondência (novo) |
| `ler_numero` | pede um inteiro e repete a pergunta até a entrada ser válida | células de entrada das matrículas |
| `classificar_porte` | devolve Pequena, Média ou Grande pelo total de matrículas | `PROCV` aproximado das faixas de porte |
| `calcular_repasse` | matrículas × per capita × dias letivos, por etapa | `SOMARPRODUTO` × dias letivos |
| `calcular_cobertura` | custo anual dos alimentos, cobertura (%) e diferença; trata o caso em que o repasse cobre o custo | sem correspondência (novo) |
| `formatar_reais` | formata valores em reais para a tela | formato de moeda das células |
| Programa principal | conversa com o usuário, chama as funções e mostra os resultados | aba `Simulador_Escola` |

## Uso de Inteligência Artificial

- Não utilizamos IA no desenvolvimento desse projeto. 

## Fonte de Dados

**Fontes oficiais:** Censo Escolar 2024 (INEP) e Resolução CD/FNDE nº 1/2026.

**Links oficiais:**

- Censo Escolar (microdados): https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos/microdados/censo-escolar
- Resolução CD/FNDE nº 1/2026: https://www.gov.br/fnde/pt-br/acesso-a-informacao/legislacao/resolucoes/2026/resolucao-cd_fnde-no-1-de-18-de-fevereiro-de-2026-dou-imprensa-nacional.pdf/view

**O que os dados representam:** o Censo Escolar traz as escolas em atividade no Brasil com suas matrículas por etapa em 2024. A Resolução define os valores per capita diários do PNAE em 2026 (creche R$ 1,57; pré-escola R$ 0,82; fundamental R$ 0,57). Juntos, permitem estimar o repasse federal de uma escola.

**Estrutura:**

| Variável | Significado |
| --- | --- |
| [PREENCHER: nomes das variáveis do Censo usadas] | nome, código INEP, município, UF, dependência, situação de funcionamento e matrículas por etapa |
| Valor per capita | R$ por aluno por dia letivo, por etapa |

**Custo dos alimentos:** 
https://blog.mundovem.com.br/calcular-reduzir-perdas/
Usamos essa fonte pois julgamos que eram dados verídicos e confiáveis. 

## Participação do Grupo

**O que aprendemos com este projeto:**  A transformar uma planilha em programa Python com funções, a buscar uma escola real no Censo e a comparar o repasse com o custo de alimentar os alunos.

**Papel de cada integrante:**

- Beatriz Apóstolo e Luiza Genta: criaram os códigos em python e colocaram no github
- Demais participantes: tiraram possíveis dúvidas durante o processo de desenvolvimento do trabalho. 
