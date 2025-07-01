import streamlit as st
import pandas as pd
from config import supabase
import plotly.express as px

def dashboard():
    st.title("Dashboard")

    vendas = supabase.table("vendas").select("*").execute().data
    df = pd.DataFrame(vendas)

    if df.empty:
        st.warning("Nenhuma venda cadastrada.")
        return

    df.columns = df.columns.str.lower().str.strip().str.replace(" ", "_")
    df["dia"] = pd.to_datetime(df["dia"])

    col1, col2 = st.columns(2)
    data_inicio = col1.date_input("Data Inicial", df["dia"].min().date(), format="DD/MM/YYYY")
    data_fim = col2.date_input("Data Final", df["dia"].max().date(), format="DD/MM/YYYY")

    df_filtrado = df[(df["dia"] >= pd.to_datetime(data_inicio)) & (df["dia"] <= pd.to_datetime(data_fim))]

    # Cards lado a lado
    col_fat, col_animador, col_locucao = st.columns(3)

    faturamento = float(df_filtrado['valor'].sum())
    valor_animador = df_filtrado['custo_animador'].sum()
    locucao = df_filtrado['custo_locucao'].sum()
    lucro_liquido = faturamento - valor_animador - locucao

    col_fat.metric("Faturamento Bruto", f"R$ {faturamento:,.2f}")
    col_animador.metric("Total em Animador", f"R$ {valor_animador:,.2f}")
    col_locucao.metric("Total em Locução", f"R$ {locucao:,.2f}")

    html_code = f"""
    <div style="font-size:16px; color:white;">Lucro Líquido</div>
    <div style="font-size:32px; font-weight:bold; color:green;">R$ {lucro_liquido:,.2f}</div>
    """
    st.markdown(html_code, unsafe_allow_html=True)

    # Gráfico de Barras
    df_group = df_filtrado.groupby(df_filtrado["dia"].dt.date)["valor"].sum().reset_index()
    df_group.columns = ["Data", "Total em Vendas"]
    df_group["Data"] = pd.to_datetime(df_group["Data"])  # Corrige tipo para datetime
    df_group["Data_formatada"] = df_group["Data"].dt.strftime("%d/%m/%Y")

    fig_bar = px.bar(
        df_group, 
        x="Data_formatada", 
        y="Total em Vendas",
        labels={"Data_formatada": "Data", "Total em Vendas": "R$"},
        height=400,
        text="Total em Vendas"
    )
    fig_bar.update_traces(texttemplate='%{text:.2f}', textposition='outside')
    fig_bar.update_layout(uniformtext_minsize=8, uniformtext_mode='hide')

    st.subheader("📊 Gráfico de Vendas")
    st.plotly_chart(fig_bar, use_container_width=True)

    # Gráfico de Pizza
    st.subheader("Produtos Mais Vendidos (Quantidade)")

    df_produto = df_filtrado.groupby("produto").size().reset_index(name="Quantidade")

    fig_pie = px.pie(
        df_produto,
        values="Quantidade",
        names="produto",
        title="Vendas por Produto"
    )
    st.plotly_chart(fig_pie, use_container_width=True)
