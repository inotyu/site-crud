import streamlit as st
import pandas as pd

def Read(cursor, conexao):
    st.header("Tabela: Alunos e Cursos")
    colunas = ["ID", "Nome", "Profissão", "Nascimento", "Sexo", "Peso", "Altura", "Nacionalidade", "Curso Preferido"]
    st.write("Listando todos os alunos:")
    
    comando = '''select a.id, a.nome, a.profissao, a.nascimento, a.sexo, a.peso, a.altura, a.nacionalidade, c.nome
                 from alunos a 
                 inner join cursos c on c.idcurso = a.curso_preferido;'''
    cursor.execute(comando)
    resultado = cursor.fetchall()
    if resultado:
        df = pd.DataFrame(resultado, columns=colunas)
        st.table(df)
    else:
        st.write("Nenhum aluno encontrado.")
