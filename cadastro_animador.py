import streamlit as st
from config import supabase
import datetime

def cadastro_animador():
    st.title("Cadastro de Animador")
    
    with st.form("form_animador"):
        nome_animador = st.text_input("Nome do Animador")
        numero_animador = st.text_input("Número do Animador")
        habilidade_1 = st.selectbox("Habilidade 1", ["Vídeo 2D", "Vídeo 3D"])
        habilidade_2 = st.selectbox("Habilidade 2", ["","Vídeo 2D", "Vídeo 3D"])
        
        submitted = st.form_submit_button("Cadastrar")
        if submitted:
            dados = {
                "nome": nome_animador,
                "numero": numero_animador,
                "habilidade_1": habilidade_1,
                "habilidade_2": habilidade_2,
            }
            supabase.table("animador").insert(dados).execute()
            st.success("Animador cadastrado com sucesso!")
