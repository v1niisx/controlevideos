import streamlit as st
from config import supabase
import openpyxl
print("openpyxl funcionando!")


def login():
    st.title("Login")
    usuario = st.text_input("Usuário")
    senha = st.text_input("Senha", type="password")
    if st.button("Entrar"):
        data = supabase.table("login").select("*").eq("usuario", usuario).eq("senha", senha).execute()
        if data.data:
            st.session_state["logado"] = True
            st.success("Login bem-sucedido!")
            st.rerun()  # ✅ Corrigido aqui
        else:
            st.error("Usuário ou senha inválidos")
