# Projeto 1 — Simulador de Repasse do PNAE

Objetivo:

O projeto calcula os valores dos repasses financeiros do Programa Nacional de Alimentação Escolar (PNAE) com base em informações configuráveis, testando quanto dinheiro é direcionado para cada tipo de escola. Ele serve como uma ferramenta para estimar recursos e apoiar a análise orçamentária na política pública de alimentação escolar.

Como usar:


Prints do resultado:
<img width="1280" height="720" alt="image" src="https://github.com/user-attachments/assets/704cef3f-e0e3-4de9-9372-3becd4e726f4" />
<img width="1280" height="720" alt="image" src="https://github.com/user-attachments/assets/2aff7322-c392-47a9-b83f-c7b73ec190ea" />


## Uso de Inteligência Artificial

Ferramenta utilizada: Claude 

Para que foi usada: gerar o artefato HTML interativo do simulador  

Prompt usado:
Você vai gerar um artefato HTML interativo (um único arquivo, autocontido) que simula o cálculo do repasse do PNAE, a partir do modelo que eu construi em Excel para o Projeto 1 do curso Análise de Dados para Pesquisas em Políticas Públicas (FGV EAESP).
Anexei dois arquivos:
1. Minha planilha Excel, com as abas Parametros_PNAE e Simulador_Escola, contendo os dados e as fórmulas.
2. Um arquivo modelo.html, que é um artefato sobre um assunto totalmente diferente (cálculo do valor atual, matemática financeira). Não use nada do conteúdo desse arquivo — nenhum dado, nenhuma fórmula, nenhum texto dele. Use apenas como referência de: paleta de cores e tipografia, formato dos cards e das tabelas, e o tipo de mecânica interativa (campos editáveis no topo, um botão que avança passo a passo reconstruindo uma tabela de resultados, valores que reagem em tempo real a mudanças nos parâmetros).
O que o artefato deve reproduzir, fielmente ao que está na minha planilha:
●	Uma tabela de referência com os parâmetros do PNAE (modalidades e valores per capita), extraída da aba Parametros_PNAE.
●	Os dados da minha escola (nome, bairro, município) e a tabela de matrículas por modalidade, com campos editáveis para o número de matrículas.
●	O cálculo automático de: total de matrículas, porte da escola (a mesma regra de classificação por faixas que está na minha planilha), repasse anual estimado, e o resultado da regra de elegibilidade para complementação municipal (se ela existir na minha planilha).
●	A simulação com o parâmetro de ajuste que criei na Tabela de Dados do Excel: um campo editável para esse fator, mostrando como matrículas e repasse mudam em tempo real.
●	Um mecanismo com botões que percorre, passo a passo, os mesmos cenários que estão na minha Tabela de Dados do Excel, reconstruindo a tabela de resultados cenário a cenário — não apenas mostrando o resultado final de uma vez.
Regras importantes:
●	Use os dados reais da minha planilha (nome da escola, matrículas, valores per capita, faixas de classificação, fórmulas). Não invente números nem modalidades que não estejam na minha planilha.
●	Siga o mesmo estilo visual do modelo.html anexado: paleta de cores, tipografia, formato dos cards, dos botões e da mecânica de "avançar".
●	O artefato deve ser um único arquivo HTML, sem dependências externas (sem CDN, sem chamadas à internet, sem fontes externas), porque será usado sem acesso à web.
●	Reproduza as fórmulas da minha planilha com a mesma lógica (soma, PROCV, SOMARPRODUTO, SE aninhado com E/OU, e o fator de ajuste usado na Tabela de Dados) — não simplifique nem troque por uma lógica diferente da que eu construí.
●	Ao final, liste rapidamente quais células da minha planilha inspiraram cada parte do artefato (preciso disso para documentar o uso de IA no portfólio do GitHub, junto com este prompt).

O que foi ajustado manualmente: 

Após a resposta do Claude, concluímos que não era necessário fazer nenhum ajuste do HTML

## Fonte de dados 

Fonte oficial: Resolução CD/FNDE nº 1/2026, ou Censo Escolar 2024 (INEP) 

Link oficial: https://www.gov.br/fnde/pt-br/acesso-a-informacao/legislacao/resolucoes/2026/resolucao-cd_fnde-no-1-de-18-de-fevereiro-de-2026-dou-imprensa-nacional.pdf/view

O que os dados representam: São dados dos parâmetros do PNAE de 2026 que representam o repasse do PNAE para cada modalidade de escola, além disso com a planilha criada é possível simular esse repasse com um aumento percentual qualquer afim de analisar o que aconteceria para cada caso. 

Estrutura: colunas de modalidade de cada escola, valor per capita por dia, matrículas por porte de escola e além da quantidade de dias letivos por ano. O simulador consiste nesses dados além de uma fórmula de soma produto que calcula o aumento percentual em cada modalidade. 

## Participação do Grupo

O que aprendemos com este projeto:
O grupo aprendeu a estruturar modelagens financeiras dinâmicas integrando fórmulas do Excel, além de compreender de forma aplicada a mecânica de financiamento e repasse de recursos estabelecida pelas normativas do PNAE.

Papel de cada integrante:
- Beatriz Apóstolo Della Nina: Desenvolvi o objetivo, o que aprendemos com o projeto e reuni os prints.
- Luiza Dias Genta: Acabei de formatar a tabela do projeto 1 e criei o HTML
