import streamlit as st
from config import supabase
import datetime

def cadastro_venda():
    st.title("Cadastro de Venda")

    # Busca os animadores no banco
    animadores_data = supabase.table("animador").select("nome").execute().data
    animadores = [a["nome"] for a in animadores_data] if animadores_data else []

    # Busca os Produtos no banco
    produtos_data = supabase.table("produtos").select("nome_prod").execute().data
    produtos = [a["nome_prod"] for a in produtos_data] if produtos_data else []

    with st.form("form_venda"):
        dia = st.date_input("Data Inicial", format="DD/MM/YYYY", value=datetime.date.today())

        nome_cliente = st.text_input("Nome do Cliente")
        numero_cliente = st.text_input("Número do Cliente")
        ramo_cliente = st.text_input("Área de Atuação")
        categoria = st.selectbox("Categoria do Produto", ["vídeo animado", "gestão de tráfego"])
        produto = st.selectbox("Produto", produtos)

        valor = st.number_input("Valor", min_value=0.0)
        custo_animador = st.number_input("Custo do Animador", min_value=0.0)
        
        # Selectbox para escolher animador, opções vindas do BD
        animador = st.selectbox("Nome do Animador", animadores)

        custo_locucao = st.number_input("Custo de Locução", min_value=0.0)
        link_projeto = st.text_input("Link do Projeto")

        submitted = st.form_submit_button("Cadastrar")
        if submitted:
            dados = {
                "dia": dia.isoformat(),
                "nome_cliente": nome_cliente,
                "numero_cliente": numero_cliente,
                "ramo_cliente": ramo_cliente,
                "categoria_produto": categoria,
                "produto": produto,
                "valor": valor,
                "custo_animador": custo_animador,
                "animador": animador,
                "custo_locucao": custo_locucao,
                "link_projeto": link_projeto,
            }
            supabase.table("vendas").insert(dados).execute()
            st.success("Venda cadastrada com sucesso!")
