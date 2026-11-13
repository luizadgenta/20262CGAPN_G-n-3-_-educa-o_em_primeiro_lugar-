import pandas as pd
import streamlit as st


# ── Função ───────────────────────────────────────────────────────────
def classificar_porte(total):
    """Classifica a escola pelo total de matrículas (mesmas faixas do Projeto 1)."""
    if total <= 200:
        return "Pequena"
    elif total <= 400:
        return "Média"
    else:
        return "Grande"


# ── Carregamento dos dados ───────────────────────────────────────────
censo = pd.read_csv("escolas_sp_regioes_2024_geo.csv")
censo["porte"] = censo["matriculas"].apply(classificar_porte)

# ── Cabeçalho ────────────────────────────────────────────────────────
st.title("Painel de escolas de regiões de SP")
st.caption("Adaptado do Censo Escolar 2024 (INEP)")
st.caption("Painel preparado pelo Grupo 3 — Educação em Primeiro Lugar")

# ── Filtros (antes dos indicadores e gráficos) ───────────────────────


# Filtro 1: região (opções lidas da própria base, sem risco de erro de grafia)
regioes = ["Todas"] + sorted(censo["regiao"].dropna().unique())
regiao = st.selectbox("Região", regioes)
if regiao != "Todas":
    censo = censo[censo["regiao"] == regiao]

# Filtro 2: município (só mostra os municípios da região escolhida)
municipios = ["Todos"] + sorted(censo["municipio"].dropna().unique())
municipio = st.selectbox("Município", municipios)
if municipio != "Todos":
    censo = censo[censo["municipio"] == municipio]

# Filtro 3: dependência administrativa
dependencias = ["Todas"] + sorted(censo["dependencia"].dropna().unique())
dependencia = st.selectbox("Dependência administrativa", dependencias)
if dependencia != "Todas":
    censo = censo[censo["dependencia"] == dependencia]

# ── Indicadores ──────────────────────────────────────────────────────
col1, col2 = st.columns(2)
col1.metric("Quantidade de escolas", len(censo))
col2.metric("Total de matrículas", int(censo["matriculas"].sum()))

if censo.empty:
    st.warning("Nenhuma escola atende a esses filtros.")
    st.stop()

# ── Gráficos de características ──────────────────────────────────────
st.subheader("Escolas por porte")
st.bar_chart(censo["porte"].value_counts())

st.subheader("Escolas por localização (urbana ou rural)")
st.bar_chart(censo["localizacao"].value_counts())

# ── Gráficos de infraestrutura ───────────────────────────────────────
st.subheader("Escolas por abastecimento de água")
st.bar_chart(censo["agua"].value_counts())

st.subheader("Escolas por esgotamento sanitário")
st.bar_chart(censo["esgoto"].value_counts())

# ── Mapa ─────────────────────────────────────────────────────────────
st.subheader("Mapa das escolas")
st.map(censo[["latitude", "longitude"]].dropna())

# ── Lista de escolas ─────────────────────────────────────────────────
st.subheader("Lista das escolas")
st.dataframe(censo[["municipio", "escola", "dependencia", "matriculas", "porte"]])