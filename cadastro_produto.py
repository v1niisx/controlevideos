import streamlit as st
from config import supabase
import datetime

def cadastro_produto():
    st.title("Cadastro de Animador")
    
    with st.form("form_animador"):
        nome = st.text_input("Nome do Produto (De a desc completa EX: Video 3D - 20s)")
        desc = st.text_input("Descrição do Produto")
        
        submitted = st.form_submit_button("Cadastrar")
        if submitted:
            dados = {
                "nome_prod": nome,
                "descricao_prod": desc,

            }
            supabase.table("produtos").insert(dados).execute()
            st.success("Produto cadastrado com sucesso!")
