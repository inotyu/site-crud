import streamlit as st
import mysql.connector

from modelos.create import Create
from modelos.read import Read
from modelos.update import Update
from modelos.delete import Delete

conexao = mysql.connector.connect(
    host='127.0.0.1',
    user='root',
    password='',
    database='db_curso'
)

cursor = conexao.cursor()

def main():
    st.title("Sistema de Cadastro com CRUD")
    
    menu = ['Create', 'Read', 'Update', 'Delete', 'Sair']
    choice = st.sidebar.selectbox("Escolha uma opção", menu)
    
    if choice == 'Create':
        st.subheader("Inserir novo registro")
        Create(cursor, conexao)
        
    elif choice == 'Read':
        st.subheader("Visualizar registros")
        Read(cursor, conexao)
        
    elif choice == 'Update':
        st.subheader("Atualizar registro")
        opcao = st.radio("Deseja ver a lista antes de atualizar?", ('Sim', 'Não'))
        
        if opcao == 'Sim':
            Read(cursor, conexao)
            Update(cursor, conexao)
        else:
            Update(cursor, conexao)
    
    elif choice == 'Delete':
        st.subheader("Excluir registro")
        Delete(cursor, conexao)
        
    elif choice == 'Sair':
        st.write("Programa encerrado.")
        st.stop()

if __name__ == '__main__':
    main()
