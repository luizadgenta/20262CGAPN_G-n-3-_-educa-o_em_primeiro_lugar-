# Simulador de Repasse do PNAE com automação em VBA

## Objetivo

Esta versão evolui o Simulador de Repasse do Programa Nacional de Alimentação Escolar (PNAE) do Projeto 1, acrescentando **automação em VBA**. O simulador continua calculando o repasse anual estimado de uma escola a partir das matrículas por modalidade e simulando variações com um **fator de ajuste**. Agora, cada simulação pode ser **registrada automaticamente** em um banco de dados dentro da própria planilha, com validação dos campos e identificação do usuário responsável.


## Como usar

1. Baixe o arquivo `Simulador-PNAE-Monitorada_24_09.xlsm` e abra no Microsoft Excel.
2. Clique em **Habilitar Conteúdo** quando aparecer o aviso de macros. Sem isso, o botão não funciona.
3. Na aba `Simulador_Escola`, edite as matrículas por modalidade, se quiser.
4. Informe o **Fator de Ajuste** (C26), por exemplo `0,15` para +15%.
5. Escreva o **Racional da Taxa** (C25), explicando o motivo do fator escolhido.
6. Escreva o **Usuário** (F26).
7. Clique em **Salvar Simulação**.
8. Consulte o resultado na aba `Banco_de_Dados`. Cada linha é uma simulação registrada.

Para ver o código, abra o editor do VBA com **Alt + F11** e acesse o módulo `modSimulador`.

> O arquivo precisa permanecer no formato `.xlsm`. Se for salvo como `.xlsx`, as macros são perdidas.

## Como foi testado

- Registro de simulações com fatores de ajuste diferentes, conferindo a gravação em todas as colunas, inclusive a de Usuário.
- Tentativa de registro com o **Usuário em branco**, que foi bloqueada pela mensagem de erro.
- Verificação de que os campos são limpos após cada registro.

## Arquivos

- `Simulador-PNAE-Monitorada_24_09.xlsm` — planilha com os parâmetros do PNAE, o simulador, a Tabela de Dados, o banco de simulações e a macro em VBA.
- `README.md` — apresentação do projeto e instruções de uso.

---

## Disclaimers

### Uso de Inteligência Artificial

**Ferramenta utilizada:** Claude (Anthropic).

**Para que foi usada:**
- Na versão original do projeto, para gerar o artefato HTML interativo do simulador (arquivo `Simulador_PNAE.html`).
- Nesta atualização, para **tirar duvidas sobre a implementação do campo Usuário em VBA**

**Prompts usados:**
- Pedido de explicação de como arrumar alguns erros que estavam dando ao implementar o Usuário em VBA.
- Envio do arquivo `Simulador-PNAE-Monitorada_24_09.xlsm` com o pedido de: ajuste os erros ocorrendo no campo Usuário do simulador.



## Fonte de Dados

**Fonte oficial:** Resolução CD/FNDE nº 1/2026 (valores per capita do PNAE).

**Link oficial:** https://www.gov.br/fnde/pt-br/acesso-a-informacao/legislacao/resolucoes/2026/resolucao-cd_fnde-no-1-de-18-de-fevereiro-de-2026-dou-imprensa-nacional.pdf/view

**O que os dados representam:** valores per capita diários do repasse do PNAE por modalidade. As matrículas e a escola (EMEB Vila Quitaúna, Osasco/SP) são fictícias. As simulações gravadas no banco de dados são registros de uso da planilha, não dados oficiais.


### Participação do grupo

**O que aprendemos com este projeto:**  
A automatizar uma rotina com VBA (ler, validar, gravar e limpar) e a registrar o raciocínio por trás de cada simulação.

**Papel de cada integrante neste projeto:**
- Luiza Dias Genta: *(implementação do campo Usuário em VBA, formatação da planilha, README e testes)*
- Demais integrantes: *(ajudaram a tirar duvidas sobre algumas questões do trabalho além de acompanharem o andamento do projeto)*





