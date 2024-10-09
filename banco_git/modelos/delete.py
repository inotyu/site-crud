import streamlit as st
import pandas as pd


    

def Delete(cursor, conexao):
    
    
    ver_lista = st.radio('Você deseja ver a lista de alunos antes de apagar?', ('Sim', 'Não'))

    if ver_lista == 'Sim':
        comando = 'SELECT * FROM alunos'
        cursor.execute(comando)
        resultado = cursor.fetchall()
        
        if resultado:
            st.write("Lista de Alunos:")
            st.table(resultado)
        else:
            st.write("Nenhum aluno encontrado.")

    opcao = st.selectbox("Escolha um critério para exclusão:", ["Selecione", "ID", "Nome"])
    
    if opcao == "ID":
        id_aluno = st.number_input('Informe o ID que deseja apagar:', min_value=1)
        if st.button('Deletar por ID'):
            cursor.execute("SELECT id FROM alunos")
            lista_ids = [id[0] for id in cursor.fetchall()]
            if id_aluno and id_aluno in lista_ids:
                comando = 'DELETE FROM alunos WHERE id = %s'
                cursor.execute(comando, (id_aluno,))
                conexao.commit()
                st.success('Aluno com ID deletado com sucesso.')
            elif id_aluno not in lista_ids:
                st.error('Por favor, insira um ID válido.')
    
    elif opcao == "Nome":
        nome_aluno = st.text_input('Informe o nome que deseja apagar:')
        if st.button('Deletar por Nome'):
            cursor.execute("SELECT nome FROM alunos;")
            lista_nome = [nome[0] for nome in cursor.fetchall()]

            if nome_aluno in lista_nome:
                comando = 'DELETE FROM alunos WHERE nome = %s;'
                cursor.execute(comando, (nome_aluno,))
                conexao.commit()
                st.success(f'Aluno com nome {nome_aluno} com sucesso.')
            elif nome_aluno not in lista_nome:
                st.error('O aluno não foi deletado. Verifique se o nome está correto.')
    
    else:
        st.warning('Por favor, selecione uma opção válida para exclusão.')

