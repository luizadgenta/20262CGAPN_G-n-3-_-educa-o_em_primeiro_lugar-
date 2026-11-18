### PARÂMETROS

# Valores per capita (R$ por aluno por dia letivo)
# Fonte: Resolução CD/FNDE nº 1/2026
VALOR_CRECHE = 1.57
VALOR_PREESCOLA = 0.82
VALOR_FUNDAMENTAL = 0.57

# Custo dos alimentos por aluno por dia letivo (R$), supondo uma refeição por aluno por dia
# Fonte: Ritter e Silveira, "Composição nutricional e custos das refeições em uma escola de
# educação infantil de Itaqui/RS", SIEPE/Unipampa, nov. 2017 (dados de ago.-set. 2017).
# Link: https://guri.unipampa.edu.br/uploads/evt/arq_trabalhos/13315/seer_13315.pdf
CUSTO_ALIMENTOS_REFEICAO = 2.01


### FUNÇÕES (processo do backend)

def ler_numero(mensagem):
    numero = input(mensagem)
    while not numero.isdigit():
        print("Você digitou um número inválido. Digite um número inteiro.")
        numero = input(mensagem)
    numero = int(numero)
    return numero


def calcular_repasse(matriculas, valor_per_capita, dias_letivos):
    repasse = matriculas * valor_per_capita * dias_letivos
    return repasse


def classificar_porte(total_matriculas):
    if total_matriculas <= 200:
        porte = "Pequena"
    elif total_matriculas <= 400:
        porte = "Média"
    else:
        porte = "Grande"
    return porte


def calcular_cobertura(repasse_total, total_matriculas, dias_letivos):
    # custo anual = alunos x dias letivos x custo da refeição (1 refeição por aluno por dia)
    custo_anual = total_matriculas * dias_letivos * CUSTO_ALIMENTOS_REFEICAO

    # evita divisão por zero quando não há matrículas
    if custo_anual == 0:
        return 0, 0, 0

    cobertura = repasse_total / custo_anual * 100

    if repasse_total >= custo_anual:
        diferenca = 0
    else:
        diferenca = custo_anual - repasse_total

    return custo_anual, cobertura, diferenca


def formatar_reais(valor):
    texto = f"{valor:,.2f}"  # ex.: 81,202.00
    texto = texto.replace(",", "X").replace(".", ",").replace("X", ".")
    return "R$ " + texto


### PROGRAMA PRINCIPAL

print("*** Olá, bem-vindes ao simulador PNAE ***")
print()
nome = input("Digite o seu nome: ")
escola = input("Digite o nome da sua escola: ")

### Pedir dias letivos
dias_letivos = ler_numero("Qual a quantidade de dias letivos do ano: ")

### Pedir as matrículas
print("Digitação das matrículas")
creche = ler_numero("Número de alunos na creche: ")
preescola = ler_numero("Número de alunos na pré-escola: ")
fundamental = ler_numero("Número de alunos no ensino fundamental: ")

total_matriculas = creche + preescola + fundamental

### Cálculos
repasse_creche = calcular_repasse(creche, VALOR_CRECHE, dias_letivos)
repasse_preescola = calcular_repasse(preescola, VALOR_PREESCOLA, dias_letivos)
repasse_fundamental = calcular_repasse(fundamental, VALOR_FUNDAMENTAL, dias_letivos)
repasse_total = repasse_creche + repasse_preescola + repasse_fundamental

porte = classificar_porte(total_matriculas)
custo_anual, cobertura, diferenca = calcular_cobertura(repasse_total, total_matriculas, dias_letivos)

### Resultados
print()
print("=== Cálculos ===")
print()
print("Escola:", escola)
print("Total de matrículas:", total_matriculas)
print("Sua escola é de porte:", porte)
print("Valor a receber creche:", formatar_reais(repasse_creche))
print("Valor a receber pré-escola:", formatar_reais(repasse_preescola))
print("Valor a receber fundamental:", formatar_reais(repasse_fundamental))
print("Valor a receber total:", formatar_reais(repasse_total))
print()
print("=== Cobertura do repasse federal ===")
print("Custo anual estimado dos alimentos:", formatar_reais(custo_anual))
print("Cobertura do repasse federal:", f"{cobertura:.2f}".replace(".", ","), "%")
print("Diferença a ser coberta por outras fontes:", formatar_reais(diferenca))

if custo_anual == 0:
    print("Não há matrículas informadas, portanto não há custo a estimar.")
elif diferenca == 0:
    print("O repasse cobre o custo estimado dos alimentos.")

print()
print("Fim dos cálculos")
input("Digite ENTER para seguir")
