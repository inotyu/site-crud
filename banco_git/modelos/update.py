import streamlit as st
from datetime import datetime

def Update(cursor, conexao):
    st.write("Atualizar informações do Aluno:")
    id_aluno = st.text_input('Digite o id do aluno que deseja atualizar:')
    
    aluno = None 

    if id_aluno:
        comando = 'SELECT * FROM alunos WHERE id = %s'
        cursor.execute(comando, (id_aluno,))
        aluno = cursor.fetchone()

    if aluno:
        nome = st.text_input('Informe o novo nome do aluno:')
        profissao = st.text_input('Informe a nova profissão:')
        nascimento = st.date_input('Informe a nova data de nascimento:',
                                    value=datetime(2000, 1, 1), 
                                    min_value=datetime(1900, 1, 1),  
                                    max_value=datetime.now())  
        sexo = st.selectbox('Selecione o novo sexo:', ['Masculino', 'Feminino', 'Outro'])
        peso = st.number_input('Informe o novo peso (kg):', min_value=0.0, step=0.1)
        altura = st.number_input('Informe a nova altura (m):', min_value=0.0, step=0.01)
        nacionalidade = st.text_input('Informe a nova nacionalidade:')
        ver_lista = st.radio('Você deseja ver a lista de cursos', ('Sim', 'Não'))

        if ver_lista == 'Sim':
            comando = 'SELECT * FROM cursos'
            cursor.execute(comando)
            resultado = cursor.fetchall()
            
            if resultado:
                st.write("Lista de Cursos:")
                st.table(resultado)
            else:
                st.write("Nenhum curso encontrado.")
        
        curso_preferido = st.text_input('Informe o novo curso preferido:').lower()

        if st.button('Atualizar Aluno'):
            if nome: 
                comando = '''UPDATE alunos SET nome = %s, profissao = %s, nascimento = %s, sexo = %s, peso = %s, altura = %s, nacionalidade = %s WHERE id = %s'''
                cursor.execute(comando, (nome, profissao, nascimento, sexo, peso, altura, nacionalidade, id_aluno))
                

                if curso_preferido == 'html5':
                    curso_id = 1
                elif curso_preferido == 'algoritmos':
                    curso_id = 2
                elif curso_preferido == 'photoshop5':
                    curso_id = 3
                elif curso_preferido == 'php':
                    curso_id = 4
                elif curso_preferido == 'java':
                    curso_id = 5
                elif curso_preferido == 'mysql':
                    curso_id = 6
                elif curso_preferido == 'word':
                    curso_id = 7
                elif curso_preferido == 'python':
                    curso_id = 8
                elif curso_preferido == 'poo':
                    curso_id = 9
                elif curso_preferido == 'excel':
                    curso_id = 10
                elif curso_preferido == 'responsividade':
                    curso_id = 11
                elif curso_preferido == 'c++':
                    curso_id = 12
                elif curso_preferido == 'c#':
                    curso_id = 13
                elif curso_preferido == 'android':
                    curso_id = 14
                elif curso_preferido == 'javascript':
                    curso_id = 15
                elif curso_preferido == 'powerpoint':
                    curso_id = 16
                elif curso_preferido == 'swift':
                    curso_id = 17
                elif curso_preferido == 'hardware':
                    curso_id = 18
                elif curso_preferido == 'redes':
                    curso_id = 19
                elif curso_preferido == 'seguranca':
                    curso_id = 20
                elif curso_preferido == 'seo':
                    curso_id = 21
                elif curso_preferido == 'premiere':
                    curso_id = 22
                elif curso_preferido == 'after effects':
                    curso_id = 23
                elif curso_preferido == 'wordpress':
                    curso_id = 24
                elif curso_preferido == 'joomla':
                    curso_id = 25
                elif curso_preferido == 'magento':
                    curso_id = 26
                elif curso_preferido == 'modelagem de dados':
                    curso_id = 27
                elif curso_preferido == 'html4':
                    curso_id = 28
                elif curso_preferido == 'php7':
                    curso_id = 29
                elif curso_preferido == 'php4':
                    curso_id = 30
                else:
                    curso_id = None  

                if curso_id is not None:
                    command = 'UPDATE alunos SET curso_preferido = %s WHERE nome = %s'
                    cursor.execute(command, (curso_id, nome))
                    conexao.commit()
                    st.success('Aluno atualizado com sucesso.')
                else:
                    st.error("Curso preferido não encontrado.")
            else:
                st.error("Por favor, insira informações válidas.")
    else:
        st.warning("Aluno não encontrado. Por favor, verifique o ID.")
