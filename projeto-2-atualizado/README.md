# Projeto 2: Painel do Censo Escolar 2024 com Automação via Power Query

Painel interativo em Excel que analisa a infraestrutura e o porte das escolas de Osasco, SP a partir da **base nacional completa do Censo Escolar 2024** (INEP). Ao trocar o município em uma única célula e clicar em **Atualizar Tudo**, todo o painel (tabelas dinâmicas, gráficos, segmentações e dashboard) é recalculado automaticamente.


---

## Objetivo

Construir um painel completo e reutilizável do Censo Escolar que:

- importe e trate a base nacional via **Power Query**, sem manipulação manual;
- reduza centenas de milhares de linhas para **apenas o município escolhido**, antes de as dinâmicas processarem os dados;
- classifique as escolas por **tamanho** (faixas de matrícula) e por **infraestrutura** (Água, Energia, Esgoto e Lixo);
- permita explorar os resultados com tabelas dinâmicas, gráficos dinâmicos, segmentação de dados e dashboard;
- seja atualizado em **um clique**, ao trocar o município.

---

**Fontes de dados utilizadas pelo Power Query:**

- Base principal: Microdados do Censo Escolar 2024 (todos os municípios);
- Tabelas auxiliares: **Dependência**, **Localização**, **Localização Diferenciada** e **Situação**;
- Tabela de filtro: intervalo com as células nomeadas **UF** e **Município**.

---

## O que mudou da versão anterior:
A lógica de tratamento é a mesma da versão anterior. O que muda é o volume de dados e o momento em que o filtro é aplicado: como a junção interna com a tabela de filtro acontece no Power Query, o painel final trabalha somente com os dados do município escolhido, mesmo partindo da base nacional.

## Como usar

1. Abra a planilha no **Excel para desktop** (o Power Query completo não está disponível em todas as versões web/mobile).
2. Na aba de parâmetros, preencha as células nomeadas:
   - **UF**: sigla do estado (ex.: `SP`);
   - **Município**: nome do município, **exatamente como consta na base do INEP** (ex.: `São Paulo`).
3. Se o Excel pedir, aponte o caminho local da base do Censo Escolar 2024 em *Dados > Obter Dados > Configurações da Fonte de Dados*.
4. Clique em **Dados > Atualizar Tudo**.
5. Aguarde a atualização terminar. O dashboard, as dinâmicas e os gráficos refletem o município informado.
6. Use as **segmentações de dados** para filtrar o painel por dependência administrativa, localização, tamanho da escola etc.

**Dica:** se o painel ficar vazio após a atualização, verifique a grafia do município e da UF (acentos e maiúsculas/minúsculas contam). A junção interna só retorna linhas quando os dois campos coincidem com a base.

---

## Disclaimers

1. **Fonte de dados:** os dados são públicos e pertencem ao **INEP (Censo Escolar da Educação Básica 2024)**. Este projeto não é oficial e não representa o INEP ou o Ministério da Educação. Os números exibidos dependem da versão da base utilizada e podem diferir de publicações oficiais posteriores.
2. **Participação**: Luiza Dias Genta fez toda parte do excel (power query), demais participantes ajudaram a tirar eventuais duvidas 
3. **Uso de IA:** Claude foi usado para assistência em dúvidas de erros que estavam ocorrendo durante o trabalho. 

---
## Nota de esclarecimento sobre o formato do arquivo: 
O arquivo excel era muito pesado e não foi possível subir no github por isso optamos por enviar o link de uma pasta em uma nuvem para que fosse possível acessar o trabalho. 
