import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path

# 1. Configuração da Página
st.set_page_config(page_title="Análise de Produtos - Amanda", page_icon="📦", layout="wide")

# 2. Cabeçalho 
st.title("📦 Análise de Produtos e Categorias")
st.markdown(f"""
Dashboard desenvolvido para análise de faturamento e logística.
**Responsável: Amanda**
""")
st.markdown("---")

# 3. Caminho Inteligente (Funciona em qualquer PC)
caminho_base = Path(__file__).parents[2]
arquivo_csv = caminho_base / 'data' / 'produtos.csv'

try:
    df = pd.read_csv(arquivo_csv)
    
    # 4. Filtro na lateral
    st.sidebar.header("Configurações")
    top_n = st.sidebar.slider("Quantas categorias ver no gráfico?", 5, 20, 10)

    # 5. Gráficos
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Faturamento por Categoria")
        fig_pie = px.pie(df.nlargest(top_n, 'Faturamento'), 
                        values='Faturamento', names='Categoria', hole=0.4)
        st.plotly_chart(fig_pie, use_container_width=True)

    with col2:
        st.subheader("Peso vs Valor do Frete")
        fig_scatter = px.scatter(df, x="Peso", y="Valor_Frete", color="Categoria")
        st.plotly_chart(fig_scatter, use_container_width=True)

    # 6. Tabela
    st.markdown("---")
    st.subheader("Dados Brutos")
    st.dataframe(df)

except Exception as e:
    st.error(f"Erro ao carregar os dados: {e}")
    st.info(f"Verifique se o arquivo está em: {arquivo_csv}")