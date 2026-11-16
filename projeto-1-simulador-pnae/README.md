# Projeto 1 — Simulador de Repasse do PNAE

Objetivo:

O projeto calcula os valores dos repasses financeiros do Programa Nacional de Alimentação Escolar (PNAE) com base em informações configuráveis, testando quanto dinheiro é direcionado para cada tipo de escola. Ele serve como uma ferramenta para estimar recursos e apoiar a análise orçamentária na política pública de alimentação escolar.

## Como usar

### Planilha Excel (`Simulador_PNAE.xlsx`)

1. Abra o arquivo no Microsoft Excel.
2. Na aba `Parametros_PNAE`, consulte os valores per capita por modalidade, os dias letivos e as faixas de porte. Não é preciso alterar nada.
3. Na aba `Simulador_Escola`, edite o número de matrículas de cada modalidade. O total de matrículas, o porte, o repasse anual estimado e a elegibilidade para complementação municipal são calculados automaticamente.
4. Na seção "Modelo para Simulação", altere o **Fator de Ajuste** (por exemplo, `0,15` para +15%) e veja as matrículas ajustadas e o repasse ajustado.
5. A **Tabela de Dados** (A39:C48) mostra o repasse para fatores de −20% a +20%, em passos de 5%.

### Simulador HTML (`Simulador_PNAE.html`)

1. Baixe o arquivo e abra no navegador (Chrome, Edge ou Firefox). Não precisa de internet nem de instalação.
2. Edite as matrículas e o fator de ajuste; os resultados mudam em tempo real.
3. Na seção "Tabela de dados", clique em **Calcular base e reiniciar** e depois em **Calcular próximo cenário** para reconstruir os 9 cenários, um por vez.


## Arquivos desta pasta

| Arquivo | O que é |
| --- | --- |
| `Simulador_PNAE.xlsx` | Planilha com as abas `Parametros_PNAE` e `Simulador_Escola` |
| `Simulador_PNAE.html` | Versão interativa no navegador, equivalente à planilha |


## Regras e fórmulas

| Resultado | Regra | Fórmula no Excel |
| --- | --- | --- |
| Total de matrículas | soma das modalidades | `SOMA` |
| Valor per capita | busca pela modalidade | `PROCV(...; FALSO)` |
| Porte da escola | Pequena (0 a 200), Média (201 a 400), Grande (401 ou mais) | `PROCV(...; VERDADEIRO)` |
| Repasse anual | soma de matrículas × valor per capita, vezes os dias letivos | `SOMARPRODUTO(...) * dias letivos` |
| Elegibilidade para complementação municipal | recebe se a escola é **Pequena E** tem matrículas em creche **OU** pré-escola | `=SE(E(B19="Pequena";OU(B10>0;B11>0));"Recebe Complementação";"Não Recebe")` |
| Matrículas ajustadas | matrículas × (1 + fator de ajuste) | — |

A regra de elegibilidade é um exercício de `SE` aninhado com `E`/`OU`; **não reproduz nenhum critério oficial** de complementação municipal.

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

**O que os dados representam:** os valores per capita diários que a União repassa a estados e municípios por aluno de cada modalidade, em 2026 (reajuste médio de 14,35% sobre 2025). Multiplicados pelas matrículas e pelos dias letivos, dão o repasse anual estimado de uma escola. A escola e as matrículas são fictícias, criadas para fins didáticos, e as faixas de porte também foram definidas para este curso.

**Estrutura:**

| Coluna / campo | Significado |
| --- | --- |
| Modalidade | Creche, Pré-escola, Fundamental, Médio, EJA, Indígena/Quilombola, AEE (contraturno) |
| Valor per capita (R$/dia) | valor repassado por aluno, por dia letivo |
| Matrículas | número de alunos da escola na modalidade (campo editável) |
| Dias letivos | 200 dias por ano |
| Porte | faixa de matrículas totais (Pequena, Média, Grande) |
| Fator de ajuste | variação percentual aplicada às matrículas na simulação |


**O que aprendemos com este projeto:** a estruturar um modelo financeiro dinâmico no Excel, combinando `PROCV`, `SOMARPRODUTO`, `SE` aninhado e Tabela de Dados, e a entender na prática como o repasse do PNAE depende das matrículas, do valor per capita e dos dias letivos.

 
## Participação do Grupo

O que aprendemos com este projeto:
O grupo aprendeu a estruturar modelagens financeiras dinâmicas integrando fórmulas do Excel, além de compreender de forma aplicada a mecânica de financiamento e repasse de recursos estabelecida pelas normativas do PNAE.

Papel de cada integrante:
- Beatriz Apóstolo Della Nina: Desenvolvi o objetivo, o que aprendemos com o projeto e reuni os prints.
- Luiza Dias Genta: Acabei de formatar a tabela do projeto 1 e criei o HTML


















