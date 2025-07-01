import streamlit as st
from login import login
from dashboard import dashboard
from cadastro_vendas import cadastro_venda
from cadastro_animador import cadastro_animador
from cadastro_produto import cadastro_produto

# Inicializa o estado de login, se ainda não estiver definido
if "logado" not in st.session_state:
    st.session_state["logado"] = False

# Se o usuário estiver logado, mostra o menu lateral
if st.session_state["logado"]:
    menu = st.sidebar.selectbox("Menu", ["Dashboard", "Cadastrar Venda", "Cadastrar Animador", "Cadastrar Produto", "Cadastrar Gastos", "Sair"])

    if menu == "Dashboard":
        dashboard()
    elif menu == "Cadastrar Venda":
        cadastro_venda()
    elif menu == "Cadastrar Produto":
        cadastro_produto()
    elif menu == "Cadastrar Animador":
        cadastro_animador()
    elif menu == "Sair":
        st.session_state["logado"] = False
        st.rerun()  # ✅ Correto para Streamlit >= 1.25


else:
    login()
